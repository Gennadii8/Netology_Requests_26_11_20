import requests
from pprint import pprint

response = requests.get("https://api.stackexchange.com/2.2/search?fromdate=1607558400&todate=1607731200&order=desc&sort=creation&tagged=Python&site=stackoverflow")
response.raise_for_status()
result = response.json()
pprint(result)

