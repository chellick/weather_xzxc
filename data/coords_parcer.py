import requests
from bs4 import BeautifulSoup as BS

url = "http://meteomaps.ru/meteostation_codes.html"


def get_csv(url="http://meteomaps.ru/meteostation_codes.html"):
    r = requests.get(url=url)
    soup = BS(r.content, "html.parser")
    arr = soup.find_all("td")
    
    result = dict()
    
    for i in range(0, len(arr), 6):
        result[str(arr[i]).replace("<td>", "").replace("</td>", "")] = [
                str(arr[i+2]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+3]).replace("<td>", "").replace("</td>", ""),
                str(arr[i+4]).replace("<td>", "").replace("</td>", "")]
        
    return result
