from urllib.request import FancyURLopener
from bs4 import BeautifulSoup
class AppURLopener(FancyURLopener):
	version = "Mozilla/5.0"

default_agent = FancyURLopener().version
changed_agent = AppURLopener().version
print(default_agent,"->",changed_agent)
url = "http://fd.postech.ac.kr/bbs/today_menu.php?bo_table=weekly&ckattempt=1"
html = AppURLopener().open(url)
result = BeautifulSoup(html, 'html.parser')
print(result)