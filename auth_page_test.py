import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import email, password, phone


@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('./chromedriver.exe')
    pytest_driver.get('https://b2c.passport.rt.ru')
    pytest_driver.implicitly_wait(10)
    yield pytest_driver

    pytest_driver.quit()


def test_login_phone(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'username').send_keys(phone)
    pytest_driver.find_element(By.ID, 'password').send_keys(password)
    pytest_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest_driver.implicitly_wait(10)
    assert pytest_driver.current_url.find('account_b2c')


def test_login_email(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'username').send_keys(email)
    pytest_driver.find_element(By.ID, 'password').send_keys(password)
    pytest_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest_driver.implicitly_wait(10)
    assert pytest_driver.current_url.find('account_b2c')


def test_redirect_user_agreement(testing):
    pytest_driver = testing
    agreement_url = pytest_driver.find_element(By.XPATH, '\
                                    //*[@id="rt-footer-agreement-link"]').get_attribute('href')
    assert agreement_url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


def test_redirect_confidential_politics(testing):
    pytest_driver = testing
    confidential_url = pytest_driver.find_element(By.XPATH, '\
                                    //*[@id="rt-footer-agreement-link"]').get_attribute('href')
    assert confidential_url != 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


def test_forgot_password(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'forgot_password').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.card-container__title').text == 'Восстановление пароля'


def test_return_to_auth_page(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'forgot_password').click()
    pytest_driver.find_element(By.ID, 'reset-back').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.card-container__title').text == 'Авторизация'


def test_cookie_information(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.CSS_SELECTOR, '.rt-footer-left__cookies-tip-container').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-tooltip__title').text == 'Мы используем Cookie'
