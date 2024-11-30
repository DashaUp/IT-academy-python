import requests

def getNames(url):
    response = requests.get(url)
    page_text = response.text
    parse_page_text = page_text.split('<h3>')

    for parse_elem_1 in parse_page_text:
        if not (parse_elem_1.startswith('<a')):
            continue
        parse_elem_2 = parse_elem_1.split('"')
        print(parse_elem_2[3])
    return response.status_code

getNames('https://books.toscrape.com/')

page=2
while(getNames(f"https://books.toscrape.com/catalogue/page-{page}.html")):
    page += 1
