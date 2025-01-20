import pyautogui
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")

import time
time.sleep(5)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("eleanor.evans@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.click(x=364, y=221)

#PASSO 3 - importar base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)

#PASSO 4 - cadastrar um produto
# MOLO000251,Logitech,Mouse,1,25.95,6.50,

for linha in tabela.index:
    pyautogui.click(x=364, y=221)

    time.sleep(2)

    #Código Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preço Unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #Custo do Produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    #Apertar botão enviar
    pyautogui.press("enter")

    pyautogui.press("home") #subir a tela para o início

    pyautogui.click(x=364, y=221) #para clicar no campo código de novo

#PASSO 5 - repetir o processo para todos os produtos da tabela
