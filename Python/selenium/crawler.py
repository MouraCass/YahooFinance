from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Opens chrome Browser
driver = webdriver.Chrome(options=chrome_options)

time_period_selector_xpath = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div'
start_date_input_xpath = '//*[@id="dropdown-menu"]/div/div[1]/input'
end_date_input_xpath = '//*[@id="dropdown-menu"]/div/div[2]/input'
done_button_xpath = '//*[@id="dropdown-menu"]/div/div[3]/button[1]'
apply_button_xpath  = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button'
csv_download_xpath = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a'

# Open Yahoo BTC-EUR history page
driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')

# Selecion
time_period_selector = driver.find_element_by_xpath(time_period_selector_xpath)
time_period_selector.click()

start_date_input = driver.find_element_by_xpath(start_date_input_xpath)
start_date_input.click()
start_date_input.clear()
start_date_input.send_keys("01/20/2022")

end_date_input = driver.find_element_by_xpath(end_date_input_xpath) 
end_date_input.click()
end_date_input.clear()
end_date_input.send_keys("01/29/2022")

done_button = driver.find_element_by_xpath(done_button_xpath)
done_button.click()

apply_button = driver.find_element_by_xpath(apply_button_xpath)
apply_button.click()

csv_download = driver.find_element_by_xpath(csv_download_xpath)
csv_download.click()



print("stop here!")
