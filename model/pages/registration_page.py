
from helpers import path
from selene import be, have, command
from data.users import User


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')
        self.browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def type_first_name(self, value):
        self.browser.element('#firstName').should(be.blank).type(value)
        return self

    def type_last_name(self, value):
        self.browser.element('#lastName').should(be.blank).type(value)
        return self

    def type_email(self, value):
        self.browser.element('#userEmail').should(be.blank).type(value)
        return self

    def choose_gender(self, value):
        self.browser.element('[for="gender-radio-1"]').should(have.text(value)).click()
        return self

    def type_number(self, value):
        self.browser.element('#userNumber').should(be.blank).type(value)
        return self

    def type_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').type(month)
        self.browser.element('.react-datepicker__year-select').type(year)
        self.browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def type_subjects(self, value):
        self.browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def choose_hobbies(self, value):
        self.browser.element('[for="hobbies-checkbox-2"]').should(have.text(value)).click()
        return self

    def upload_picture(self, file_name):
        self.browser.element('#uploadPicture').set_value(path(file_name))
        return self

    def type_address(self, value):
        self.browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def choose_state_and_city(self, state, city):
        self.browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()
        self.browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()
        return self

    def click_submit(self):
        self.browser.element('#submit').perform(command.js.click)
        return self

    def should_registered_user_with(self, full_name, email, gender, number,
                                    date_of_birth, subjects, hobbies, foto, address, state_and_city):
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(full_name, email, gender, number,
                             date_of_birth, subjects, hobbies, foto, address, state_and_city))
        return self

    def user_registration(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.choose_gender(user.gender)
        self.type_number(user.number)
        self.type_date_of_birth(user.month_of_birth, user.year_of_birth, user.day_of_birth)
        self.type_subjects(user.subjects)
        self.choose_hobbies(user.hobbies)
        self.upload_picture(user.picture)
        self.type_address(user.address)
        self.choose_state_and_city(user.state, user.city)
        self.click_submit()
        return self
