
from browser import Browser
from selenium.webdriver.common.keys import Keys
import time


class HomePage(Browser):

    SCROLL = 0

    def set_scroll_position(self, position):
        try:
            self.driver.execute_script(f"window.scrollTo(0,{position})")

            time.sleep(1)
            global SCROLL
            SCROLL = self.get_scroll_position()
        except Exception as e:
            raise ValueError(e)

    def get_scroll_position(self):
        try:
            return self.driver.execute_script('return window.pageYOffset;')
        except Exception as e:
            raise ValueError(e)

    def navigate(self, address):
        try:
            self.driver.get(address)
        except Exception as e:
            raise ValueError(e)

    def get_page_title(self):
        try:
            return self.driver.title
        except Exception as e:
            raise ValueError(e)

    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            raise ValueError(e)

    def get_social_link(self, name):
        soc_dict = {
            'Facebook': 'https://www.facebook.com/Herolofrontend',
            'Linkedin': 'https://www.linkedin.com/company/herolo/',
            'WhatsApp': 'https://api.whatsapp.com/send?phone=972544945333',
            'WebSite': 'https://herolo.co.il/?lang=he'
        }
        try:
            if 'WhatsApp' not in name:
                social = self.driver.find_element_by_css_selector(f'a[href = "{soc_dict[name]}"]')
            else:
                whats_apps = self.driver.find_elements_by_css_selector(f'a[href = "{soc_dict[name[:-1]]}"]')
                if name.endswith("1"):
                    social = [whats_app for whats_app in whats_apps
                              if str(whats_app.get_attribute('class')).startswith('callUsWhatsapp')][0]

                else:
                    social = [whats_app for whats_app in whats_apps
                              if str(whats_app.get_attribute('class')).startswith('socialMediaBar')][0]

            social.click()
        except Exception as e:
            raise ValueError(e)

    def switch_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except Exception as e:
            raise ValueError(e)

    def form_section_inputs(self, name, company, email, telephone):
        if name == 'null':
            name = ""
        if company == 'null':
            company = ""
        if email == 'null':
            email = ""
        if telephone == 'null':
            telephone = ""
        try:
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
        except Exception as e:
            raise ValueError(e)

    def err_msg_empty_field(self, id_field):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}
        try:
            form = self.driver.find_element_by_id('section-inputs')
            input_name = form.find_element_by_id(id_field)
            input_name.click()
            form.click()
            time.sleep(0.5)
            span = form.find_element_by_css_selector(error_msg[id_field])
            return 'הוא שדה חובה' in span.text
        except Exception as e:
            raise ValueError(e)

    def err_msg_fill_feild(self, id_field, text, ch_status):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}
        try:
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
        except Exception as e:
            raise ValueError(e)

    def err_msg_fill_field(self, id_field, text, ch_status):
        error_msg = {
            "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
            "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
            "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
            "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}
        try:
            form = self.driver.find_element_by_id('section-inputs')
            input_name = form.find_element_by_id(id_field)

            time.sleep(0.5)
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(text)
            form.click()
            span = form.find_element_by_css_selector(error_msg[id_field])
            print(f' start{span.text}end')
            if ch_status:
                return span.text == ''
            return 'לא חוקי' in span.text
        except Exception as e:
            raise ValueError(e)

    def find_element_by_css_selector(self, selector):
        try:
            return self.driver.find_element_by_css_selector(selector)
        except Exception as e:
            raise ValueError(e)
