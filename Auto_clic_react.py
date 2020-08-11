from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import credentials

if __name__ == '__main__':
    
    options = Options()
    options.add_argument("--headless")
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    
    driver = webdriver.Firefox(profile, executable_path="Z:\\Projet\\Coucou cliqueur\\geckodriver.exe", options=options)
    driver.get(f"https://www.messenger.com/t/{credentials.GROUPE}")
    driver.find_element_by_name("email").send_keys(credentials.USERNAME)
    driver.find_element_by_name("pass").send_keys(credentials.PASSWORD)
    driver.find_element_by_name("login").click()

    while True:
        try:
            if driver.find_elements_by_class_name("_ih3")[-1].text != credentials.NAME:
                driver.find_element_by_class_name("_5j_u").click()
                time.sleep(1)
                print("clic")
            else:
                print("un tour de boucle")
                time.sleep(5)
        except:
            pass
