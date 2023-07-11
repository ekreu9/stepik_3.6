from selenium.webdriver.common.by import By


def test_languages(browser):
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link1)

        # Ищем кнопку
        
        button =browser.find_elements(By.CSS_SELECTOR, "button[type='submit']")

        
        # Проверка наличия кнопки

        assert len(button) > 0, "Кнопка не найдена"

        
