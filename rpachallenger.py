from playwright.sync_api import sync_playwright
from time import sleep
import pandas as pd
from download import baixarDesafioRPA
from params import Params

download = baixarDesafioRPA(r'./', 'desafioRPA.xlsx')


dataframe = pd.read_excel(download)
# print(dataframe)

with sync_playwright() as p:

    url = 'https://rpachallenge.com/?lang=EN'
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    p = Params()
    page.locator(str(p.start)).click()

    for i, row in dataframe.iterrows():
        try:
            page.locator(p.telefone).fill(str(row['Phone Number']))
            page.locator(p.nomeCompania).fill(row['Company Name'])
            page.locator(p.endereco).fill(row['Address'])
            page.locator(p.cargo).fill(row['Role in Company'])
            page.locator(p.primeiroNome).fill(row['First Name'])
            page.locator(p.ultimoNome).fill(row['Last Name '])
            page.locator(p.email).fill(row['Email'])
            page.locator(p.submit).click()

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    sleep(5)
    mensagem = page.evaluate(
        """ ( el ) => {return document.querySelector( el ).innerText} """, 'div[class="message2"]')

    print(mensagem)
