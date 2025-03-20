
import openpyxl 
import pyautogui 
import subprocess
import time
import sys
import os

caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_sistema = os.path.join(caminho_atual, 'System_app.py')
processo_sistema = subprocess.Popen([sys.executable, caminho_sistema])
time.sleep(5)
workbook= openpyxl.load_workbook('vendas_de_produtos.xlsx')

vendas_sheet= workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    #nome
    pyautogui.click(868,503, duration=1.5)
    pyautogui.write(linha[0].value)
    #produto
    pyautogui.click(871,524, duration=1.5)
    pyautogui.write(linha[1].value)
    #quantidade
    pyautogui.click(887,553, duration=1.5)
    pyautogui.write(str(linha[2].value))
    #categoria
    pyautogui.click(955,578, duration=1.5)
    pyautogui.write(linha[3].value)
    #salvar
    pyautogui.click(829,598, duration=1.5)
    #confirma
    pyautogui.click(827,570, duration=1.5)

    
    
