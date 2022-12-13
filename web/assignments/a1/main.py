from crawler import Crawler

def main():
    crawler = Crawler()

    while(True):
        print('Select an option:')
        print('1) Add a webpage to the crawler')
        print('2) search for a word')
        print('3) Quit')
        opt = input()
        if opt == '1':
            print('Enter the desired domian')
            domain=input()
            print('Enter an URI')
            uri=input()
            crawler.extract_links(domain, uri)
            print('The pages were added to the index')
        elif opt == '2':
            print('Enter a word')
            word = input()
            results = crawler.search(word)
            print('Results:')
            print(results)
           
        elif opt == '3':
            break
           
        else:
            print('Not a valid option')
        
    pass
if __name__ == "__main__":
    main()