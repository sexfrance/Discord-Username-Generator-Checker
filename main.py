import requests 
import random
import yaml
import string

from concurrent.futures import ThreadPoolExecutor
from logmagix import Logger, Home


log = Logger()

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

Home("Discord username checker", credits="discord.cyberious.xyz").display()

def generate_usernames(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def proxy_dict():
    with open("proxies.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        if lines:
            return {"http": "http://" + random.choice(lines), 
                    "https": "https://" + random.choice(lines)}
        else:
            return None

def check_username(username):
    response = requests.post("https://discord.com/api/v9/unique-username/username-attempt-unauthed", json={"username": username}, proxies=proxy_dict())
    if response.status_code == 200:
        taken = response.json()["taken"]
        return taken
    elif response.status_code == 400:
        log.failure(f'Failed to check username: {response.text}')
        return None

def main():
    if config["Mode"] == "generate":
        usernames = []

        with ThreadPoolExecutor(max_workers=config["Threads"]) as executor:
            futures = [
                executor.submit(
                    generate_usernames,
                    random.randint(config["Username_min_length"], config["Username_max_length"])
                )
                for _ in range(config["Usernames_to_gen"])
            ]

            for future in futures:
                try:
                    username = future.result()
                    log.success(f"Generated username: {username}")
                    usernames.append(username)
                except Exception as e:
                    log.error(f"Error generating username: {e}")

        with open("usernames.txt", "w") as f:
            f.write("\n".join(usernames))

        return

    elif config["Mode"] == "check":
        with open("usernames.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            if not lines: 
                username = log.question("Enter a username to check: ").strip()
                usernames = [username]
            else:
                usernames = lines 

        with ThreadPoolExecutor(max_workers=config["Threads"]) as executor:
            futures = {executor.submit(check_username, username): username for username in usernames}
            for future in futures:
                taken = future.result()
                if not taken:
                    log.success(f"Username {username} is available")
                else:
                    log.failure(f"Username {username} is taken")

    elif config["Mode"] == "both":
        with open("usernames.txt", "w") as f:
            with ThreadPoolExecutor(max_workers=config["Threads"]) as executor:
                futures = {executor.submit(generate_usernames, random.randint(config["Username_min_length"], config["Username_max_length"])): None for _ in range(config["Usernames_to_gen"])}
                for future in futures:
                    username = future.result()
                    log.success(f"Generated username: {username}")
                    f.write(username + "\n")

            usernames = [line.strip() for line in f.readlines() if line.strip()] 

        with ThreadPoolExecutor(max_workers=config["Threads"]) as executor:
            futures = {executor.submit(check_username, username): username for username in usernames}
            for future in futures:
                taken = future.result()
                if not taken:
                    log.success(f"Username {username} is available")
                else:
                    log.failure(f"Username {username} is taken")
    else:
        log.failure("Invalid mode, make sure to set it to either 'generate', 'check' or 'both'")
        return

if __name__ == "__main__":
    main()
