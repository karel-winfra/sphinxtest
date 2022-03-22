import os
from livereload import Server, shell

carpetas = [
    "puesta_en_marcha",
    "winfra_cliente"
]


if __name__ == '__main__':
    server = Server()

    for carpeta_raiz in carpetas:
        for root, carpeta, fichero in os.walk(carpeta_raiz):
            server.watch(os.path.join(root, '*.md'), shell('make.bat html'), delay=1)

    server.watch('*.py', shell('make.bat html'), delay=1)

    server.watch('_static/*', shell('make.bat html'), delay=1)
    server.watch('_templates/*', shell('make.bat html'), delay=1)
    server.serve(root='_build/html')
