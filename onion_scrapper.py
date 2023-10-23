# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests
from icecream import ic

from datetime import date
URL = "https://www.theonion.com/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
first_return = soup.find(name="article")
ic(first_return.attrs)
ic(first_return.contents)
ic(type(first_return.findChildren))
ic(first_return.findChildren)
for values in first_return.find_all():
    ic(values)


today = date.today()
d4 = today.strftime("%b-%d-%Y")
articles_found = soup.find_all(name="article")
f = open("onionScrapping_"+d4+".html", "w")
ic(soup.find_all(name="style"))
f.write(str(soup.find_all(name="style")))
f.write("<p>"+d4+"</p>")
f.write("<hr>")
for articles in articles_found:
    f.write(str(articles).replace("<picture", "<picture style=\"width:100px\""))
    f.write("<hr>")

f.close()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
