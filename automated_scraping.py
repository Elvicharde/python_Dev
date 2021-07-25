# Automated Scraper
# This code demonstrates the use of Selenium's webdriver in combination with bS4.

# Importing relevant packages
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from time import sleep

# Setting browser options
option = webdriver.chrome.options.Options()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)



urls = ["https://youtube.com", "https://google.com","https://fb.com",\
                                "https://Upwork.com", "https://ymail.com"]

for index, url in enumerate(urls):
    if index == 1:
        driver.get(url)
    else:
        script = f'''window.open("{url}", "_blank")'''
        driver.execute_script(script)
        sleep(1)

browser_tabs = driver.window_handles

for tab in browser_tabs:
    driver.switch_to.window(tab)
    print("Current Tab: ", driver.title)
    sleep(1)

# Closing tabs other than google.com
print("\nChecking if current tab is Google.com!")
print('--------------------------------------------')

for tab in browser_tabs:
    sleep(1)
    driver.switch_to.window(tab)

    if driver.title == "Google":
        g_tab = tab       
    else:
        driver.execute_script("alert('Not Google.com. Closing now')")
        sleep(3)
        driver.switch_to.alert.accept()
        # print("\nNah, this is "+ driver.title +". Closing now!\n")
        sleep(2)
        driver.close()
        
driver.switch_to.window(g_tab)
print('--------------------------------------------')
driver.execute_script('''alert("Now, this is Google. Let us check the price of dollar today!")''')
sleep(3)
driver.switch_to.alert.accept()
sleep(3)
# print("\nNow, this is "+ driver.title +".\nLet us check the price of dollar today!")
search_box, search_button = [driver.find_element_by_xpath(val) for val in \
                            ['/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input',\
                            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]']]\

search_box.send_keys("Dollar to Naira today")
search_button.click()
value = driver.find_element_by_class_name("b1hJbf").text.split("\n")[1]
script = f'''alert("Dollar is now #{value}, as of today.")'''
driver.execute_script(script)
print("\nDollar is now #" + value + ", as of today.")
