# Github-repo-scraper-cli
Herramienta de linea de comandos para obtener ssh del respositiorio de usuario ingresado por consola.El comando se copia automaticamente al portapapeles.
## Requerimientos para usuarios Linux
Como el comando es copiado al portapapeles pyperclip necesita un mecanismo de copy/paste es necesario instalarlo en caso de no tener uno.
Podemos hacer uso de alguno de las siguientes herramientas:
+ Para instalar xsel
```bash
sudo apt-get install xsel
```
+ Para instalar xclip
```bash
sudo apt-get install xclip
```
+ Para instalar el modulo gtk de Python 
```bash
pip install gtk
```
+ Para instalar el modulo PyQt4 de python
```bash
pip install PyQt4
```

## Instalacion 
No es necesario clonar el repositorio. Podemos hacer uso del siguiente comando para instalar todo y simplemente hacer uso del comando `ghclone` desde la terminal.

```bash
pip install git+https://github.com/MarcosDavd/github-repo-scraper.git
```
