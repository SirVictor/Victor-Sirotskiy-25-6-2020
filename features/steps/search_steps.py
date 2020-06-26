from behave import step
from nose.tools import assert_equal, assert_not_equal, assert_true
from selenium.webdriver.common.by import By

RETURN_FROM_HOME_PAGE = None


@step('I navigate to the Herolo page')
def step_impl(context):
    context.home_page.navigate('https://automation.herolo.co.il/')


''' ===================    DownSize Form  ============================='''


@step('I expect page title to equal "{page_title}"')
def step_impl(context, page_title):
    assert_equal(context.home_page.get_page_title(), page_title)


@step('I fill the form fields "{name}", "{company}", "{email}" and "{phone}"')
def step_impl(context, name, company, email, phone):
    context.home_page.form_section_inputs(name, company, email, phone)


@step('I expect to be redirected to the thank you page: "{flag}"')
def step_impl(context, flag):
    if flag == "True":
        assert_equal(context.home_page.get_current_url(), 'https://automation.herolo.co.il/thank-you/',
                     msg='Positive Case')
    else:
        assert_not_equal(context.home_page.get_current_url(), 'https://automation.herolo.co.il/thank-you/',
                         msg="Nagative Case")


@step('I fill the form fields "{field_name}" with "" I expect to see error massage')
def step_impl(context, field_name):
    assert_true(context.home_page.err_msg_empty_field(field_name))


@step('I fill the form field "{name}" with "{text}" and "{flag}" of Case')
def step_impl(context, name, text, flag):
    global RETURN_FROM_HOME_PAGE
    if flag == 'True':
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_feild(id_field=name, text=text, ch_status=True)
    elif flag == 'False':
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_feild(id_field=name, text=text, ch_status=False)
    # print(f'{RETURN_FROM_HOME_PAGE} => {name}  +  {text}  +  {flag}')    # for test


@step('I expect that in False "{flag}" case(wrong text for this field) will event error message and True case will not')
def step_impl(context, flag):
    global RETURN_FROM_HOME_PAGE
    if flag:
        assert_true(RETURN_FROM_HOME_PAGE == True)
    else:
        assert_true(RETURN_FROM_HOME_PAGE == False)


