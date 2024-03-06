import pyautogui
import pandas 
import time

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa

# Abrir o navegador (chrome) e entrar no site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Pausa maior para carregar a página
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=779, y=410)
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha12345")
pyautogui.click(x=965, y=570)

# Pausa maior para carregar a página
time.sleep(3)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo até o final da base de dados