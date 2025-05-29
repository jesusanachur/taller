from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    # Primero obtener la URL antes de retornar
    driver.get("https://demoqa.com/register")
    sleep(2)
    return driver


def datos_registro(driver):    
    print("Llenando el formulario de registro...")
    try:
        # Llenar el formulario
        driver.find_element(By.ID, "firstname").send_keys("Jesus")
        sleep(1)
        driver.find_element(By.ID, "lastname").send_keys("Anachury")
        sleep(1)
        driver.find_element(By.ID, "userName").send_keys("janachury")
        sleep(1)
        driver.find_element(By.ID, "password").send_keys("P@ssw0rd123")
        sleep(1)
        
        # Hacer clic en el captcha
        click_captcha(driver)
        
        # Hacer clic en registrar
        driver.find_element(By.ID, "register").click()
        sleep(3)
        
        # Verificar si el registro fue exitoso
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "name"))
            )
            print("¡Registro exitoso!")
            return True
        except:
            print("Error: No se pudo completar el registro")
            return False
            
    except Exception as e:
        print(f"Error en el registro: {e}")
        return False


def click_captcha(driver):
    try:
        # Cambiar al iframe del captcha
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[contains(@src,'google.com/recaptcha')]")
            )
        )
        # Hacer clic en el captcha
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
        ).click()
        # Volver al contenido principal
        driver.switch_to.default_content()
        sleep(3)  # Esperar a que se complete la verificación
    except Exception as e:
        print(f"Error con el captcha: {e}")


def login(driver):
    try:
        print("\nIniciando sesión...")
        driver.get("https://demoqa.com/login")
        sleep(2)
        
        # Ingresar credenciales
        driver.find_element(By.ID, "userName").send_keys("janachury")
        sleep(1)
        driver.find_element(By.ID, "password").send_keys("P@ssw0rd123")
        sleep(1)
        
        # Hacer clic en login
        driver.find_element(By.ID, "login").click()
        sleep(3)
        
        # Verificar si el login fue exitoso
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "userName-value"))
            )
            print("¡Inicio de sesión exitoso!")
            return True
        except:
            print("Error: No se pudo iniciar sesión")
            return False
            
    except Exception as e:
        print(f"Error durante el inicio de sesión: {e}")
        return False


def stop_driver(driver):
    if driver:
        driver.quit()


def main():
    driver = None
    try:
        # Iniciar el navegador y cargar la página de registro
        driver = start_driver()
        
        # Realizar el registro
        if datos_registro(driver):
            # Si el registro fue exitoso, intentar hacer login
            login(driver)
            
    except Exception as e:
        print(f"Error en la ejecución: {e}")
    finally:
        # Cerrar el navegador
        stop_driver(driver)


if __name__ == "__main__":
    main()

