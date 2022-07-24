# Task2 Solution Explanation

## How I solved this task
- Firstly, I created a new file called as "product.py" to write a product class. I wrote a product class for creating product objects. These objects have three attributes. These attributes are name, price and imageLink respectively.
<br/>
- Secondly, I created a new file called as "scrape.py" for scraping the amazon web page which was provided to me. I send a get request to this amazon web page for getting content of this web page by using requests module. For doing web scraping, I used bs4 module. I created a BeautifulSoup object and gave the amazon web page content as one of the arguments of this object.
<br/>
-  Thirdly, I started to examine this Amazon web page and, I realized that all divs which contains product information has class attribute includes "s-card-container". I got these divs by using find_all() method. I used children of each div element to find product name. I got first child of first child of first h2 element of each div for getting product name. Then I used some spans which has class attributes are "a-price-whole", "a-price-fraction" and "a-price-symbol" respectively. I got these spans for finding price of these products. For finding image links of these products, I found all div elements which have class attribute includes "s-product-image-container". I got all these divs. And I searched img element inside each div. And I got src attribute of these img elements. For each product, I created a product object and gave product name,product price and image link to each object. And I added these objects to a product list.    
<br/>
- Finally, for building a simple api I used Flask framework.  I created "app.py" file for writing an API. My api has only one GET route which is root route ("/"). When a user sends a request to my root route, my server calls getData() function. This function calls scrapeProductNamesPricesAndImages() function inside it for scraping the Amazon web page.  And we render Jinja2 templates which includes our "index.html" file and giving our prouducts list to this template. By the way, I created a html file which is "index.html" for showing our Amazon products in a table. Also I created three css files which are "main.css", "tablet.css" and "mobile.css" respectively for giving style to our html file. 
  
## How I can execute solution of Task2
You only run app.py file to reach solution of this task. However, my pyhton files use flask, requests and bs4 module. So for running these scripts you must have these modules. If you don't have these modules, you can download these modules by using PyPI. Open your terminal and run the commands below orderly.
```
    pip install Flask
    pip install requests
    pip install bs4
```
If you downloaded these modules you can run "app.py" file. Simply go to the place where this file locates in terminal and run the command below in your terminal.
```
    py app.py
```
You will see this output below. Please go to "http://127.0.0.1:5000" web adress.
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 203-995-032
```
