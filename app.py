import json

# Dados em formato JSON
data = {
    "logo": "caminho/para/logo_GlicoCare.png",
    "status": {
        "label": "Status",
        "message": "Concluído",
        "color": "green"
    },
    "descricao_projeto": "Descrição do projeto...",
    "imagem_descricao": "caminho/para/imagem_descricao.png",
    "funcionalidades": ["Funcionalidade 1", "Funcionalidade 2", "Funcionalidade 3"],
    "aplicacao_imagem": "caminho/para/aplicacao_imagem.png",
    "ferramentas_utilizadas": [
        {"nome": "Ferramenta 1", "logo": "caminho/para/logo_ferramenta1.png"},
        {"nome": "Ferramenta 2", "logo": "caminho/para/logo_ferramenta2.png"},
        {"nome": "Ferramenta 3", "logo": "caminho/para/logo_ferramenta3.png"}
    ],
    "link_codigo_fonte": "https://github.com/seu_usuario/projeto",
    "link_download": "https://github.com/seu_usuario/projeto/archive/main.zip",
    "desenvolvedores": [
        {"nome": "Desenvolvedor 1", "imagem": "caminho/para/imagem_dev1.png", "github": "https://github.com/dev1"},
        {"nome": "Desenvolvedor 2", "imagem": "caminho/para/imagem_dev2.png", "github": "https://github.com/dev2"},
        {"nome": "Desenvolvedor 3", "imagem": "caminho/para/imagem_dev3.png", "github": "https://github.com/dev3"}
    ]
}

# Construção do texto formatado
formatted_text = f'''
![logo]({data["logo"]})

---

<p align="center">
   <img src="http://img.shields.io/static/v1?label={data["status"]["label"]}&message={data["status"]["message"]}&color={data["status"]["color"]}&style=for-the-badge" alt="vitrinedev"/>
</p>

### Tópicos 

- [Descrição do projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Aplicação](#aplicação)
- [Ferramentas utilizadas](#ferramentas-utilizadas)
- [Acesso ao projeto](#acesso-ao-projeto)
- [Abrir e rodar o projeto](#abrir-e-rodar-o-projeto)
- [Desenvolvedores](#desenvolvedores)

## Descrição do projeto 

<p align="justify">
 {data["descricao_projeto"]}

![Descrição do projeto GlicoCare]({data["imagem_descricao"]})
</p>

## Funcionalidades

{"\n".join("- " + funcionalidade for funcionalidade in data["funcionalidades"])}

## Aplicação

<div align="center">

![Android Emulator]({data["aplicacao_imagem"]})

</div>

###

## Ferramentas utilizadas

{"\n".join(f"<a href='{tool['nome']}' target='_blank'> <img src='{tool['logo']}' alt='{tool['nome']}' width='40' height='40'/> </a>" for tool in data["ferramentas_utilizadas"])}

###

## Acesso ao projeto

Você pode [acessar o código fonte do projeto]({data["link_codigo_fonte"]}) ou [baixá-lo]({data["link_download"]}).

## Abrir e rodar o projeto

Após baixar o projeto, você pode abrir com o `Android Studio`. Para isso, na tela de launcher clique em:

- `Open an Existing Project` (ou alguma opção similar);
- Procure o local onde o projeto está e o selecione (Caso o projeto seja baixado via zip, é necessário extraí-lo antes de procurá-lo);
- Por fim clique em `OK`.

O `Android Studio` deve executar algumas tasks do *Gradle* para configurar o projeto, aguarde até finalizar. Ao finalizar as tasks, você pode executar o App 🏆 

## Desenvolvedores

{"\n".join(f"| [<img src='{dev['imagem']}' width=115><br><sub>{dev['nome']}</sub>]({dev['github']})" for dev in data["desenvolvedores"])} |
| :---: | :---: |
'''

print(formatted_text)


with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(formatted_text)


