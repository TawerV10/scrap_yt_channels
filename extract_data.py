from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

keyword = ''

try:
    options = webdriver.ChromeOptions()

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    with open(f'{keyword}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'name', 'activity', 'videos', 'subscribers', 'link'
        ])

    url = f'https://www.youtube.com/results?search_query={keyword}&sp=EgIQAg%253D%253D'
    driver.get(url)

    count = 1
    channel_lst = driver.find_elements(By.XPATH, "//div[@id='content-section']/div[@id='info-section']/a")

    for channel in channel_lst:
        name = channel.find_element(By.XPATH, "div[@id='info']/ytd-channel-name[@id='channel-title']").text
        link = channel.get_attribute('href')
        subscribers = channel.find_element(By.XPATH, "div[@id='info']/div[@id='metadata']/span[@id='subscribers']").text
        videos = channel.find_element(By.XPATH, "div[@id='info']/div[@id='metadata']/span[@id='video-count']").text

        with open(f'{keyword}.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                name,
                keyword,
                videos.replace('videos', '').replace('video', '').strip(),
                subscribers.replace('subscribers', '').replace('subscriber', '').strip(),
                link
            ])

        print(f'{count}. {name}')
        count += 1

except Exception as ex:
    print(ex)
finally:
    driver.stop_client()
    driver.close()
    driver.quit()