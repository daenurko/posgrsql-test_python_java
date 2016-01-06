from lxml.html import parse
# Получаем страничку
page = parse('http://habrahabr.ru/').getroot()
# Ищем все теги <a> с css классом topic
hrefs = page.cssselect("a.topic")
for row in hrefs:
    # Получаем атрибут href
    print row.get("href")