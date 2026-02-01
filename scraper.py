import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def get_product_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Title extraction
            title_node = soup.find(id="productTitle") or soup.find(id="title")
            title = title_node.get_text().strip() if title_node else "Title not found"
            
            # Price extraction
            price = "Price not found"
            price_selectors = ["a-price-whole", "a-offscreen", "priceblock_ourprice"]
            for selector in price_selectors:
                found = soup.find(class_=selector) or soup.find(id=selector)
                if found:
                    price = found.get_text().strip()
                    break
            
            return {"title": title, "price": price, "status": "Success"}
    except Exception as e:
        return {"title": "Error", "price": "Error", "status": str(e)}
    return {"title": "N/A", "price": "N/A", "status": f"Failed {response.status_code}"}

if __name__ == "__main__":
    # 1. Read links from your text file
    with open("links.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"--- Starting Scraper for {len(urls)} items ---")
    
    results = []
    for link in urls:
        print(f"Checking: {link[:50]}...")
        data = get_product_data(link)
        data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        results.append(data)

    # 2. Save results to a professional CSV (Excel-ready) file
    with open("prices.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "title", "price", "status"])
        writer.writeheader()
        writer.writerows(results)

    print("--- Done! Results saved to prices.csv ---")


