URL = 'https://api.hfs.purdue.edu/menus/v3/GraphQL'

PAYLOAD = {
    'operationName': 'getLocationMenu',
    'variables': {'date': '2025-11-13'},
    'query': """
    query getFoodNames($date: Date!) {
      diningCourts {
        formalName\n
        dailyMenu(date: $date) {
          meals {
            name
            stations {
              name
              items {
                item {
                  name
                }
              }
            }
          }
        }
      }
    }
    """,
}

HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0',
}
