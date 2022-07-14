from 爬蟲 import 登入, 銷貨明細查詢_搜尋條件

判斷頁面元素_xpath = {
    '登入頁': {'登入字樣_xpath': 'xpath1', '帳號匡_xpath': 'xpath2',
             '密碼匡_xpath': 'xpath3'},
    '儀表板': {'公告欄': 'xpath1', '標題': 'xpath2'},
    '銷貨明細查詢_結果': {'銷貨日期': 'xpath1', '門市': 'xpath2','總筆數':'xpath3'},
}
urls = {
    '銷貨明細查詢':'url1',
    '登入頁':'url2',
}
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_登入():
    ''''''
    driver.get(urls['登入頁'])
    # is in 登入頁
    for xpath in 判斷頁面元素_xpath['登入頁'].values():
        print(xpath)
        assert driver.find_element(By.XPATH, xpath)

    登入()

    # is in 儀表板
    for xpath in 判斷頁面元素_xpath['儀表板'].values():
        print(xpath)
        assert driver.find_element(By.XPATH, xpath)


def test_銷貨明細查詢_搜尋條件():
    '''檢查上方的文字是否正確'''
    driver.get(urls["銷貨明細查詢"])
    測試資料_input = {'銷貨日期':'2022/06/27',}
    測試資料_output = {'銷貨日期':'2022/06/27','門市':'全部門市','總筆數':'43'}

    銷貨明細查詢_搜尋條件( **測試資料_input)

    assert driver.find_element(By.XPATH,判斷頁面元素_xpath['銷貨明細查詢_結果']['銷貨日期']).text == 測試資料_output['銷貨日期']
    assert driver.find_element(By.XPATH,判斷頁面元素_xpath['銷貨明細查詢_結果']['門市']).text == 測試資料_output['總筆數']
    assert driver.find_element(By.XPATH,判斷頁面元素_xpath['銷貨明細查詢_結果']['總筆數']).text == 測試資料_output['門市']

