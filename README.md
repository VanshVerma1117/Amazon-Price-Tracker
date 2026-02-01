# 🚀 Amazon Price Tracker: Resilient Web Scraping Project

## **Project Overview**
This is a **Python-based automation tool** built to track product prices on Amazon India. The project serves as a case study in handling **real-world web security**, data sanitization, and automated logging.

## **Technical Stack**
* **Language:** Python 3.11+
* **Libraries:** `Requests` (Networking), `BeautifulSoup4` (HTML Parsing), `CSV` (Storage), `Re` (Regex)
* **Environment:** VS Code / macOS Terminal

## **Key Features (What Worked)**
* **URL Sanitization:** Integrated **Regular Expressions** to strip tracking junk from long Amazon links, improving request efficiency.
* **Data Logging:** Successfully automated the creation of a **structured CSV file** containing timestamps, titles, and prices.
* **Stealth Logic:** Implemented **User-Agent rotation** and **randomized sleep timers** to mimic human behavior.

## **Engineering Challenges (What Failed & Lessons Learned)**
One of the most valuable parts of this project was encountering and diagnosing **industrial-grade security measures**:

* **IP Shadow Banning:** Faced persistent blocks even when using mobile hotspots. This highlighted the sophistication of **Amazon's anti-bot algorithms**.
* **Persistent CAPTCHAs:** Identified that manual browser verification is sometimes required to reset a "trust score" for a specific network.
* **Browser Fingerprinting:** Learned that Amazon tracks more than just IP; they monitor **device signatures**, making basic `requests` scripts vulnerable to detection over time.

## **How to Run**
1. Ensure `links.txt` contains your shortened Amazon URLs.
2. Run the script via terminal:
   ```zsh
   python3 scraper.py
