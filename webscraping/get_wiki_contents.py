def get_wikipedia_contents(url):
    from requests import get
    from bs4 import BeautifulSoup
    
    fetched_data = get(url).text
    soup = BeautifulSoup(fetched_data, 'lxml')
    tocnumbers = soup.select('.tocnumber')
    toctexts = soup.select('.toctext')
    toc = list()
    index = 0
    while index < len(tocnumbers):
        toc.append((tocnumbers[index], toctexts[index]))
        index += 1
        
    def wrapper_format_print():
        for tocnumber, toctext in toc:
            if '.' in tocnumber.text:
               print(f'\t{tocnumber.text} -> {toctext.text}')
            else:
                print(f'{tocnumber.text} -> {toctext.text}')
                
    return wrapper_format_print
  
# test1
if __name__ == '__main__':
  wiki1 = get_wikipedia_contents('https://en.wikipedia.org/wiki/Jonas_Salk')
  wiki2 = get_wikipedia_contents('https://en.wikipedia.org/wiki/Karl_Marx')
  
  wiki1()
  wiki2()
