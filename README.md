<p align="center">
  <img src="assets/logo.png" alt="catsay Logo" width="200"/>
</p>

<h1 align="center">catsay</h1>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python: 3.6+"/></a>
</p>

<p align="center">
  A terminal-based feline messenger. Inspired by <code>cowsay</code>, but for those who prefer whiskers and attitude.
</p>

---

### ✨ Features

- **Dynamic Bubbles:** Speech bubbles that wrap and scale with your message.
- **Custom Cat Assets:** Load various cat designs from the `catfiles/` directory.
- **Piped Input:** Works seamlessly with `echo`, `cat`, or other CLI outputs.
- **Lightweight:** Pure Python with no external dependencies.

---

### 🚀 Quick Start

> [!TIP]
> Make sure you have **Python 3.6+** installed before proceeding.

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anon4You/catsay.git
   cd catsay
   ```

2. **Make it executable**
   ```bash
   chmod +x catsay.py
   ```

3. **Run it!**
   ```bash
   ./catsay.py "Hello, Human."
   ```

---

### 🛠 Usage

```text
Usage: catsay [OPTIONS] [MESSAGE]

Options:
  -l, --list             List all available cat designs
  -c, --cat NAME_PATH    Specific cat name from catfiles/ or a custom file path
  -h, --help             Show the help message
```

#### Examples

**The Classic Meow**
```bash
./catsay.py "Stay pawsitive!"
```

**Choose Your Cat**
```bash
./catsay.py -c grumpy "I hate Mondays."
```

**Pipe to Cat**
```bash
fortune | ./catsay.py
```

> [!TIP]
> You can chain multiple commands with pipes — anything that prints to stdout can be fed straight into `catsay`.

---

### 📂 Directory Structure

```text
.
├── catsay.py        # The engine
└── catfiles/        # Your ASCII art collection
    ├── greeting.txt # Default cat
    ├── grumpy.txt
    └── ...
```

---

### 🤝 Connect

- **GitHub:** [Anon4You](https://github.com/Anon4You)
- **Telegram:** [@nullxvoid](https://t.me/nullxvoid)
- **Instagram:** [@alienkrishn](https://instagram.com/alienkrishn)

---

> [!NOTE]
> This project is provided strictly for **educational purposes**. No real cats were harmed in the making of this script.
