# Projeto: Gerador de README
![exemplo](https://indify.co/widgets/live/countdown/p2OgzaK9xLU8cVq7ZQPo)

<p align="center">
   <img alt="Static Badge" src="https://img.shields.io/badge/STATUS-EM_DESENVOLVIMENTO-yellow">
</p>

## Estrutura do Projeto:
```
gerador_readme/
│
├── src/
│   ├── components/
│   │   ├── logo_component.py
│   │   ├── status_component.py
│   │   └── ...
│   └── templates/
│       └── template.txt
│
├── pub_components.json
└── README.md
```

## Descrição:
Um projeto para automatizar a criação de README.md para projetos do GitHub. O usuário pode definir modelos (templates) de README.md com componentes personalizados e preenchê-los com dados específicos.

## Funcionalidades:
1. **Definindo Componentes:**
   - O usuário pode criar novos componentes executando `cgmd create component <nome_do_componente>` no terminal. Isso cria um arquivo de componente na pasta `src/components` e atualiza o arquivo `pub_components.json`.

2. **Criando um Arquivo de Template:**
   - O usuário define um arquivo de template em `src/templates/template.txt`, que contém a estrutura do README.md com marcadores para os componentes.

3. **Lendo e Preenchendo o Template:**
   - Um script Python lê o arquivo de template e solicita as informações necessárias para preencher cada componente.
   - Para cada componente no template, o script solicita as informações específicas e preenche os marcadores no template.

4. **Gerando o README.md:**
   - Com todas as informações coletadas, o script Python substitui os marcadores no template pelos dados fornecidos.
   - O script gera o arquivo README.md final na raiz do projeto.

## Scripts Python:
1. **`cgmd.py`:**
   - Script principal para gerenciar a criação de componentes, preenchimento do template e geração do README.md.

2. **`component.py`:**
   - Módulo contendo funções relacionadas à criação de novos componentes.

3. **`template.py`:**
   - Módulo contendo funções relacionadas à leitura e preenchimento do template.

4. **`generator.py`:**
   - Módulo contendo funções para gerar o README.md final.

## Arquivos:
- **`pub_components.json`:**
   - Arquivo JSON que mantém o registro de todos os componentes disponíveis e seus caminhos de importação.

- **`README.md`:**
   - README principal do projeto.

## Setup e Uso:
1. Execute `cgmd init` para inicializar o projeto.
2. Crie novos componentes com `cgmd create component <nome_do_componente>`.
3. Defina o arquivo de template em `src/templates/template.txt`.
4. Execute `cgmd generate` para preencher o template e gerar o README.md final.

## Desenvolvedores

[<img src="https://avatars.githubusercontent.com/Emerson-Vitor" width=115><br><sub>Emerson V P Silva</sub>](https://github.com/Emerson-Vitor)
