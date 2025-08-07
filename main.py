import time

from cffi.cffi_opcode import CLASS_NAME
#from jsonschema.benchmarks.const_vs_enum import value

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_tariff = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_button = (By.CLASS_NAME, 'np-text')
    phone_input = (By.ID, 'phone')
    flash_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[1]/div[2]')
    vehicleTypeButton = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[2]/div[3]')
    askForACab = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    addCardButton = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    card_number = (By.XPATH, '//*[@id="number"]')
    cardCvv = (By.NAME, 'code')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    add_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    messageForDriver = (By.ID, 'comment')
    blanketAndTissues = (By.CLASS_NAME, 'slider round')
    chocolateIceCreamButton = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]' )
    strawBerryIceCreamButton = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div/div[3]')
    reserve_button = (By,CLASS_NAME, 'smart-button')
    sms_codes = (By. ID, 'code')
    submitSmsCodeButton = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    carCheckBox = (By.XPATH, '//*[@id="card-1"]')
    exit_payment_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.driver.implicitly_wait(10)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def set_tariff_flash(self):
        self.driver.find_element(*self.flash_button).click()

    def set_taxi(self):
        self.driver.find_element(*self.vehicleTypeButton).click()

    def click_askForACab(self):
        self.driver.find_element(*self.askForACab).click()

    def set_comfort_tariff(self):
        self.wait.until(expected_conditions.element_to_be_clickable(self.comfort_tariff)).click()

    def click_phone_button(self):
        self.driver.find_element(*self.phone_button).click()

    def set_phone_input(self):
        self.driver.find_element(*self.phone_input).send_keys(data.phone_number)

    def set_phone_info(self):
        self.driver.find_element(*self.next_button).click()

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_new_card(self):
        self.driver.find_element(*self.addCardButton).click()

    def set_card_number(self):
        self.driver.find_element(*self.card_number).send_keys(data.card_number)

    def set_cardCvv(self):
        self.driver.find_element(*self.cardCvv).send_keys(data.card_code + Keys.TAB)

    def get_cardCVV(self):
        return self.driver.find_element(*self.cardCvv).get_property('value')

    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()

    def click_exit_payment_window(self):
        self.driver.find_element(*self.exit_payment_window).click()

    def set_message_to_driver(self):
        self.driver.find_element(*self.messageForDriver).send_keys(data.message_for_driver)

    def click_add_chocolate_iceCream(self):
        self.driver.find_element(*self.chocolateIceCreamButton).click()

    def click_add_strawberry_iceCream(self):
        self.driver.find_element(*self.strawBerryIceCreamButton).click()

    def click_make_reserve(self):
        self.driver.find_element(*self.reserve_button).click()

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.sms_codes).send_keys(code)

    def click_submit_sms_code_buttom(self):
        self.driver.find_element(*self.submitSmsCodeButton).click()

    #Metodos Auxiliares

    def prepare_basic_route(self):
        self.driver.get(data.urban_routes_url)
        #page = UrbanRoutesPage(self.driver)
        self.set_route(data.address_from, data.address_to)
        #return page

    def prepare_comfort_tariff(self):
        self.prepare_basic_route()
        self.set_tariff_flash()
        self.set_taxi()
        self.click_askForACab()
        self.set_comfort_tariff()
        #return self

    def prepare_phone_input(self):
        self.prepare_comfort_tariff()
        self.click_phone_button()
        self.set_phone_input()
        self.set_phone_info()
        self.set_sms_code()
        self.click_submit_sms_code_buttom()
        #return self


    def prepare_pp_method(self):
        self.prepare_phone_input()
        self.click_payment_method()
        self.click_add_new_card()
        self.set_card_number()
        self.set_cardCvv()
        self.click_add_button()

        #return self

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.prepare_comfort_tariff()

        element =self.driver.find_element(*page.comfort_tariff)
        assert "tcard active" in element.get_attribute("class")

    def test_set_phone_input(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.prepare_phone_input()

        element = self.driver.find_element(*page.phone_input)
        assert '+13235554817' in element.get_attribute('value')

    def test_add_new_card(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.prepare_pp_method()

        element = self.driver.find_element(*page.carCheckBox)
        assert 'checkbox' in element.get_attribute("class")

    def test_message_to_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.prepare_pp_method()
        page.set_message_to_driver()

        element = self.driver.find_element(*page.messageForDriver)
        assert 'Muéstrame el camino al museo' in element.get_attribute("value")

    def test_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.prepare_pp_method()
        page.click_exit_payment_window()
        page.click_add_chocolate_iceCream()
        page.click_add_strawberry_iceCream()

        chocolate = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]').text
        strawberry = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div/div[2]').text

        assert chocolate == "1", f"Esperado 1 chocolate, y resulto {chocolate}"
        assert strawberry == "1", f"Esperado 1 fresa, y resulto {strawberry}"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
