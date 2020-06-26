from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.keys import Keys
import time

# class HomePageLocator(object):
#     # Home Page Locators
#
#     HEADER_TEXT = (By.XPATH, "//h1")
#     SEARCH_FIELD = (By.ID, "term")
#     SUBMIT_BUTTON = (By.ID, "submit")


class HomePage(Browser):
    # Home Page Actions

    # def fill(self, text, *locator):
    #     self.driver.find_element(*locator).send_keys(text)

    # def click_element(self, *locator):
    #     self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    # def search(self, search_term):
    #     self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
    #     self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def form_section_inputs(self, name, company, email, telephone):
        if name == 'null':
            name = ""
        if company == 'null':
            company = ""
        if email == 'null':
            email = ""
        if telephone == 'null':
            telephone = ""
        form = self.driver.find_element_by_id('section-inputs')
        submit = form.find_element_by_css_selector('a[type="button"]')

        name_field = form.find_element_by_id('name')
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys(name)

        company_field = form.find_element_by_id('company')
        company_field.send_keys(Keys.CONTROL + "a")
        company_field.send_keys(Keys.DELETE)
        company_field.send_keys(company)

        email_field = form.find_element_by_id('email')
        email_field.send_keys(Keys.CONTROL + "a")
        email_field.send_keys(Keys.DELETE)
        email_field.send_keys(email)

        phone_field = form.find_element_by_id('telephone')
        phone_field.send_keys(Keys.CONTROL + "a")
        phone_field.send_keys(Keys.DELETE)
        phone_field.send_keys(telephone)

        submit.click()
        time.sleep(0.5)

    def err_msg_empty_field(self, id_field):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}

        form = self.driver.find_element_by_id('section-inputs')
        input_name = form.find_element_by_id(id_field)
        input_name.click()
        form.click()
        time.sleep(0.5)
        span = form.find_element_by_css_selector(error_msg[id_field])
        return 'הוא שדה חובה' in span.text

    def err_msg_fill_feild(self, id_field, text, ch_status):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}

        form = self.driver.find_element_by_id('section-inputs')
        input_name = form.find_element_by_id(id_field)

        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(text)
        form.click()
        time.sleep(0.5)
        span = form.find_element_by_css_selector(error_msg[id_field])
        print(f' strat{span.text}end')
        if ch_status:
            return span.text == ''
        return 'לא חוקי' in span.text

    def err_msg_fill_feild(self, id_field, text, ch_status):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}

        form = self.driver.find_element_by_id('section-inputs')
        input_name = form.find_element_by_id(id_field)

        time.sleep(0.5)
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(text)
        form.click()
        span = form.find_element_by_css_selector(error_msg[id_field])
        print(f' strat{span.text}end')
        if ch_status:
            return span.text == ''
        return 'לא חוקי' in span.text