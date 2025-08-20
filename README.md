# Python Keylogger (Proof of Concept)

**Author:** Steve Park
**Date:** August 2025

This project is a simple **keylogger proof of concept** built in Python using the [`pynput`](https://pypi.org/project/pynput/) library.
It is intended **strictly for research and practice purposes** — for example, to study how keystroke logging works at a technical level.

⚠️ **Disclaimer:**
This project is for **educational use only**. Do not use this software on any system without explicit permission. Unauthorized use may be illegal and unethical.

---

## Features

- Captures keystrokes system-wide
- Logs to a file (`logs.txt`) in the same directory
- Handles special keys with readable formatting:
  - `Space` → `" "`
  - `Enter` → `"\n"`
  - `Tab` → `[TAB]`
  - `Shift` → `[SHIFT]`
  - `Backspace` → `[BACKSPACE]`

---

## Requirements

- Python 3.8+
- [`pynput`](https://pypi.org/project/pynput/)

Install dependencies:

```bash
pip install pynput
```
Your requirements.txt should contain:
```
pynput
```
## Usage

Clone the repo and run the script.

```bash
git clone https://github.com/wrmgt/python-keylogger.git
cd ~/python-keylogger/src
python3 keylogger.py
```
The program will start listening for keystrokes immediately.
Captured keys will be appended to the log.txt file in the same directory.

## Roadmap (optional ideas)

Roadmap (optional ideas)
- Add CLI flags for specifying the log file location
- Option to record timestamps with keystrokes
- Suport for stopping the logger with a hotkey
- Potentially re-writing in C as a self-contained executable
- Ability to report out to a remote C2
