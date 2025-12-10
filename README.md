# kidexa

Stop writing Regex to clean numbers. Convert messy strings to numbers instantly.

## 🚀 The Problem

Every Python developer has faced this error when scraping data or processing user input:

```
ValueError: invalid literal for int() with base 10: '$ 1,200.00'
```

Cleaning these strings manually using regex is repetitive and error-prone.

## 💡 The Solution

**kidexa** is a lightweight utility that takes any messy string and converts it into a valid number (integer or float).  
It automatically handles:

- Currency symbols  
- Commas  
- Extra words  
- Social media suffixes (`k`, `m`, `b`)  
- Random special characters  

## 📦 Installation

```bash
pip install kidexa
```

## 🛠 Usage

```python
from kidexa import sloppy_number

print(sloppy_number.parse("$ 1,200.00"))   # Output: 1200
print(sloppy_number.parse("Rs. 450/-"))    # Output: 450

print(sloppy_number.parse("2.5k views"))   # Output: 2500
print(sloppy_number.parse("2M followers")) # Output: 2000000

print(sloppy_number.parse("Order #555"))   # Output: 555
print(sloppy_number.parse("N/A"))          # Output: None
```

## ✨ Features

- Currency Support  
- Commas  
- Multipliers (k, m, b)  
- Smart Typing  
- Safe (returns None if invalid)  

## 📝 Use Cases

- Web Scraping  
- Data Analysis  
- Social Media Bots  
- Backend Validation  

## 🤝 Contributing

Pull requests are welcome!

## 📄 License

MIT License
- [LICENSE](LICENSE) file for details.