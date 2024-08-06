from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho para o WebDriver (substitua pelo caminho correto do seu WebDriver)
driver_path = 'path/to/chromedriver'

# Inicializa o navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Abre a página desejada
driver.get('https://www.python.org')

try:
    # Espera até que um elemento específico esteja presente na página (tempo máximo de espera de 10 segundos)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'element_id'))
    )
    # Interaja com o elemento encontrado
    element.click()

except:
    print("Elemento não encontrado no tempo especificado")

finally:
    # Fecha o navegador
    driver.quit()
