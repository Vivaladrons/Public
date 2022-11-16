import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import new_name, new_surname, new_email, new_password, password_twice, email, phone
from config import invalid_name, invalid_surname, invalid_email, invalid_phone, invalid_password


@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('./chromedriver.exe')
    pytest_driver.get('https://b2c.passport.rt.ru')
    pytest_driver.implicitly_wait(10)
    pytest_driver.find_element(By.ID, 'kc-register').click()
    yield pytest_driver

    pytest_driver.quit()


def test_invalid_name(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'firstName').send_keys(invalid_name)
    pytest_driver.find_element(By.NAME, 'lastName').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_invalid_surname(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'lastName').send_keys(invalid_surname)
    pytest_driver.find_element(By.NAME, 'firstName').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_invalid_email(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'address').send_keys(invalid_email)
    pytest_driver.find_element(By.NAME, 'firstName').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_invalid_phone(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'address').send_keys(invalid_phone)
    pytest_driver.find_element(By.NAME, 'firstName').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_invalid_password(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.ID, 'password').send_keys(invalid_password)
    pytest_driver.find_element(By.NAME, 'firstName').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_password_confirm(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'firstName').send_keys(new_name)
    pytest_driver.find_element(By.NAME, 'lastName').send_keys(new_surname)
    pytest_driver.find_element(By.ID, 'address').send_keys(new_email)
    pytest_driver.find_element(By.ID, 'password').send_keys(new_password)
    pytest_driver.find_element(By.ID, 'password-confirm').send_keys(password_twice)
    pytest_driver.find_element(By.NAME, 'register').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta--error').text != ' '


def test_new_user(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'firstName').send_keys(new_name)
    pytest_driver.find_element(By.NAME, 'lastName').send_keys(new_surname)
    pytest_driver.find_element(By.ID, 'address').send_keys(new_email)
    pytest_driver.find_element(By.ID, 'password').send_keys(new_password)
    pytest_driver.find_element(By.ID, 'password-confirm').send_keys(new_password)
    pytest_driver.find_element(By.NAME, 'register').click()
    assert pytest_driver.current_url.find('account_b2c')


def test_email_already_exist(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'firstName').send_keys(new_name)
    pytest_driver.find_element(By.NAME, 'lastName').send_keys(new_surname)
    pytest_driver.find_element(By.ID, 'address').send_keys(email)
    pytest_driver.find_element(By.ID, 'password').send_keys(new_password)
    pytest_driver.find_element(By.ID, 'password-confirm').send_keys(new_password)
    pytest_driver.find_element(By.NAME, 'register').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.card-modal__title').text == 'Учётная запись уже существует'


def test_phone_already_exist(testing):
    pytest_driver = testing
    pytest_driver.find_element(By.NAME, 'firstName').send_keys(new_name)
    pytest_driver.find_element(By.NAME, 'lastName').send_keys(new_surname)
    pytest_driver.find_element(By.ID, 'address').send_keys(phone)
    pytest_driver.find_element(By.ID, 'password').send_keys(new_password)
    pytest_driver.find_element(By.ID, 'password-confirm').send_keys(new_password)
    pytest_driver.find_element(By.NAME, 'register').click()
    assert pytest_driver.find_element(By.CSS_SELECTOR, '.card-modal__title').text == 'Учётная запись уже существует'
