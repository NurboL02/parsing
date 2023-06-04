from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def parse_akipress(request):
    url = 'https://www.akipress.kg/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_titles = soup.find_all('h3', class_='news_title')
    titles = [title.text for title in news_titles]

    context = {'titles': titles}
    return render(request, 'parser_app/akipress.html', context)
