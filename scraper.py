import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    # Headers make the request look like it's coming from a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Note: Selectors change per website. This is a generic example.
        try:
            title = soup.find(id="productTitle").get_text().strip()
            price = soup.find(class_="a-price-whole").get_text().strip()
            print(f"Product: {title}")
            print(f"Current Price: ₹{price}")
        except AttributeError:
            print("Could not find product details. Check the HTML tags.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

# Test with a sample URL
if __name__ == "__main__":
    product_url = "https://www.amazon.in/dp/B0CXF43N73" # Replace with any real link
    get_product_data(product_url)
