import pyautogui
import time

pyautogui.PAUSE = 1


pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


pyautogui.click(x=676, y=485)

pyautogui.write("Programador.Dev@gmail.com")
pyautogui.press("tab") 
pyautogui.write("Estagiario")
pyautogui.click(x=1000, y=687)
time.sleep(3)


import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:
    
    pyautogui.click(x=700, y=339)
   
    codigo = tabela.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
   
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)
   
