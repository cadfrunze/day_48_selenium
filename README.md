# Samsung S24+ Web Scraper & WhatsApp Notifier

This project is a Python automation script that uses **Selenium** for web scraping and **pywhatkit** for sending WhatsApp messages.  
Its main purpose is to search for a **Samsung S24+** on a target e-commerce website, extract product details (such as name and price), and notify you via WhatsApp when the device is found.

---

## 🚀 Features
- Automated search for **Samsung Galaxy S24+** on the target site.
- Extracts:
  - Product name
  - Product price
  - Product link
- Supports multiple pages of search results.
- Sends a WhatsApp message with product information using **pywhatkit**.

---

## 🛠️ Requirements
- Python 3.10+
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

### Python dependencies:
```bash
pip install selenium python-dotenv pywhatkit