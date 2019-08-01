from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
    O pacote é responsável por conectar com o browser e com o site, 
    além de definir funções padrão para o acesso de elementos." 
'''


class Locators:

    def __init__(self):
        """ O método 'init' conecta com o browser e acessa o site passado no 'get' """
        self.path = "/home/arturmeinen/Downloads/chromedriver"
        self.driver = webdriver.Chrome(self.path)
        self.driver.get('https://www.google.com.br/')

    def preencher_texto(self, texto, elemento):
        """ O método 'preencher_texto' preenche um input do tipo text com o texto passado como parâmetro """
        elemento.send_keys(texto)

    def botao_enter(self, elemento):
        """ O método 'botao_enter' aperta enter no elemento passado como parâmetro """
        elemento.send_keys(Keys.ENTER)

    def clicar_elemento(self, elemento):
        """ O método 'clicar_elemento' clica no elemento passado como parâmetro """
        elemento.click()
