import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import nums_from_string


driver = webdriver.Chrome()

driver.get('https://www.amazon.ae/')
driver.maximize_window()
driver.implicitly_wait(10)

# webdriver.ActionChains(driver).move_to_element(driver.find_element(By.ID, 'nav-link-accountList')).perform()
# sleep(2)
# driver.find_element(By.XPATH, '//*[@id="nav_prefetch_yourorders"]/span').click()
# sleep(5)

# webdriver.ActionChains(driver).move_to_element(driver.find_element(By.ID, 'nav-link-accountList')).perform()
# sleep(2)
# driver.find_element(By.XPATH, '//*[@id="nav_prefetch_youraddresses"]/span').click()
# sleep(5)

webdriver.ActionChains(driver).move_to_element(driver.find_element(By.ID, 'nav-link-accountList')).perform()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="nav-al-your-account"]/a[4]/span').click()
sleep(5)

https://www.amazon.ae/hz/wishlist/intro






# driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]').click()
# sleep(5)
# driver.find_element(By.XPATH, '//*[@id="slot-15"]/div/div/div[2]/div[3]/div/div[2]').click()
# sleep(5)
# driver.find_element(By.XPATH, '//*[@id="octopus-dlp-asin-stream"]/ul/li[1]').click()
# sleep(5)
# price1 = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]').text
## price2 = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]').text
# print(price1)
## print(nums_from_string.get_nums(price1))
## print(price2)
# Select(driver.find_element(By.ID, 'quantity')).select_by_value('3')
# driver.find_element(By.ID, 'add-to-cart-button').click()
# sleep(3)
# webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# sleep(5)
# driver.find_element(By.ID, 'nav-cart').click()
# sleep(5)
## name = driver.find_element(By.XPATH, '//*[@id="sc-item-C571241e4-aa1c-4ed6-bc90-ee78d01c6a10"]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span[1]/span/span[1]').text
## name = driver.find_element(By.XPATH, '//*[@id="sc-item-C571241e4-aa1c-4ed6-bc90-ee78d01c6a10"]/div[4]/div/div[1]/div/div/div[2]/ul/li[1]/span/a/span[1]/span/span[2]').text
# col = driver.find_element(By.XPATH, '//*[@id="sc-subtotal-label-activecart"]').text
# print(col)
## print(nums_from_string.get_nums(col))
## price = driver.find_element(By.XPATH, '//*[@id="sc-item-C75cc3c92-89de-45f4-b8e5-c8c9d226895f"]/div[4]/div/div[2]/p/span').text
# price = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/p/span').text
# print(price)
## print(nums_from_string.get_nums(price))
# price_all = driver.find_element(By.XPATH, '//*[@id="sc-subtotal-amount-activecart"]/span').text
# print(price_all)
## print(nums_from_string.get_nums(price_all))
# sleep(3)
# print("цена товара за еденицу при заказе")
# print(nums_from_string.get_nums(price1)[0])
# a = nums_from_string.get_nums(price1)
## print(type(a[0]))
## print(a[0])

# print("количество заказаных едениц")
# print(nums_from_string.get_nums(col)[0])
#
#
# print("цена товара за еденицу в корзине")
# print(nums_from_string.get_nums(price)[0])
#
#
# print("общая цена товара")
# print(nums_from_string.get_nums(price_all)[0])
## d = nums_from_string.get_nums(price1)
## result_p_all = [int(item) for item in d]
## print(result_p_all)
# print(a[0]*3)
#
#
# if nums_from_string.get_nums(price1) == nums_from_string.get_nums(price):
#     print("Цена при заказе и в корзине одинаковая")
# else:
#     print(False)
#
# if nums_from_string.get_nums(col)[0] == 3:
#     print("количество заказанных едениц верно")
# else:
#     print(False)
#
# if nums_from_string.get_nums(price1)[0] * nums_from_string.get_nums(col)[0] == nums_from_string.get_nums(price_all)[0]:
#     print("Общая цена == цене за единицу товара * заказаных едениц")
# else:
#     print(False)

