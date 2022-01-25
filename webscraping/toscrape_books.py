def get_books(url, star_rating=None):
    from requests import get
    from bs4 import BeautifulSoup
    
    fetched = get(url).text
    soup = BeautifulSoup(fetched, 'lxml')
    
    product_pods = soup.select('.product_pod')
    rating_dict = {
        1:'One',
        2:'Two',
        3:'Three',
        4:'Four',
        5:'Five'
    }
    books = []
    if star_rating:
        index = 0
        while index < len(product_pods):
            if(product_pods[index].select(f'.star-rating.{rating_dict[star_rating]}')):
                base = product_pods[index].select('a')
                
                src = base[0].select('img')[0]['src']
                image_link = 'https://books.toscrape.com' + src[2:]
                
                title = base[1]['title']
                
                books.append((title, image_link))
            index += 1
    
    return books

if __name__ == '__main__':
    books = get_books('https://books.toscrape.com/catalogue/page-1.html', 3)

    from IPython import display
    from PIL import Image
    from requests import get

    for book_title, book_image in books:
        print(book_title)
        print(book_image)
