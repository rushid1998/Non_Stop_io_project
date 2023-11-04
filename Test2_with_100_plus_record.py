import requests
from bs4 import BeautifulSoup
import csv


def get_sport_headlines_2(sport_name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='container__text container_grid-4__text')

    headlines_2 = []

    for result in results:
        headline = result.find('span', class_='container__headline-text')
        headlines_2.append({"Sport Name": sport_name, "Headline": headline.text})

    return headlines_2



def get_sport_headlines_1(sport_name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='container__text container_vertical-strip__text')

    headlines_1 = []

    for result in results:
        headline = result.find('span', class_='container__headline-text')
        headlines_1.append({"Sport Name": sport_name, "Headline": headline.text})

    return headlines_1


def get_sport_headlines(sport_name, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='container__text container_lead-plus-headlines-with-images__text')

    headlines = []

    for result in results:
        headline = result.find('span', 'container__headline-text')
        headlines.append({"Sport Name": sport_name, "Headline": headline.text})

    return headlines


sports = {
    "Golf": "https://edition.cnn.com/sport/golf",
    "Football": "https://edition.cnn.com/sport/football",
    "Tennis": "https://edition.cnn.com/sport/tennis",
    "motorsport":"https://edition.cnn.com/sport/motorsport",
    "Olympics": "https://edition.cnn.com/sport/olympics",
    "Climbing": "https://edition.cnn.com/sport/climbing",
    "US Sports": "https://edition.cnn.com/sport/us-sports"
}

all_headlines = []


for sport, url in sports.items():
    headlines = get_sport_headlines(sport, url)
    all_headlines.extend(headlines)
    


for sport, url in sports.items():
    headlines_1 = get_sport_headlines_1(sport, url)
    all_headlines.extend(headlines_1)


for sport, url in sports.items():
    headlines_2 = get_sport_headlines_2(sport, url)
    all_headlines.extend(headlines_2)
    

csv_file = "sports_headlines_2.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Sport Name", "Headline"])
    writer.writeheader()
    writer.writerows(all_headlines)

print(f"Data written to {csv_file}")
