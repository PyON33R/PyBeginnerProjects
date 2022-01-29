def select_type(url, element):
    from requests import get
    from bs4 import BeautifulSoup
    
    fetched_data = get(url)
    soup = BeautifulSoup(fetched_data.text, 'lxml')
    result = soup.select(element)
    
    return result
 
# test1
select_type('http://example.com', 'a')
