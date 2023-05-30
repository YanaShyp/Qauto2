import requests
from driver import Driver
from Qauto2.pages.login_page import LoginPage
from Qauto2.models.create_new_car_model import CreateNewCar
from Qauto2.models.register_post_model import RegisterPostModel
from Qauto2.models.login_post_model import UserLogin
from Qauto2.pages.garage_page import GaragePage

class TestCars:

    def setup_class (self):
        self.driver = Driver.get_chrome_driver()
        self.session = requests.session()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        register_user = RegisterPostModel("Yana", "Shyp", "yanatestCars@gmail.com", "Qwerty123", "Qwerty123")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user.__dict__)
        login_user = UserLogin("yanatestCars@gmail.com", "Qwerty123", "False")
        self.session.post("https://qauto2.forstudy.space/api/auth/signin", json=login_user.__dict__)
        create_new_car = CreateNewCar("1", "1", 100)
        self.session.post("https://qauto2.forstudy.space/api/cars", json=create_new_car.__dict__)

    def setup_method(self):
        self.driver.implicitly_wait(5)

    def test_user_login(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("yanatestCars@gmail.com")
        self.login_page.get_password_field().fill_field("Qwerty123")
        self.login_page.get_login_button().click()

    def test_edit_car(self):
         self.garage_page.get_edit_button().click()
         self.garage_page.get_mileage_field().click()
         self.garage_page.get_mileage_field().fill_field("10")
         self.garage_page.get_save_button().click()

    def test_delete_car(self):
        self.garage_page.get_edit_button().click()
        self.garage_page.get_remove_car_button().click()
        self.garage_page.get_remove_danger_car_button().click()


    def teardown_class(self):
        self.session.delete("https://qauto2.forstudy.space/api/users")


