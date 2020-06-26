import json
import requests
import time
from tqdm import tqdm

class WikiSearch:
    def __init__(self, name):
        self.name = name
    
    def search_request(self):
        url = "https://en.wikipedia.org/w/api.php"
        session = requests.Session()
        params = {
            "action": "opensearch",
            "namespace": "0",
            "search": self.name,
            "limit": "1",
            "format": "json"
        }
        response = session.get(url=url, params=params)
        result = response.json()
        return result[3]
    

class MyIterator:
    def __init__(self, value):
        self.value = value
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            self.current = self.value[self.index]['name']['official']
            self.index += 1
            return self.current
        except IndexError:
            raise StopIteration

if __name__ == "__main__":

    with open('countries.json', encoding='utf-8') as f:
        data = json.load(f)
        countries_list = []
        url_list = []
        result_list = []
        for countries in tqdm(MyIterator(data)):
            countries_list.append(countries)
            url = WikiSearch(countries)
            url = url.search_request()
            time.sleep(0.05)
            try:
                url_list.append(url[0])
            except IndexError:
                url_list.append('no link found')
                continue
        result_list = zip(countries_list, url_list)
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(str(tuple(result_list)))
        f.close()