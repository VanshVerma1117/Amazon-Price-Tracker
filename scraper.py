import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        try:
            # Title extraction
            title_node = soup.find(id="productTitle") or soup.find(id="title")
            title = title_node.get_text().strip() if title_node else "Title not found"
            
            # Price extraction with multiple selectors
            price = "Price not found"
            price_selectors = ["a-price-whole", "a-offscreen", "priceblock_ourprice"]
            
            for selector in price_selectors:
                found = soup.find(class_=selector) or soup.find(id=selector)
                if found:
                    price = found.get_text().strip()
                    break
            
            print(f"Product: {title}")
            print(f"Current Price: ₹{price}")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    product_url = "https://www.amazon.in/Cockatoo-Adjustable-Equipment-One-Second-Adjustment/dp/B0CTHF8V89/?_encoding=UTF8&pd_rd_w=9ZbYw&content-id=amzn1.sym.af6a98ef-7336-445c-93a2-8e7a381920da&pf_rd_p=af6a98ef-7336-445c-93a2-8e7a381920da&pf_rd_r=E3R7YSG4MMM1GPNXJGVQ&pd_rd_wg=4dGl1&pd_rd_r=7452ca9c-6a1a-4a6c-ac91-3d87756fafb6&ref_=pd_hp_d_atf_dealz_cs_t1&th=1" 
    get_product_data(product_url)


