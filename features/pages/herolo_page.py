
from browser import Browser
from selenium.webdriver.common.keys import Keys
import time

SCROLL = 0

form_error_msg = {
    "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
    "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
    "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
    "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"}

footer_error_msg = {
    "name": '#footer > form > div > div:nth-child(1) > label > span',
    "email": "#footer > form > div > div:nth-child(2) > label > span",
    "phone": "#footer > form > div > div:nth-child(3) > label > span"}

soc_dict = {
    'Facebook': 'https://www.facebook.com/Herolofrontend',
    'Linkedin': 'https://www.linkedin.com/company/herolo/',
    'WhatsApp': 'https://api.whatsapp.com/send?phone=972544945333',
    'WebSite': 'https://herolo.co.il/?lang=he'
}

class HeroloPage(Browser):

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
            time.sleep(1)
            return self.driver.current_url
        except Exception as e:
            raise ValueError(e)

    def get_social_link(self, name):
        global soc_dict
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

    @staticmethod
    def _is_null(field):
        return field == 'null'

    def form_section_inputs(self, name, company, email, telephone):

        try:
            form = self.driver.find_element_by_id('section-inputs')
            submit = form.find_element_by_css_selector('a[type="button"]')

            fields = [
                {'text': 'name', 'value': name},
                {'text': 'company', 'value': company},
                {'text': 'email', 'value': email},
                {'text': 'telephone', 'value': telephone}
            ]

            for field in fields:
                if self._is_null(field['value']):
                    field['value'] = ""

                name_field = form.find_element_by_id(field['text'])
                name_field.send_keys(Keys.CONTROL + "a")
                name_field.send_keys(Keys.DELETE)
                name_field.send_keys(field['value'])

            submit.click()
            time.sleep(0.5)
        except Exception as e:
            raise ValueError(e)

    def err_msg_empty_field(self, id_field):
        global form_error_msg
        try:
            form = self.driver.find_element_by_id('section-inputs')
            input_name = form.find_element_by_id(id_field)
            input_name.click()
            form.click()
            time.sleep(0.5)
            span = form.find_element_by_css_selector(form_error_msg[id_field])
            return 'הוא שדה חובה' in span.text
        except Exception as e:
            raise ValueError(e)

    def err_msg_fill_field(self, id_field, text, ch_status):
        global form_error_msg
        try:
            form = self.driver.find_element_by_id('section-inputs')
            input_name = form.find_element_by_id(id_field)

            time.sleep(0.5)
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(text)
            form.click()
            span = form.find_element_by_css_selector(form_error_msg[id_field])
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

    def find_element_by_partial_link_text(self, partial_link_text):
        try:
            return self.driver.find_element_by_partial_link_text(partial_link_text)

        except Exception as e:
            raise ValueError(e)

    def err_msg_empty_field_footer(self, id_field):
        global footer_error_msg
        try:
            form = self.driver.find_element_by_id('footer')
            input_name = form.find_element_by_name(id_field)
            input_name.send_keys(Keys.ENTER)
            time.sleep(0.5)
            span = form.find_element_by_css_selector(footer_error_msg[id_field])
            print(span.text, 'הוא שדה חובה' in span.text)
            return 'הוא שדה חובה' in span.text
        except Exception as e:
            raise ValueError(e)

    def err_msg_fill_field_footer(self, id_field, text, ch_status):
        global footer_error_msg
        try:
            form = self.driver.find_element_by_id('footer')
            input_name = form.find_element_by_name(id_field)

            time.sleep(0.5)
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(text)
            form.click()
            if ch_status:
                try:
                    span = form.find_element_by_css_selector(footer_error_msg[id_field])
                except:
                    return True
            return 'לא חוקי' in span.text
        except Exception as e:
            raise ValueError(e)