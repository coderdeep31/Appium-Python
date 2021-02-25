import unittest
from AppiumFrameWork.tests.LoginTest import LoginTest
from AppiumFrameWork.tests.ContactUsFormTest import ContactFormTest


lt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

regressiontest = unittest.TestSuite([lt, cf])

unittest.TextTestRunner(verbosity= 2).run(regressiontest)