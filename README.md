<div align="center">
 
  <h2 align="center">Discord Username Checker</h2>
  <p align="center">
    This script is a discord username checker for Discord that features proxy support and efficient batch processing. It reads usernames from a text file, validates their availability against Discord's API, and provides formatted output.
    <br />
    <br />
    <a href="https://discord.cyberious.xyz">💬 Discord</a>
    ·
    <a href="https://github.com/sexfrance/Discord-Username-Generator-Checker#-changelog">📜 ChangeLog</a>
    ·
    <a href="https://github.com/sexfrance/Discord-Username-Generator-Checker/issues">⚠️ Report Bug</a>
    ·
    <a href="https://github.com/sexfrance/Discord-Username-Generator-Checker/issues">💡 Request Feature</a>
  </p>
</div>

### ⚙️ Installation

- Requires: `Python 3.7+`
- Make a python virtual environment: `python3 -m venv venv`
- Source the environment: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS, Linux)
- Install the requirements: `pip install -r requirements.txt`

---

### 🔥 Features

- Checks Discord usernames availability quickly
- Supports both proxy and proxyless modes
- Logs results with different status (Available, Taken)
- Efficient rate limit handling
- Saves results to separate files

---

### 📝 Usage

- Prepare a file named `usernames.txt` with usernames to check, one per line
- (Optional) Prepare a file named `proxies.txt` with proxies, one per line
- Configure the settings in `config.yml`
- Run the script:
  ```sh
  python main.py
  ```

---
### ❗ Disclaimers

- This tool is for educational purposes only
- I am not responsible for any misuse or for any Discord API restrictions that may occur
- Use at your own risk and respect Discord's Terms of Service

---

### 📜 ChangeLog

```diff
v0.0.1 ⋮ 09/12/2023
! Initial release
```

---

<p align="center">
  <img src="https://img.shields.io/github/license/sexfrance/Discord-Username-Generator-Checker.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=IOTA"/>
  <img src="https://img.shields.io/github/stars/sexfrance/Discord-Username-Generator-Checker.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=IOTA"/>
  <img src="https://img.shields.io/github/languages/top/sexfrance/Discord-Username-Generator-Checker.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=python"/>
</p>
