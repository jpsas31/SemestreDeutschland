#link-texts == hypertext
import bs4 ## library to parse html
import re
import urllib

class Store():
    def __init__(self, domain:str, html:str) -> None:
        
        self.domain = domain
        self.html = html
        self.pages= {} 
        self.terms={}


    def add_link(self) -> None:
        soup = bs4.BeautifulSoup(self.html,features='lxml')
       
        for link in soup.find_all('a', href=True):
         
            if (self.domain in link['href'] or re.search('^/.*/$', link['href'])) and len(link.text) != 0:
                url =  urllib.parse.urljoin(self.domain,link['href'])
                text = link.text.lower()
                for word in text.split(' '):
                    self.terms[word] = (url,text)
                    
                self.pages[url]=text
         

               
        
    def search(self, searchStr:str) -> list:
        searchResults={}
        for word in searchStr.split(' '):
            if word in self.terms and self.terms[word][0] not in searchResults :
                searchResults[self.terms[word][0]]=self.terms[word][1]

        return searchResults


    def getLinks(self):
        return self.pages.keys()

    

