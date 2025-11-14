import requests
from food.constants import URL, HEADERS, PAYLOAD
import re

if __name__ == '__main__':
    response = requests.post(URL, headers=HEADERS, json=PAYLOAD)

    if not response.ok:
        print('Error: ', response.status_code, response.text)
        exit()

    text = response.text

    splitByCourt = re.split(r'(?=\"formalName\":)', text)

    diningCourts = {}
    menu = set()

    for court in splitByCourt[1:]:
        courtMenu = set(
            re.findall(r'"item":\s*{\s*"name":\s*"([^"]+)"', court)
        )
        
        diningCourts[re.findall(r'"formalName":\s*"([^"]+)"', court)[0]] = courtMenu
        
        menu = menu.union(courtMenu)

    print(len(menu))
