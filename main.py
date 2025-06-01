from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    return webdriver.Chrome(options=options)

def registro(driver):
    driver.get("https://demoqa.com/register")
    time.sleep(2)

    datos = {
        "firstname": "jesus david",
        "lastname": "anachury",
        "userName": "Anachury15",
        "password": "Anachury@1520001",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)

    # generar simulación de captcha
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "recaptcha-anchor").click()
    time.sleep(10)
    driver.switch_to.default_content()

    # Habilitar el botón Register de manera manual
    boton_register(driver)

    # Hacer clic en el botón Register
    driver.find_element(By.ID, "register").click()
    time.sleep(10)

    # Volver a login
    driver.find_element(By.ID, "gotologin").click()
    time.sleep(2)

def boton_register(driver):
    driver.execute_script("document.getElementById('register').disabled = false;")
    time.sleep(1)

def usuario(driver):

    driver.find_element(By.ID, "userName").send_keys("Anachury15")
    driver.find_element(By.ID, "password").send_keys("Anachury@1520001")
    driver.find_element(By.ID, "login").click()
    time.sleep(3)

def verificar_login(driver):
    try:
        logout_btn = driver.find_element(By.ID, "submit")
        if logout_btn.text.strip().lower() == "log out":
            print("inicio de sesión.")
        else:
            print("inicio de sesión fallido.")
    except Exception:
        print(" login fallido.")

def main():
    driver = get_driver()
    registro(driver)
    usuario(driver)
    verificar_login(driver)
    boton_register(driver)
    driver.quit()

if __name__ == "__main__":
    main()