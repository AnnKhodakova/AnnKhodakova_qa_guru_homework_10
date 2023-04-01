from selene import command
from selene.support.shared import browser
from model.pages.registration_page import RegistrationPage

browser.config.click_by_js = True


def test_registration_page():
    registration_page = RegistrationPage()
    # OPEN PAGE
    registration_page.open()

    # WHEN
    registration_page.type_first_name('Bob')
    registration_page.type_last_name('By')
    registration_page.type_email('email@email.email')
    registration_page.choose_gender('Male')
    registration_page.type_number('1234567890')
    registration_page.type_date_of_birth('March', '2002', '27')
    registration_page.type_subjects('physics')
    browser.element('[for="hobbies-checkbox-2"]').click()
    registration_page.picture_path('/picture/VYqbjvKLSlU.jpg')
    registration_page.type_address('address')
    registration_page.choose_state_and_city('Haryana', 'Karnal')
    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Bob By',
        'email@email.email',
        'Male',
        '1234567890',
        '27 March,2002',
        'Physics',
        'Reading',
        'VYqbjvKLSlU.jpg',
        'address',
        'Haryana Karnal'
    )
    browser.element('#closeLargeModal').click()
