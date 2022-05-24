def test_check_add_to_cart(browser):
    button = browser.find_element_by_class_name("btn-add-to-basket")
    button.click()

    message = browser.find_element_by_class_name("alertinner ")
    assert "Coders at Work" in message.text, "Its not added in cart"


