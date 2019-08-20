from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

def get_html(url):
    r = requests.get(url)
    return r.text

result_txt = get_html('https://news.ycombinator.com/')
soup = BeautifulSoup(result_txt, 'lxml')

print(soup.prettify())
a = soup.prettify()
def get_data(request):
    return HttpResponse(a)
