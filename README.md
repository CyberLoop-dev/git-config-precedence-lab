<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:0f766e&height=170&section=header&text=git%20config%20precedence%20lab&fontSize=36&fontColor=ffffff&animation=twinkling" alt="Animated wave header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=14B8A6&center=true&vCenter=true&width=760&lines=git%20config%20precedence%20lab%20%7C%20inspect%2C%20understand%2C%20improve" alt="Animated title"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/git-config-precedence-lab?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/git-config-precedence-lab?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/git-config-precedence-lab?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/git-config-precedence-lab?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="assets/mark.svg" alt="git-config-precedence-lab project mark" width="520"/></p>

## 🧭 Overview

`git-config-precedence-lab` reads explicitly supplied Git-style config files from lowest to highest precedence. It reports effective section/key values and the file that supplied each winning value. It uses sample files by default and never reads your real Git configuration unless you pass those paths yourself.

## ✨ Features

- 🧭 Shows which config file wins for each section and key
- 🧾 Preserves source-file provenance for overridden values
- 🔤 Treats section and variable names case-insensitively while keeping subsection names distinct
- 🛡️ Read-only: it never invokes Git or changes configuration files
- 📤 Supports JSON output for scripts and comparisons

## 🧪 Demo

Run `python main.py sample/system.gitconfig sample/global.gitconfig sample/local.gitconfig`. The output shows local settings taking precedence over global and system values. No hosted demo is published.

## 🚀 Quick Start

```bash
python main.py sample/system.gitconfig sample/global.gitconfig sample/local.gitconfig
python main.py system.conf global.conf local.conf --json
python -m unittest discover -s tests
```
Requires Python 3.10 or newer. No third-party packages are needed.

## 🧰 Tech Stack

- **Stack:** Python 3.10+ (standard library only)
- **Approach:** small, local-first tooling with clear output

## 🗂️ Folder Structure

```text
git-config-precedence-lab/
├── assets/mark.svg
├── sample/system.gitconfig
├── sample/global.gitconfig
├── sample/local.gitconfig
├── tests/test_main.py
├── main.py
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🛣️ Roadmap

- Add support for Git-style escaped subsection values
- Add an optional explanation of common configuration scopes

## 🤝 Contributing

Issues and focused pull requests are welcome. Explain the use case, keep changes small, and add tests for behavior changes. Run the project using the Quick Start instructions before submitting.

## 📄 License

Released under the [MIT License](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:0f172a&height=120&section=footer&animation=twinkling" alt="Animated wave footer"/></p>
