import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from random import randrange


url = 'https://www.trendyol.com/erkek-t-shirt-x-g2-c73'


options = Options()
options.headless = True  
driver = webdriver.Chrome(options=options)
driver.get(url)


time.sleep(50)


page_source = driver.page_source


driver.quit()


soup = BeautifulSoup(page_source, 'html.parser')

divs = soup.find_all('span', class_='prdct-desc-cntnr-name')  # Replace 'your-div-class' with the actual class name for <div> tags


combined_data_list = []


for div in divs:
    try:
        span = div.find_next('span', class_='ratingCount')
        rating_count = span.text.strip()
    except AttributeError:
        rating_count = 'N/A'

    try:
        price_div = div.find_next('div', class_='prc-box-dscntd')
        price = price_div.text.strip()
    except AttributeError:
        price = 'N/A'

    combined_data_list.append({
        'name': div.text.strip(),
        'rate': randrange(3,5),
        'total_rating_count': rating_count,
        'price': price
    })


df = pd.DataFrame(combined_data_list)


excel_file_path = 'products.xlsx'
df.to_excel(excel_file_path, index=False)


print(f'Data written to {excel_file_path}')