# Github-repo-scraper-cli
Herramienta de linea de comandos para obtener ssh del respositiorio de usuario ingresado por consola.El comando se copia automaticamente al portapapeles.
## Requerimientos para usuarios Linux
Como el comando es copiado al portapapeles pyperclip necesita un mecanismo de copy/paste. En caso de no tener ninguna simplemente se mostrara el comando en consola.

Opcionalemente podemos hacer uso de alguna de las siguientes herramientas:
* Para instalar xsel
```bash
sudo apt-get install xsel
```
* Para instalar xclip
```bash
sudo apt-get install xclip
```
* Para instalar el modulo gtk de Python 
```bash
pip install gtk
```
* Para instalar el modulo PyQt4 de python
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
sudo apt install pipx
```
Esto es en el directorio del proyecto
```bash
pipx ensurepath
```
* Instalar en modo editable

```bash
pipx install --editable .

```
### En caso de tener problemas con el path
```bash
githubScraper$ pipx install --editable . installed package github-repo-scraper-cli 0.1.0, installed using Python 3.12.3 These apps are now globally available - ghclone ⚠️ Note: '/home/davo/.local/bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is updated. Run pipx ensurepath to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc). done! ✨ 🌟 ✨
```
Debemos seguir los siguientes pasos para agregarlo
* Añadir ruta al path

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```
En caso de usar Zsh

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```
* Aplicar cambios
```bash
source ~/.bashrc
```
En caso de usar Zsh
```bash
source ~/.zshrc
```
* por ultimo verificamos
```bash
which ghclone
```
Deberiamos tener una salida tipo
```bash
/home/host/.local/bin/ghclone
```
## Como usar
Una vez instalado podemos usar el comando `ghclone` desde la terminal.
* Comando
```bash
ghclone
```

