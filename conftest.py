import pytest
from selenium import webdriver

def pytest_addoption(parser):
   parser.addoption('--language', action='store', default='en-gb',
                    help='Please, select language')
   parser.addoption('--browser_name', action='store',
                    default='chrome', help='Allowed browsers: chrome and firefox')
   
def is_browser_allowed(selected_browser):
   browsers_allowed = ['chrome', 'firefox']
   assert selected_browser != None, '\n\n\n ---> Please, select browser <--- \n\n'
   assert browsers_allowed.count(
      selected_browser) != 0, f"\n\n\n ---> Selected browser ({selected_browser}) is not allowed <--- \n\n"

def is_language_allowed(selected_language):
   languages_allowed = ['en-gb', 'en', 'ar', 'ca', 'cs', 'da', 'de', 'el', 'es', 'fi',
      'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']
   assert selected_language != None, "\n\n\n ---> Please, select language <--- \n\n"
   assert languages_allowed.count(
      selected_language) != 0, f"\n\n\n ---> Selected language ({selected_language}) is not allowed <--- \n\n"

@pytest.fixture
def browser(request):

   browser_name = request.config.getoption("browser_name")
   is_browser_allowed(browser_name)
   
   user_language = request.config.getoption("language")
   is_language_allowed(user_language)

   if browser_name == "chrome":
      options = webdriver.ChromeOptions()
      options.add_experimental_option(
         'prefs', {'intl.accept_languages': user_language})
      browser = webdriver.Chrome(options=options)
   elif browser_name == "firefox":
      fp = webdriver.FirefoxProfile()
      fp.set_preference("intl.accept_languages", user_language)
      browser = webdriver.Firefox(firefox_profile=fp)      

   yield browser

   browser.quit()

