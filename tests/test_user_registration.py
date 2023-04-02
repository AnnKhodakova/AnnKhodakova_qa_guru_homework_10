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
            '/picture/VYqbjvKLSlU.jpg',
            'address',
            'Haryana', 'Karnal')


@allure.title("Registration page")
def test_registration_page():
    registration_page = RegistrationPage()
    with allure.step("Open registrations form"):
        registration_page.open()
    with allure.step("Fill form"):
        registration_page.user_registration(user)
    with allure.step("Form results"):
        registration_page.should_registered_user_with('Bob By',
                                                      'email@email.email',
                                                      'Male',
                                                      '1234567890',
                                                      '27 March,2002',
                                                      'Physics',
                                                      'Reading',
                                                      'VYqbjvKLSlU.jpg',
                                                      'address',
                                                      'Haryana Karnal')


