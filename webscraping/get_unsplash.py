def get_unsplash(url):
    from requests import get
    from bs4 import BeautifulSoup
    
    fetched = get(url).text
    soup = BeautifulSoup(fetched, 'lxml')
    img_data = soup.select('.YVj9w')
    img_urls = []
    index = 0
    while index < len(img_data):
        try:
            img_urls.append(img_data[index]['src'])
        except Exception as e:
            print(f"Encountered an Error -> {type(e).__name__}, {e}")
        index += 1
        
    def save_to_file():
        num = 1
        for url in img_urls:
            image = get(url)
            with open('image' + str(num) + '.jpg', 'wb') as file:
                file.write(image.content)
            num += 1
    return save_to_file
