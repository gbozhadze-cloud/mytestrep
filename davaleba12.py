# ------------------------ ვებ-გვერდის ავტომატიზაცია ------------------------
#
# თქვენი მიზანია გააკეთოთ ვებ-გვერდის ავტომატიზაცია დრაივერის გამოყენებით:
#
# მისამართი: https://www.saucedemo.com/
#
# დავალება:
#
# 1. უნდა სცადოთ locked_out_user-ით ავტორიზაცია, ასევე უნდა დაიჭიროთ შეტყობინება რომელსაც დააბრუნებს გვერდი, ან გაივლის ავტორიზაციას.
#
# 2. უნდა სცადოთ performance_glitch_user-ით ავტორიზაცია, თუ გაივლით ავტორიზაციას უნდა გააკეთოთ logout, ან დაიჭიროთ error შეტყობინება
#
# 3. უნდა სცადოთ problem_user-ით ავტორიზაცია, თუ ვერ გაივლით ვიჭერთ error-ს, გავლის შემთხვევაში უნდა დაამატოთ 2 ნივთი კალათაში და შემდეგ წაშალოთ ან დავიჭიროთ error (logout)
#
# 4. უნდა სცადოთ standard_user-ით ავტორიზაცია, თუ ვერ გაივლით ვიჭერთ error-ს, გავლის შემთხვევაში უნდა დაამატოთ 2 ნივთი კალათაში და 5
# წამის შემდეგ უნდა წაშალოთ ერთ-ერთი კალათიდან, ასევე უნდა შეხვიდეთ რომელიმე პროდუქტზე და 5 წამის შემდეგ დაბრუნდეთ მთავარ გვერდზე (back)-ით.
# გამოიყენოთ სორტირება და ფასები დაალაგოთ High to Low, ბოლოს უნდა შეამოწმოთ footer-ის ნაწილი - გავაკეთოთ კლიკი ფეისბუქის icon-ზე დავბრუნდეთ
# ისევ ვებ-გვერდზე და შემდეგ გავაკეთოთ კლიკი linkedin-ის icon-ზე და ისევ დავბრუნდეთ საიტზე, ამის შემდეგ გავაკეთოთ logout.
#
# აუცილებლად გამოიყენეთ unittest მოდული, ასევე გამოიყენეთ TestCase კლასი და ტესტები გაუშვით ფუნქციებად შინაარსობრივად უნდა გქონდეს მინიმუმ 4 ფუნქცია.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

def test_locked_out_user():
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")
    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(2)
    check_text = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
    assert check_text.text == "Epic sadface: Sorry, this user has been locked out."

# test_locked_out_user()

def test_performance_glitch_user():
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("performance_glitch_user")
    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(2)
    (driver.find_element(By.ID, "react-burger-menu-btn")).click()
    time.sleep(1)
    logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
    logout_btn.click()

#test_locked_out_user()
    #check_text = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
    #assert check_text.text == "Epic sadface: Sorry, this user has been locked out."

def test_problem_user():
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("problem_user")
    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(5)
    add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart.click()
    time.sleep(2)
    add_to_cart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add_to_cart2.click()
    time.sleep(2)
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    (driver.find_element(By.ID, "remove-sauce-labs-backpack")).click()
    time.sleep(1)
    (driver.find_element(By.ID, "remove-sauce-labs-bike-light")).click()
    time.sleep(3)
    (driver.find_element(By.ID, "react-burger-menu-btn")).click()
    time.sleep(1)
    logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
    logout_btn.click()

#test_problem_user()

def test_standard_user ():
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("problem_user")
    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(5)
    add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart.click()
    time.sleep(2)
    add_to_cart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    add_to_cart2.click()
    time.sleep(2)
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    (driver.find_element(By.ID, "remove-sauce-labs-backpack")).click()
    time.sleep(1)
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(1)
    driver.get("https://www.saucedemo.com/inventory-item.html?id=4")
    time.sleep(5)
    driver.back()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-test="social-facebook"]').click()
    time.sleep(8)
    driver.get("https://www.saucedemo.com/inventory.html")
    driver.find_element(By.CSS_SELECTOR, '[data-test="social-linkedin"]').click()
    (driver.find_element(By.ID, "react-burger-menu-btn")).click()
    time.sleep(3)
    logout_btn = driver.find_element(By.ID, "logout_sidebar_link")
    logout_btn.click()
    time.sleep(3)

test_standard_user()