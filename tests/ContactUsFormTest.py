import unittest
import pytest
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm
import AppiumFrameWork.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInForm(self):
        self. cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=4)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
