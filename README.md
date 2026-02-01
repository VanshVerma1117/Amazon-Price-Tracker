🚀 Amazon Price Tracker: Resilient Web Scraping Project
Project Overview
A high-performance Python-based automation tool designed to monitor and log prices for multiple products on Amazon India. This project was engineered to demonstrate core competencies in Data Engineering, Asynchronous Request Handling, and Anti-Bot Mitigation.

Technical Stack
Language: Python 3.11+

Libraries: Requests (Networking), BeautifulSoup4 (HTML Parsing), CSV (Data Storage), Re (Regex Sanitization)

Tools: VS Code, Zsh Terminal

Engineering Challenges & Solutions
1. Anti-Scraping & Bot Detection
Challenge: Amazon implements sophisticated rate-limiting and IP-level shadow banning.

Solution: Developed a multi-layered stealth strategy including User-Agent rotation, randomized execution delays (6-11s), and Session Management to mimic organic human browsing patterns.

2. Dynamic Data Extraction
Challenge: E-commerce platforms frequently update HTML class names, causing standard scrapers to break.

Solution: Built a resilient selector logic that queries multiple CSS fallback paths to ensure data integrity across different product categories.

3. URL Sanitization
Challenge: Raw Amazon URLs contain lengthy tracking parameters that increase payload and detection risk.

Solution: Integrated Regular Expressions (Regex) to automatically sanitize links into their shortest canonical form (ASIN-based), improving script efficiency.

Key Learning Outcomes
Advanced understanding of HTTP/1.1 Request/Response cycles.

Experience diagnosing Network-level rate limiting and implementing back-off strategies.

Proficiency in File I/O operations for structured data logging (CSV).
