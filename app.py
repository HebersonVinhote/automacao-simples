import pyautogui
import time
import pandas as pd

# sistema https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o navegador
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(5)

# Fazer Login
# Selecionar o campo de email
pyautogui.click(x=527, y=390)
pyautogui.write('pydatalab@gmail.com')

#selecionar o campo senha
pyautogui.click(x=476, y=487)
pyautogui.write('Foquinha.23!')

#clicar em Login
pyautogui.click(x=655, y=546)
time.sleep(5)

# importar base de dados
produtos = pd.read_csv('./produtos.csv')

# Cadastro de produtos
for linha in produtos.index:
    pyautogui.click(x=428, y=276)
    pyautogui.write(str(produtos.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = produtos.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
    pyautogui.click(x=471, y=275)