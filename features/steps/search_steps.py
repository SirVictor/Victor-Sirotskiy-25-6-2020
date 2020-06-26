from behave import step
from nose.tools import assert_equal, assert_not_equal, assert_true
from selenium.webdriver.common.by import By


@step('I navigate to the Herolo page')
def step_impl(context):
    context.home_page.navigate('https://automation.herolo.co.il/')


@step('I expect page title to equal "{page_title}"')
def step_impl(context, page_title):
    assert_equal(context.home_page.get_page_title(), page_title)


@step('I fill the form fields "{name}", "{company}", "{email}" and "{phone}"')
def step_impl(context, name, company, email, phone):
    context.home_page.form_section_inputs(name, company, email, phone)


@step('I expect to be redirected to the thank you page: "{flag}"')
def step_impl(context, flag):
    if flag == "True":
        assert_equal(context.home_page.get_current_url(), 'https://automation.herolo.co.il/thank-you/', msg='Positive Case')
    else:
        assert_not_equal(context.home_page.get_current_url(), 'https://automation.herolo.co.il/thank-you/', msg="Nagative Case")
