from model.pages.registration_page import RegistrationPage
from data.users import User
import allure

user = User('Bob', 'By',
            'email@email.email',
            'Male',
            '1234567890',
            'March', '2002', '27',
            'Physics',
            'Reading',
            'VYqbjvKLSlU.jpg',
            'address',
            'Haryana', 'Karnal')


@allure.title("Registration page")
def test_registration_page(setup_browser):
    registration_page = RegistrationPage(setup_browser)
    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.user_registration(user)
    with allure.step("Form results"):
        registration_page.should_registered_user_with('Bob By',
                                                      'email@email.email',
                                                      'Male',
                                                      '1234567890',
                                                      '27 April,2023',
                                                      'Physics',
                                                      'Reading',
                                                      'VYqbjvKLSlU.jpg',
                                                      'address',
                                                      'Haryana Karnal')
