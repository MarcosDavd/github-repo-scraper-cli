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
## Instalacion rapida(no git clone)
```bash 
pipx install --editable git+https://github.com/MarcosDavd/github-repo-scraper-cli.git
```

## Instalacion paso a paso(recomendable)
* Clonar el repositorio
    * HTTPS
    ```bash
    git clone https://github.com/MarcosDavd/github-repo-scraper-cli.git
    ```
    * SSH
    ```bash
    git clone git@github.com:MarcosDavd/github-repo-scraper-cli.git 
    ```
* Moverse a la carpeta del repositorio
```bash 
cd github-repo-scraper-cli
```
* Instalar pipx
```bash
python3 -m pip install --user pipx
```
```bash
python3 -m pipx ensurepath
```
* Instalar en modo editable

```bash
pipx install --editable .

```
## Como usar
Una vez instalado podemos usar el comando `ghclone` desde la terminal.
* Comando
```bash
ghclone
```

