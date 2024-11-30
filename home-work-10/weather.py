import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def getTemperature():
    response = requests.get('https://meteofor.com.ua/weather-poznan-3194/', headers=headers)
    page_text = response.text
    parse_page_text = page_text.split ( '<temperature-value' )
    parse_page_text_1 = parse_page_text[1].split('"')
    temp = parse_page_text_1[1]
    return int(temp)