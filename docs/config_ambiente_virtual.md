# Tutorial: Preparação do Ambiente Virtual para um Projeto

Neste tutorial, será explicado como criar um ambiente virtual isolado para o desenvolvimento de projetos, utilizando as ferramentas estudadas em sala de aula. O objetivo é proporcionar um ambiente limpo e organizado, integrando-o tanto ao Jupyter Notebooks quanto ao Visual Studio Code (VSCode).

## Passo 1: Instalação do Anaconda

Baixe e instale o Anaconda a partir do [site oficial](https://www.anaconda.com/download).

## Passo 2: Criação do Ambiente Virtual

    1. Abra o terminal (Linux/macOS) ou prompt de comando (Windows).

    2. Execute o seguinte comando para criar um ambiente virtual chamado "meu_projeto":

` conda create --name meu_projeto python=3.8 `


    3. Ative o ambiente virtual:

    No Linux/macOS:

`conda activate meu_projeto`

    No Windows:

`conda activate meu_projeto`

## Passo 3: Instalação do Jupyter Notebooks

    - Com o ambiente virtual ativo, instale o Jupyter Notebooks:

`conda install jupyter`

## Passo 4: Integração com Jupyter Notebooks

    - Certifique-se de que o ambiente virtual está ativado.

    - Execute o seguinte comando para instalar o kernel do Jupyter no ambiente virtual:

`python -m ipykernel install --user --name=meu_projeto`

## Passo 5: Instalação do Visual Studio Code (VSCode)

Baixe e instale o Visual Studio Code a partir do [site oficial](https://code.visualstudio.com/download).

Instale a extensão "Python" no VSCode para suporte ao desenvolvimento Python.

## Passo 6: Configuração do Ambiente Virtual no VSCode

    - Abra o VSCode.

    - Vá para a seção de extensões, pesquise por "Python Extension Pack" e instale-a.

    - No canto inferior direito, clique no ambiente atual e selecione "Python: Select Interpreter". Escolha o interpretador do ambiente virtual criado.

    Ao seguir esses passos, teremos um ambiente virtual isolado pronto para o desenvolvimento do próximo exercício, integrado tanto ao Jupyter Notebooks quanto ao Visual Studio Code.

## Passo 7: Discussão e Uniformização das ferramentas 

    Destaca-se a facilidade de uso do VSCode, além da utilização do Jupyter para prototipação rápida, mas percebe-se que a integração com o VSCode não foi tão intuitiva. Desafios específicos incluem a configuração inicial do ambiente virtual no Jupyter.

    O projeto requer tanto prototipação rápida quanto desenvolvimento de módulos e pacotes.
    A preferência pela eficiência no desenvolvimento levou à escolha do VSCode como a principal IDE.

    Verificou-se que o VSCode possui extensões eficientes para Python e integra-se bem com o Git, atendendo às necessidades do projeto. Dessa forma, decidiu-se uniformizar o ambiente de desenvolvimento, escolhendo o VSCode como a IDE principal para a equipe.



