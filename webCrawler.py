# Author: Partha Pratim Neog
# Email: thisisppn@gmail.com
# Usage: Scraping the site "www.shopping.com" to find out required data.

from bs4 import BeautifulSoup
import requests
import sys
import re
#Get arguments from command line
arguments = sys.argv
arg_count = len(sys.argv)

#Distinguish query type based on number of arguments & Validation
if arg_count == 2:
    keyword = arguments[1]
    base_url = "http://www.shopping.com/products?KW="+keyword
    print("Scraping",base_url)
elif arg_count == 3:
    page=arguments[1]
    patterOnlyNumber = re.compile("^[0-9]*$")
    match = patterOnlyNumber.match(page)
    if match is None:
        sys.exit("Parameter 1 needs to be a number")

    keyword = arguments[2]
    base_url = "http://www.shopping.com/products~PG-"+page+"?KW="+keyword
    print("Scraping",base_url)
else:
    base_url = ""
    sys.exit("Invalid number of arguments")


#Scraping process starts
try:
    raw_html = requests.get(base_url)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    out = soup.select(".numTotalResults")
    if len(out)>0:
        #If query is type 1, then only find out the total Number of results
        if arg_count == 2:
            req_string = out[0].string
            arr = req_string.split(" ")
            totalResults = arr[5]
            print("Total number of results is:",totalResults)
            sys.exit()

        #else, find and print out the "Title" and "Price" of all the items in the current page
        all_items = soup.select(".gridBox")
        # print(all_items)
        if len(all_items) > 0:
            for item in all_items:
                productName = item.select(".productName > span")
                productPrice = item.select(".productPrice > a")
                productShipping = item.select(".taxShippingArea > span")

                ##################################
                if len(productShipping) > 0:
                    print(productName[0]['title'].strip())
                else:
                    productName = item.select(".productName")
                    print(productName[0]['title'])

                ###################################
                if len(productShipping) > 0:
                    print(productPrice[0].string.strip())
                else:
                    productPrice = item.select(".productPrice")
                    print(productPrice[0].string)

                ###################################
                if len(productShipping) > 0:
                    print(productShipping[0].string.strip())
                else:
                    productShipping = item.select(".freeShip")
                    if len(productShipping) > 0:
                        print(productShipping[0].string)
                print("--------------------------------------")
        else:
            print("No items to display!")
    else:
        print("No Results for the Keyword \"",keyword,"\"")
except Exception:
    print("Oops! Something went wrong. Please check your arguments and try again.")


