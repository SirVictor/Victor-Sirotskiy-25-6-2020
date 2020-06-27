
from browser import Browser
from selenium.webdriver.common.keys import Keys
import time


form_error_msg = {
    "name": '#section-inputs > div:nth-child(1) > div:nth-child(1) > span',
    "company": "#section-inputs > div:nth-child(1) > div:nth-child(2) > span",
    "email": "#section-inputs > div:nth-child(2) > div:nth-child(1) > span",
    "telephone": "#section-inputs > div:nth-child(2) > div:nth-child(2) > span"
}

footer_error_msg = {
    "name": '#footer > form > div > div:nth-child(1) > label > span',
    "email": "#footer > form > div > div:nth-child(2) > label > span",
    "phone": "#footer > form > div > div:nth-child(3) > label > span"
}

soc_dict = {
    'Facebook': 'https://www.facebook.com/Herolofrontend',
    'Linkedin': 'https://www.linkedin.com/company/herolo/',
    'WhatsApp': 'https://api.whatsapp.com/send?phone=972544945333',
    'WebSite': 'https://herolo.co.il/?lang=he'
}

pop_up_err_msg = {

            "name": '#modal-form > div > div:nth-child(1) > label > span',
            "email": "#modal-form > div > div:nth-child(2) > label > span",
            "phone": "#modal-form > div > div:nth-child(2) > label > span"
}


class HeroloPage(Browser):
    SCROLL = 0

    def set_scroll_position(self, position):
        try:
            self.driver.execute_script(f"window.scrollTo(0,{position})")

            time.sleep(1)

            self.SCROLL = self.get_scroll_position()
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
            time.sleep(2)
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
                    form.find_element_by_css_selector(footer_error_msg[id_field])
                    return False
                except:
                    return True

            return 'לא חוקי' in form.find_element_by_css_selector(footer_error_msg[id_field]).text
        except Exception as e:
            raise ValueError(e)

    def footer_form_section_inputs(self, name, email, telephone):
        def _is_null(element):
            return element == 'null'
        try:
            form = self.driver.find_element_by_id('footer')
            submit = form.find_element_by_css_selector('button')

            fields = [
                {'text': 'name', 'value': name},
                {'text': 'email', 'value': email},
                {'text': 'phone', 'value': telephone}
            ]

            for field in fields:
                if _is_null(field['value']):
                    field['value'] = ""

                name_field = form.find_element_by_name(field['text'])
                name_field.send_keys(Keys.CONTROL + "a")
                name_field.send_keys(Keys.DELETE)
                name_field.send_keys(field['value'])

            submit.click()
            time.sleep(0.5)
        except Exception as e:
            raise ValueError(e)

    def scroll_down_and_back_to_the_top(self):

        down = 5000

        try:
            for i in range(0, down, 5):
                self.driver.execute_script(f"window.scrollTo(0,{i})")
            time.sleep(5)
            for i in range(down - 1, 0, -5):
                self.driver.execute_script(f"window.scrollTo(0,{i})")
            time.sleep(25)
        except Exception as e:
            raise ValueError(e)

    def empty_fields_pop_up_form(self, pop_up_div):
        try:
            pop_up_div.find_element_by_css_selector("button").click()
            if self.get_current_url() == 'https://automation.herolo.co.il/':
                for name in pop_up_err_msg.keys():
                    span = pop_up_div.find_element_by_css_selector(pop_up_err_msg[name])
                    print(span.text, 'הוא שדה חובה' in span.text)
                    if 'הוא שדה חובה' not in span.text:
                        return False
                return True
            return False
        except Exception as e:
            raise ValueError(e)

    def err_msg_fill_field_pop_up(self, name, text, ch_status):
        global pop_up_err_msg
        try:
                    div = self.driver.find_element_by_css_selector('div[class="ReactModalPortal"]')

                    input_name = div.find_element_by_name(name)

                    time.sleep(0.5)
                    input_name.send_keys(Keys.CONTROL + "a")
                    input_name.send_keys(Keys.DELETE)

                    input_name.send_keys(text)

                    if ch_status == "True":
                        try:
                            div.find_element_by_css_selector(pop_up_err_msg[name])
                            return False
                        except:
                            return True
                    else:
                        return 'לא חוקי' in div.find_element_by_css_selector(pop_up_err_msg[name]).text

        except Exception as e:
            raise ValueError(e)

    def pop_up_form_section_inputs(self, name, email, telephone):

        def _is_null(element):
            return element == 'null'

        try:

            div = self.driver.find_element_by_css_selector('div[class="ReactModalPortal"]')
            btn = div.find_element_by_css_selector('button')

            fields = [
                {'text': 'name', 'value': name},
                {'text': 'email', 'value': email},
                {'text': 'phone', 'value': telephone}
            ]

            for field in fields:
                if _is_null(field['value']):
                    field['value'] = ""

                name_field = div.find_element_by_name(field['text'])
                name_field.send_keys(Keys.CONTROL + "a")
                name_field.send_keys(Keys.DELETE)
                name_field.send_keys(field['value'])

            btn.click()
            time.sleep(0.5)
        except Exception as e:
            raise ValueError(e)

    def close_pop_up(self):

        try:
            div = self.driver.find_element_by_css_selector('div[class="ReactModalPortal"]')
            spans = div.find_elements_by_css_selector('span')
            close = [span for span in spans if str(span.get_attribute('class')).startswith("onUnloadPopup__Close")][0]
            close.click()
        except Exception as e:
            raise ValueError(e)

    def _is_pop_up_closed(self):
        try:
            if  self.driver.find_element_by_css_selector('div[class="ReactModalPortal"]').text == "":
                return True
            return False
        except Exception as e:
            raise ValueError(e)