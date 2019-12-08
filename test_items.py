import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_button_addtobasket(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    buttton = len(browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert buttton > 0 , 'Кнопки добавки товара в корзину нет!'

#pytest --language=ru test_items.py