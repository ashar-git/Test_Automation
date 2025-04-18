import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver =  webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row_cnt = len(row_elements)
    # print(row_cnt)
    col_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col_cnt = len(col_elements)
    # print(col_cnt)
    # time.sleep(10)

    # // table[contains( @ id, 'cust')] / tbody / tr[ -- FP
    # 2 - i(2,7)
    # ] / td[   -- sp
    # 3 - j(1,3)
    # ]  -- 3p

    #creating dynamic xpath
    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"
    for i in range(2,row_cnt+1):
        for j in range(1,col_cnt+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH,country_path)
                print(f"Helen Bennet belongs to {country_text.text}")


#Find web table elements using tr and td
def test_find_web_table_element_using_tr_td():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    #Get the table
    table =  driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    table_rows = table.find_elements(By.TAG_NAME,"tr")
    for row in table_rows:
        col = row.find_elements(By.TAG_NAME,"td")
        for c in col:
            print(c.text)