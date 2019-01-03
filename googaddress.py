import webbrowser,sys 
from bs4 import BeautifulSoup
ggl = ('https://www.google.com/maps/place/')
address = input("Address   ")
wbpg = ggl + address 
webbrowser.open(wbpg)
