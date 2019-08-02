from pages import AcessarGoogle

''' O pacote é responsável por definir as ações que vão ser seguidas no teste'''


class MinhaAction(AcessarGoogle):
    def __init__(self):
        """ O método 'init' herda da classe 'AcessarGoogle' """
        super().__init__()

    def pesquisar(self):
        """ O método 'pesquisar' pesquisa 'zallpy' no Google """
        self.selecionar_caixa_texto()
        self.teclar_botao_enter()

    def acessar_site(self):
        """ O método 'acessar_site' acessa o link do site da Zallpy no Google """
        self.clicar_link_zallpy()

    def acessar_oportunidades(self):
        """ O método 'acessar_oportunidades' acessa a aba de 'Oportunidades' no site da Zallpy """
        self.selecionar_oportunidades()

    def validar_vaga_dev(self,tipo_vaga) -> bool:
        """ A função 'validar_vaga_dev' recebe a lista com as vagas disponíveis,
         e retorna 'True' se encontrou alguma vaga de 'tipo_vaga' """
        lista = self.selecionar_vagas_disponiveis()
        if any(tipo_vaga in texto.lower() for texto in lista):
            return True
        else:
            print('Vagas de {} não encontradas!'.format(tipo_vaga))
