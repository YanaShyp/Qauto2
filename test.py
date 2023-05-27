import requests
from driver import Driver
from Qauto2.pages.login_page import LoginPage
from Qauto2.models.create_new_car_model import CreateNewCar
from Qauto2.models.register_post_model import RegisterPostModel
from Qauto2.models.login_post_model import UserLogin

class TestCars:

    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.session = requests.session()
        self.login_page = LoginPage()

    def test_car(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        register_user = RegisterPostModel("Yana", "Shyp", "yanatestCarss@gmail.com", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)
        login_user = UserLogin("yanatestCarss@gmail.com", "Qwerty123", "False")
        self.session.post("https://qauto2.forstudy.space/api/auth/signin", json=login_user.__dict__)
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("yanatestCarss@gmail.com")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_button().click()
        create_new_car = CreateNewCar("Audi", "TT", "11")
        self.session.post("https://qauto2.forstudy.space/api/cars", json=create_new_car.__dict__)

    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")

