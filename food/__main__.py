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

    for court in splitByCourt[1:]:
        diningCourts[re.findall(r'"formalName":\s*"([^"]+)"', court)[0]] = set(
            re.findall(r'"item":\s*{\s*"name":\s*"([^"]+)"', court)
        )

    print(diningCourts)
