from selene import have, command
from selene.support.shared import browser


def test_practice_form(browser_config):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Tester')
    browser.element('#lastName').type('Testov')

    gender_group = browser.element('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
