import requests 
from bs4 import BeautifulSoup

def scrape_books(url):
    """
    Scrapes teh titles and prices of books from the given URL of 'BOoks to Scrape'.

    Args:
    url (str): URL of the webpage to scrape

    Returns:
    list of tuples: A list containing tuples of (title, price) of each book.
    """
    # send a GET request to the URL``
    response = requests.get(url)

    books_data = []
    if response.status_code == 200:
        # parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book entires on the page: they are in <article class="product_pod">
        books = soup.findAll('article', class_='product_pod')

        for book in books:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text
            books_data.append((title, price))
    else:
        print('Failed to fetch the webpage', response.status_code)

    return books_data

if __name__ == "__main__":
    # URL of the site to be scraped
    url = 'http://books.toscrape.com/'

    # Call the function to scrape books
    books = scrape_books(url)

    # [(<name>, <price>), (<name>, <price>)]
    for name, price in books:
        print(f"Book: {name}, Price: {price}$")
