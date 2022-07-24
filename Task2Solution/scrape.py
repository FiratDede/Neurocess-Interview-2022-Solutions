from requests import Session 
from bs4 import BeautifulSoup
import html
from product import Product

"""
    scrapeProductNamesPricesAndImages does scraping the amazon website
    which was provided by the pdf file. This function returns a product
    list.
"""
def scrapeProductNamesPricesAndImages():
    # Create Products List
    products=[]
    
    session = Session()

    # Prepare headers for the request
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

    # The url which is scraped
    url="https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4"

    # Make a get request to the url with the provided headers
    page = session.get(url,headers=headers)

    # Raise HTTPError, if one occured
    page.raise_for_status()


    # Create a beautiful soup object for parsing html.
    soup = BeautifulSoup(page.content, "html.parser")

    #Find all divs which include 's-card-container' value in its class attribute 
    productCards=soup.find_all("div",class_="s-card-container")

    #Iterate in these divs
    for productCard in productCards:

        #Find product name of the card
        newProductName = html.unescape( productCard.find("h2",).findChild().findChild().text )
        
        #Find price value of the product
        newPrice="" 
        newWholePrice=productCard.find("span", class_="a-price-whole")
        if(newWholePrice!=None):
            newWholePrice=newWholePrice.text
            newPriceFraction=productCard.find("span",class_="a-price-fraction").text
            newPriceSymbol=productCard.find("span",class_="a-price-symbol").text
            newPrice=newWholePrice+newPriceFraction+" "+newPriceSymbol

        else:
            newPrice="Not Available"

        
        # Find image link of the product
        newProductImageLink=productCard.find("div",class_="s-product-image-container")

        if(newProductImageLink!=None):
            newProductImageLink=newProductImageLink.find("img").get("src")
        else:
            newProductImageLink=""

        # Create a product object
        newProduct= Product(newProductName,newPrice,newProductImageLink)

        # Add this object to products list
        products.append(newProduct)
    
    #Return products list
    return products


        
    