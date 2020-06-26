from behave import step
from nose.tools import assert_equal, assert_not_equal, assert_true


RETURN_FROM_HOME_PAGE = None


@step('I navigate to the Herolo page')
def step_impl(context):
    context.home_page.navigate('https://automation.herolo.co.il/')


''' ===================    DownSize Form  ============================= '''


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
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_field(id_field=name, text=text, ch_status=True)
    elif flag == 'False':
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_field(id_field=name, text=text, ch_status=False)
    # print(f'{RETURN_FROM_HOME_PAGE} => {name}  +  {text}  +  {flag}')    # for test


@step('I expect that in False "{flag}" case(wrong text for this field) will event error message and True case will not')
def step_impl(context, flag):
    global RETURN_FROM_HOME_PAGE
    if flag:
        assert_true(RETURN_FROM_HOME_PAGE == True)
    else:
        assert_true(RETURN_FROM_HOME_PAGE == False)


''' ==============================  Social links =================================== '''


@step('I click on "{social}" link')
def step_impl(context, social):
    context.home_page.get_social_link(social)


@step('I expect for opening new window with Url "{url}"')
def step_impl(context, url):

    context.home_page.switch_window()
    assert_equal(str(context.home_page.get_current_url()).lower().split("/")[:3], str(url).lower().split("/")[:3])
    print(f'{context.home_page.get_current_url()} : {url}')


''' ============================= Scroll Button =============================================== '''


@step('I scroll "{down}" and wait 1 sec')
def step_impl(context, down):
    context.home_page.set_scroll_position(down)


@step('I search and after click on scroll button')
def step_impl(context):
    scroll = context.home_page.find_element_by_css_selector('a[data-scroll="true"]')
    scroll.click()


@step('I expect scroll from "{down}" to Top')
def step_impl(context, down):
    if context.home_page.SCROLL == down:
        assert_equal(context.home_page.get_scroll_position(), 0)
    else:
        assert_not_equal(True, False)


''' ============================= Mail link =============================================== '''


@step("I search for a Mail link")
def step_impl(context):
    global RETURN_FROM_HOME_PAGE
    RETURN_FROM_HOME_PAGE = context.home_page.find_element_by_partial_link_text('@herolo')


@step("I expect that link is valid (start with mailto:)")
def step_impl(context):
    print(RETURN_FROM_HOME_PAGE.get_attribute('href'))
    assert_true(str(RETURN_FROM_HOME_PAGE.get_attribute('href')).startswith('mailto:'))


''' ============================= Footer Form =============================================== '''


@step('I fill the footer form fields "{field_name}" with "" I expect to see error massage')
def step_impl(context, field_name):
    assert_true(context.home_page.err_msg_empty_field_footer(field_name))


@step('I fill the footer form field "{name}" with "{text}" and "{flag}" of Case')
def step_impl(context, name, text, flag):
    global RETURN_FROM_HOME_PAGE
    if flag == 'True':
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_field_footer(id_field=name, text=text, ch_status=True)
    elif flag == 'False':
        RETURN_FROM_HOME_PAGE = context.home_page.err_msg_fill_field_footer(id_field=name, text=text, ch_status=False)
    # print(f'{RETURN_FROM_HOME_PAGE} => {name}  +  {text}  +  {flag}')    # for test