url = "https://ria.ru/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("a", class_="cell-main-photo__link")

print("Последние заголовки:")
for h in headlines[:5]:
    print("-", h.text.strip())
