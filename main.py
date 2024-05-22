#PASSO A PASSO DO PROJETO 

#1 ABIR O NAVEGADOR 
#2 LOGAR NO SISTEMA DA EMPRESA
#3 ACESSAR O BANCO DE DADOS / IMPORTAR 
#4 CADASTRAR UM PRODUTO
#5 REPETIR ISSO ATÉ CADASTRAR TUDO

import pyautogui
import time
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=527, y=401)
pyautogui.write('jonathan.analista')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')

import pandas

tabela = pandas.read_csv('produtos.csv')

print(tabela)
print(tabela.loc[ :,'codigo'])

time.sleep(2)



for linha in tabela.index:  
    codigo = str(tabela.loc[linha,'codigo'])

    pyautogui.click(x=445, y=300)

    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write (str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')

    pyautogui.write (str(tabela.loc[linha,'tipo']))
    pyautogui.press('tab')

    pyautogui.write (str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')

    pyautogui.write (str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write (str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')
 
    obs = (str(tabela.loc[linha,'obs']))
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(4000)
