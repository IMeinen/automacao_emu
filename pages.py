from functions import Locators

'''
    Através desse pacote é feito o mapeamento dos elementos e todas as funções que interagem com eles
'''


class AcessarGoogle(Locators):
    """ A classe 'AcessarGoogle' mapeia os elementos e chama as funções para interagir com eles  """
    def __init__(self):
        """ O método 'init' herda da classe 'Locators' e faz o mapeamento dos elementos que vão ser usados """
        super().__init__()

        self.CAIXA_TEXTO = 'q'
        self.ZALLPY_LINK = 'LC20lb'
        self.OPORTUNIDADES_BUTTON = 'OPORTUNIDADES'
        self.OPORTUNIDADES_DESENVOLVEDOR = 'title title-custom'

    def selecionar_caixa_texto(self):
        """ O método 'selcionar_caixa_texto' seleciona o input mapeado em 'CAIXA_TEXTO' """
        self.preencher_texto('zallpy', self.driver.find_element_by_name(self.CAIXA_TEXTO))

    def teclar_botao_enter(self):
        """ O método 'teclar_botao_enter' tecla no botão enter no elemento 'CAIXA_TEXTO' """
        self.botao_enter(self.driver.find_element_by_name(self.CAIXA_TEXTO))

    def clicar_link_zallpy(self):
        """ O método 'clicar_link_zallpy' clica no link do elemento 'ZALLPY_LINK' """
        self.clicar_elemento(self.driver.find_element_by_class_name(self.ZALLPY_LINK))

    def selecionar_oportunidades(self):
        """ O método 'selecionar_oportunidades' clica no botão 'OPORTUNIDADES' no site da Zallpy """
        self.clicar_elemento(self.driver.find_element_by_link_text(self.OPORTUNIDADES_BUTTON))

    def selecionar_vagas_dev(self):
        """ A função 'selecionar_vagas_dev' retorna uma lista com todas as vagas da página de 'oportunidades' """
        lis = self.driver.find_elements_by_tag_name('h2')
        lis = [x.text for x in lis]
        return lis
