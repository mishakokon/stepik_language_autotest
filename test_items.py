import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert basket_button is not None, "no 'add to basket' button"
