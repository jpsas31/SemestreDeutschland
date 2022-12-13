from store import Store
import requests
import pickle

class Crawler():
    def __init__(self) -> None:
        pass
        self.searchResults={} 
        self.uriQueue = []
        self.uriVisited = []
        self.location = __file__[:__file__.rindex('/')+1] + 'searchResults.b'
        try:
           
            self.searchResults=pickle.load(open(self.location, 'rb'))
        except:
            print('there were no search results saved')
    
    def fetch(self, domain:str, URI:str) ->None:
        try:
            response = requests.get(domain+URI)
            if response.status_code == 200:
                return response.content
            return None
        except:
            print('Error: the webpage you chose is not available')
            return None
      
           
            
       
    def extract_links(self, domain:str, URI:str, maxDepth:int = 50):

        if 'http://' not in domain and 'https://' not in domain:
            domain = 'https://'+domain

        if domain+URI in self.searchResults: return
        
        uriQueue = []
        uriQueue.append(domain+URI)
        level=0
        fileStore = open(self.location, "wb" )
        print("extracting links....")

        while len(uriQueue) != 0 and level <= maxDepth:
            currentUri = uriQueue.pop(0)
            html=self.fetch(domain,URI)
            if html is None:
                continue

            store = Store(currentUri,html)
            store.add_link()
            self.searchResults[currentUri] = store
            pickle.dump(self.searchResults, fileStore)
            for link in store.getLinks():
                if link not in self.searchResults:
                    uriQueue.append(link)
                    
            level = level + 1
            
        fileStore.close()

    def search(self, searchStr:str):
        searchStr= searchStr.lower()
        results={}
        print('searching...')
        for store in self.searchResults.values():
            results.update(store.search(searchStr))
        
        return results






