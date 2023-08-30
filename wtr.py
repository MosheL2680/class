import requests
def getw(citi):
    
    
    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

getw(input("enter citi:"))