from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse
import time

TIME_TO_LOAD_PAGE = 5


def open_dataset_page(url: str):
    driver.get(url)
    time.sleep(TIME_TO_LOAD_PAGE)
    try:
        entry_list = driver.find_element_by_class_name("entryList")
    except:
        return

    entries = entry_list.find_elements_by_class_name("entryListRow")
    if len(entries) == 0:
        return

    for entry in entries:
        try:
            distro_format = entry.find_element_by_class_name("esbRowAlignPrimary")
        except:
            return

        try:
            distro_link = entry.find_element_by_class_name('distribution__link')
        except:
            return

        print(distro_link.get_attribute('href'))

        try:
            data_format = distro_format.get_attribute('innerHTML')
        except:
            return

        if data_format not in ['API','geojson','shp','csv','json']:
            return
        
        with open(f"{data_format}.txt", "a") as myfile:
            myfile.write(distro_link.get_attribute('href') + '\n')
        
    

# Change driver path to your chromedriver.exe
DRIVER_PATH = 'C:/Users/LaptopE14/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
print('\n\n\n\n')

time.sleep(10)

for page_number in range(1,374):
    driver.get(f'https://www.dataportal.se/sv/datasets/?p={page_number}&q=&s=2&t=20&f=&rt=dataset%24esterms_IndependentDataService%24esterms_ServedByDataService&c=false')
    time.sleep(TIME_TO_LOAD_PAGE)   # To catch up loading the website
    search_results_li = driver.find_elements_by_class_name('search-result-list-item')
    search_results_length = len(search_results_li)

    for i in range(search_results_length):
        search_results_li = driver.find_elements_by_class_name('search-result-list-item')

        search_result_link = search_results_li[i].find_element_by_tag_name('a')

        dataset_link = search_result_link.get_attribute('href')
        
        open_dataset_page(dataset_link)
        driver.get(f'https://www.dataportal.se/sv/datasets/?p={page_number}&q=&s=2&t=100&f=&rt=esterms_IndependentDataService%24esterms_ServedByDataService&c=true')
        time.sleep(TIME_TO_LOAD_PAGE)