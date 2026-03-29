#  Tree.py — Directory Tree Generator

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge\&logo=python)
![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

> **Tree.py** is a lightweight, zero-dependency Python tool that generates clean, professional ASCII directory trees for documentation, READMEs, and project overviews.

---

# ✨ Features

* 🌲 **Professional tree formatting** using `├──` and `└──`
* ⚡ **Fast recursive scanning**
* 🛡️ **Handles permission errors safely**
* 📄 **UTF-8 encoding** for correct symbol display
* 💻 **Cross-platform** (Windows, Linux, macOS)
* 📦 **No external libraries required**

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Tree.py.git
cd Tree.py
```

Or simply download the script file.

---

# ▶ Usage

Run the script:

```bash
python tree.py
```

You will be prompted to:

1. Enter the folder path
2. Enter output file name

Example:

```
Enter folder path: /home/user/project
Enter output file name: structure.txt
```

---

# 📊 Example Output

```
MyProject/
├── .github/
│   └── workflows/
│       └── main.yml
├── src/
│   ├── main.py
│   ├── utils.py
│   └── templates/
│       └── index.html
├── .gitignore
├── README.md
└── requirements.txt
```

---

# ⚙ How it Works

Tree.py uses a **recursive depth-first search (DFS)** algorithm:

* Traverses directories layer by layer
* Detects last items in each folder
* Applies proper tree connectors
* Maintains consistent indentation

This ensures accurate and visually clean structures.

---

# 🧪 Requirements

Python **3.6 or newer**

Check version:

```bash
python --version
```

---

# 📁 Project Structure Example

```
Tree.py/
├── tree.py
├── README.md
└── LICENSE
```

---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork the repository
2. Create a branch

   ```bash
   git checkout -b feature-name
   ```
3. Commit changes

   ```bash
   git commit -m "Add feature"
   ```
4. Push branch

   ```bash
   git push origin feature-name
   ```
5. Open Pull Request

---

# 📄 License

Distributed under the **MIT License**.

You are free to use, modify, and distribute this software.

---

# 👨‍💻 Author

Built for developers who like clean documentation.

---
