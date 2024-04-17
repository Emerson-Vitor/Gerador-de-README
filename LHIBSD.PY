
pub_components_path = "pub_components.json"
name = "logo"

with open(pub_components_path, "rb+") as arquivo:

    text=f'''
    "{name}": {{
        "import": "./src/components/",
        "label": "{name.capitalize()}"
    }}
}}
'''

    arquivo.seek(-1, 2)
    

    while arquivo.read(1) != b'}':
        arquivo.seek(-2, 1)
    arquivo.seek(-2, 1)
    
    inicio_ultima_linha = arquivo.tell()
    arquivo.seek(inicio_ultima_linha)
    arquivo.write(text.encode('utf-8'))

    


