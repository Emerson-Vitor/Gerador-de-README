#!/usr/bin/env python

import os
import sys

def create_component(name):
    component_path = f"./src/components/{name}_component.py"
    pub_components_path = "./pub_components.json"

    # Criar arquivo de componente
    with open(component_path, "w") as f:
        f.write(f'''
class {name.capitalize()}:
    def __init__(self):
        pass
    
    def render(self):
        return None
''')

    with open(pub_components_path, "rb+") as arquivo:

        text=f''',
    "{name}": {{
        "import": "./src/components/",
        "label": "{name.capitalize()}"
    }}
}}'''

        arquivo.seek(-1, 2)
        

        while arquivo.read(1) != b'}':
            arquivo.seek(-2, 1)
        arquivo.seek(-2, 1)
        
        inicio_ultima_linha = arquivo.tell()
        arquivo.seek(inicio_ultima_linha)
        arquivo.write(text.encode('utf-8'))

        

def initialize_project():

    os.makedirs("./src/components", exist_ok=True)
    open("./pub_components.json", "a").close()
    with open("./pub_components.json", 'w') as f:
        f.write('''
{
                
}
                ''')


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "create" and sys.argv[2] == "component":
        create_component(sys.argv[3])
    elif command == "init":
        initialize_project()

