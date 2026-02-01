import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import random
import re
from datetime import datetime

def clean_amazon_url(url):
    match = re.search(r"/(dp|gp/product)/(B[A-Z0-9]{9})", url)
    return f"https://www.amazon.in/dp/{match.group(2)}" if match else url

def get_product_data(session, url):
    # Expanded list of identities to stay hidden
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
    ]
    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
        "Referer": "https://www.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Cache-Control": "no-cache"
    }
    
    target_url = clean_amazon_url(url)
    
    for attempt in range(2):
        try:
            # Random wait before the very first request
            time.sleep(random.uniform(2, 5))
            response = session.get(target_url, headers=headers, timeout=20)
            
            # If Amazon gives us the 'Robot' page, response.text usually contains 'api-services-support'
            if response.status_code == 200 and "api-services-support" not in response.text:
                soup = BeautifulSoup(response.content, "html.parser")
                title_node = soup.find(id="productTitle")
                
                if title_node:
                    title = title_node.get_text().strip()
                    price = "N/A"
                    # Deep search for the price across 5 different tags
                    for s in ["span.a-price-whole", "span.a-offscreen", "#priceblock_ourprice", ".a-color-price", "span.a-price span.a-offscreen"]:
                        found = soup.select_one(s)
                        if found:
                            price = found.get_text().strip().replace('₹', '').replace(',', '').split('.')[0]
                            break
                    return {"title": title, "price": price, "status": "Success"}
            
            print(f"   ⚠️ Blocked (Attempt {attempt+1}). Waiting 20 seconds...")
            time.sleep(random.uniform(18, 25)) 
            
        except Exception:
            continue
            
    return {"title": "Bot Detected", "price": "N/A", "status": "Failed"}

if __name__ == "__main__":
    current_folder = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_folder, "prices.csv")
    links_path = os.path.join(current_folder, "links.txt")

    try:
        with open(links_path, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: links.txt not found!")
        urls = []

    print(f"--- Starting Final Resilient Scraper ({len(urls)} items) ---")
    session = requests.Session()
    results = []

    for link in urls:
        print(f"🔍 Fetching Data...")
        data = get_product_data(session, link)
        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        results.append(data)
        
        # Long, randomized delay between products
        wait = random.uniform(10, 15)
        print(f"   Result: {data['price']} | Waiting {wait:.1f}s...")
        time.sleep(wait) 

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "title", "price", "status"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ DONE: Check your prices.csv now!")


