#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1

#1 - entrar sistema da empresa
pyautogui.press("win")
pyautogui.write("Opera") #escreve o nome do navegador
pyautogui.press("enter")

time.sleep(2)


pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

#2 - fazer o login
pyautogui.click(x=861, y=370)
pyautogui.write("meu_login")
pyautogui.click(x=837, y=457)
pyautogui.write("minha_senha")

#clicar em acessar

pyautogui.click(x=910, y=507)   
time.sleep(3)

#3 - exportar base de dados

pyautogui.click(x=489, y=305) #seleciona opções do documento
pyautogui.click(x=589, y=799) #clica em download

time.sleep(5)





# In[16]:


import pandas

#4 - Tirar os dados necessários da tabela
tabela = pandas.read_csv(r"C:\Users\ttana\Downloads\Compras.csv", sep=";")#INSERIR O CAMINHO DO ARQUIVO DENTRO DO TEU COMPUTADOR
display(tabela)

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)


# In[19]:


#5 - enviar as informações para o email 
pyautogui.press("win")
pyautogui.write("Opera") #escreve o nome do navegador
pyautogui.press("enter")
pyautogui.click(x=676, y=78)
##pyautogui.write("https://mail.google.com/mail/u/1/#inbox") #inserir o email do remetente
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=80, y=196) #clica para escrever email novo no gmail

pyautogui.write("xxx@gmail.com") #vai escrever o email do destinatário
pyautogui.press("tab") #selecionar destinatário

pyautogui.press("tab") #passar para o campo "assunto"
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") #passar para o corpo do texto

texto = f"""Prezados,

Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de produtos: {quantidade:,}
Preço médio: R${preco_medio:,.2f}

Qualquer dúvida, favor entrar em contato.

Att. Takashi Tanaka
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")
pyautogui.hotkey("crtl", "enter")


# In[ ]:


# linha de código para rodar e achar a posição do mouse necessário
#time.sleep(5)
#print(pyautogui.position())

