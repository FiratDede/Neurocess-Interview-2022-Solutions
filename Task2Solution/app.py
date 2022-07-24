from flask import Flask,render_template
from scrape import scrapeProductNamesPricesAndImages


app=Flask(__name__)

@app.route('/')
def getData():
    """ Displays the index page accessible at '/'
    """
    
    # Do scraping
    products=scrapeProductNamesPricesAndImages()
 
    # Calculate total number of products
    totalProductNumber=len(products)
    
    return render_template('index.html',products=products,totalProductNumber=totalProductNumber)


if(__name__=="__main__"):
    app.run(debug=True)