from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
from datetime import datetime


def capturar_pantalla(driver, nombre_archivo):
    """Toma una captura de pantalla y la guarda en una carpeta 'screenshots'"""
    # Crear carpeta si no existe
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    
    # Generar nombre del archivo con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta_archivo = f"screenshots/{nombre_archivo}_{timestamp}.png"
    
    # Tomar captura
    driver.save_screenshot(ruta_archivo)
    print(f"Captura guardada: {ruta_archivo}")
    return ruta_archivo

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/register")
    return driver

# Inicializar el navegador
driver = get_driver()

# Tomar captura del formulario vacío
capturar_pantalla(driver, "formulario_vacio")



def datos_formulario_registro(driver):
    # Datos de registro completos
    datos_registro = {
        "firstname": "Jesus",
        "lastname": "Anachury",
        "userName": "janachury" + str(int(time.time())),  # Nombre de usuario único
        "password": "P@ssw0rd123",
        "confirmPassword": "P@ssw0rd123"  # Asegurarse de que coincida con la contraseña
    }
    
    print("Llenando formulario de registro...")
    
    # Llenar cada campo del formulario
    for campo, valor in datos_registro.items():
        try:
            # Algunos campos pueden necesitar un selector diferente
            if campo == "country":
                # Para el campo de país que es un select
                select = Select(driver.find_element(By.ID, "country"))
                select.select_by_visible_text(valor)
            elif campo == "state":
                # Algunos campos pueden necesitar un selector específico
                driver.find_element(By.ID, "state").send_keys(valor)
            else:
                # Para la mayoría de los campos de entrada de texto
                elemento = driver.find_element(By.ID, campo)
                elemento.clear()
                elemento.send_keys(valor)
                
            print(f"Campo '{campo}' completado")
            time.sleep(0.5)  # Pequeña pausa entre campos
            
        except Exception as e:
            print(f"Error al llenar el campo {campo}: {str(e)}")
    
    # Hacer clic en el botón de registro
    try:
        # Tomar captura antes de enviar el formulario
        capturar_pantalla(driver, "antes_de_enviar")
        
        # Enviar formulario
        driver.find_element(By.ID, "register").click()
        print("Formulario de registro enviado")
        time.sleep(2)
        
        # Tomar captura después de enviar el formulario
        capturar_pantalla(driver, "despues_de_enviar")
        
    except Exception as e:
        capturar_pantalla(driver, "error_en_formulario")
        print(f"Error al enviar el formulario: {str(e)}")



def hacer_login(driver, usuario, contraseña):
    # Ir a la página de login
    driver.get("https://demoqa.com/login")
    time.sleep(2)
    
    # Llenar credenciales
    driver.find_element(By.ID, "userName").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(contraseña)
    
    # Hacer clic en el botón de login
    driver.find_element(By.ID, "login").click()
    time.sleep(2)
    
    
   

def main():
    datos_formulario_registro(driver=driver)
    hacer_login(driver=driver, usuario="anachury", contraseña="anachury15")
   
    
   
    # Cerrar el navegador
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()