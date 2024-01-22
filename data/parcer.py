import requests
from bs4 import BeautifulSoup as BS
import os

url = "http://meteomaps.ru/meteostation_codes.html"


def get_coords(url="http://meteomaps.ru/meteostation_codes.html"):
    r = requests.get(url=url)
    soup = BS(r.content, "html.parser")
    arr = soup.find_all("td")
    
    result = []
    
    for i in range(0, len(arr), 6):
        result.append([
                str(arr[i]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+2]).replace("<td>", "").replace("</td>", "").replace(',', '.'),
                str(arr[i+3]).replace("<td>", "").replace("</td>", "").replace(',', '.'),
                str(arr[i+4]).replace("<td>", "").replace("</td>", "").replace(',', '.')])
        
    return result

def get_valid_coords(result):
    files = []
    for r in result:
        for i in os.listdir('srock8/'):
            station_index = i.replace('.dat', '').replace('.csv', '').replace('.xslx', '')
            if station_index == r[0]:
                files.append([i, r[1:]])
                break
    return files
                
# print(get_valid_coords(get_coords(url)))