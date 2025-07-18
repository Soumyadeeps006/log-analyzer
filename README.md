# 📄 Log File Analyzer

[![License](https://img.shields.io/badge/license-MIT-blue.svg )](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg )](https://www.python.org)

A simple yet effective **Log File Analyzer** written in Python.  
This tool reads a log file, identifies all lines containing the word `ERROR`, and writes a summary to a report file.

---

## 🧩 Features

✅ Reads a log file (`app.log`)  
✅ Counts the number of lines with the word `ERROR`  
✅ Writes the results to an output file (`error_report.txt`)  
✅ Gracefully handles common file-related errors:  
 - File not found  
 - Permission denied  
 - General I/O errors  

---

## 📁 Project Structure

log-analyzer/
│
├── log_analyzer.py # Main script
├── app.log # Sample log file
├── error_report.txt # Output file
├── README.md # This file
└── LICENSE # MIT License

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Soumyadeeps006/log-analyzer.git
cd log-analyzer
```

### 2. Run the script

```bash
python log_analyzer.py
```

---

## 📝 Sample Output (error_report.txt)

Total ERROR entries: 3
List of ERROR lines:
2025-04-05 10:01:00 ERROR Failed to connect to database
2025-04-05 10:03:00 ERROR Invalid credentials
2025-04-05 10:06:00 ERROR Failed to load resource: /img/logo.png

---

## 🛠 Requirements

* Python 3.6 or higher

No external libraries are required. Just pure Python!

---

## 🔐 License
This project is licensed under the MIT [LICENSE](LICENSE).