import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

def trn(org):
    payload = {
        "q": org,
        "target": "he",
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "223bef9639msh208f10b5b53f489p1276cejsn8383fd52c58f",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    translated_data = response.json()
    print(translated_data["data"]["translations"][0]["translatedText"][::-1])

trn(input('Enter word: '))
