def get_title_of(url):
    from requests import get
    from bs4 import BeautifulSoup
    
    fetched_data = get(url)
    soup = BeautifulSoup(fetched_data.text, 'lxml')
    title = soup.select('title')[0].getText()
    return title
  
# test1
get_title_of('http://example.com')
  
# test2
get_title_of('https://python.org')
  
