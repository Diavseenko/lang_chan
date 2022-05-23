def test_check_add_to_cart(browser):
    button = browser.find_element_by_class_name("btn-add-to-basket")
    button.click()

    message = browser.find_element_by_class_name("alertinner ")
    assert message.text == "Coders at Work has been added to your basket.", "Its not added in cart"


