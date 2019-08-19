
# Instalação do ambiente Linux –Ubuntu

Antes de iniciar a instalação do ambiente, atualize os programas do Ubuntu através do ícone “Atualizador de Programas” clicar em <Instalar agora>, após a atualização deve-se reiniciar o ambiente Linux:

<div align="left">
    <img width="75" heigth="75" src="https://github.com/IMeinen/automacao_emu/blob/master/images/atualizaor.png">
</div>

##### 1. Realizar o download do Chrome no Linux através do Mozilla:
    
##### 2. Acessar o aplicativo “Software Ubuntu” para download da ferramenta:
<div align="left">
    <img width="75" heigth="75" src="https://github.com/IMeinen/automacao_emu/blob/master/images/aplicativos.png">
</div>

##### 3. Realizar o download do Pycharm CE:
<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm1.png">
</div>

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm2.png">
</div>

##### 4. Realizar a instalação do Pycharm CE:

<div align="center">
    <img width="550" heigth="350" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm2%20(1).png">
</div>

<div align="center">
    <img width="350" heigth="250" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm.png">
</div>


<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm3.png">
</div>

Clicar na opção “Install and Enable” para o plugin “IdeaVim” e “Markdown”.
Após a instalação dos plugins, clicar em "Start Using Pycharm":

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm4.png">
</div>
    
Após a instalação do Pycharm, fechar o aplicativo para prosseguir com as demais configurações.

##### 5. Instalar o Chromedriver:
<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/Chromedriver.png">
</div>

Clicar na opção “Chromedriver_linux64.zip”:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/Chromedriver2.png">
</div>


Clicar na opção “Extrair”:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/Chromedriver3.png">
</div>

Será solicitado a pasta o qual será realizada a extração do arquivo, você pode colocar na pasta que fique melhor pra você, porém precisa salvar o caminho dela pois será executada na automação.
Neste caso será deixado na pasta “Downloads”.

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/Chromedriver4.png">
</div>

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/Chromedriver5.png">
</div>


##### 6. Abrir o prompt de comando e inserir os comandos:
  
    sudo apt install python.pip
    pip install webdriver
    pip install selenium
  
 Após a instalação do selenium, instalar a biblioteca do BDD:
 
    pip install behave

##### 7. Abrir o PyCharm e importar o projeto:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/pycharm5.png">
</div>

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/find_folder.png">
</div>


##### 8. Clicar na "features.feature" e instalar o Gherkin:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/gherkin.png">
</div>

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/gherkin2.png">
</div>



Reiniciar o Pycharm após a instalação do plugin.


##### 9. Configurar “Project Interpreter”:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/gherkin3.png">
</div>

Clicar na opção “Project Interpreter” e verificar se existe a opção “Python 3.6”, clicar em "OK":

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/interpreter2.png">
</div>

Caso não seja apresentado esta opção, retornando somente "No Interpreter", clicar na engrenagem ao lado do campo            e clicar na opção "add" .

Na tela abaixo, deve ser selecionado a opção <System Interpreter> e clicar na opção "OK", conforme print abaixo:

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/interpreter.png">
</div>

O sistema adicionará esta opção no “Project Interpreter”, em seguida devemos selecionar a opção “Python 3.6” e clicar em "OK".

<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/final_Py_1.png">
</div>

##### 10. Após estes passos seu ambiente de automação estará instalado e configurado com sucesso, faltando somente informar o caminho que encontra-se o chromedriver para execução dos testes automatizados, no arquivo “Locators.py”:

self.path = "/home/usuariodapasta/Downloads/chromedriver"

Exemplo:


<div align="center">
    <img width="750" heigth="550" src="https://github.com/IMeinen/automacao_emu/blob/master/images/final_Py_2.png">
</div>
