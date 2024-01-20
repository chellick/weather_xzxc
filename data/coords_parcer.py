import requests
from bs4 import BeautifulSoup as BS
import os

url = "http://meteomaps.ru/meteostation_codes.html"


def get_csv(url="http://meteomaps.ru/meteostation_codes.html"):
    r = requests.get(url=url)
    soup = BS(r.content, "html.parser")
    arr = soup.find_all("td")
    
    result = []
    
    for i in range(0, len(arr), 6):
        result.append([
                str(arr[i]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+2]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+3]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+4]).replace("<td>", "").replace("</td>", "")])
        
    return result


def get_valid_coords():
    result = dict()
    net_coords = get_csv()
    for i in os.listdir('C://python//GitHub//weather_xzxc//data//srock8//'):
        sin_index = int(i.replace('.dat', ''))
        for coords in net_coords:
            try:
                if sin_index == int(coords[0]):
                    result[sin_index] = [int(i) for i in coords[1:]]
            except:
                ...
    return result
            