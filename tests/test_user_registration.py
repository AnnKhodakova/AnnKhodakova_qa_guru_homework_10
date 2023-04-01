from model.pages.registration_page import RegistrationPage
from data.users import User

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


def test_registration_page():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.user_registration(user)
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
