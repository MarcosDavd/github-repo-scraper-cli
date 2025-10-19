import sys
import requests
import pyperclip

from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from pyperclip import PyperclipException

def main():
    gitUser = input("Ingresa el nombre de usuario de Github:")
    url = f"https://github.com/{gitUser}?tab=repositories"
    try:
        repos = requests.get(url)

        repos.raise_for_status()
        soup = BeautifulSoup(repos.text,'html.parser')
        repo_list = soup.select('ul li div div h3 a')  
        if not repo_list:
            print(f"⚠️  No se encontraron repositorios para el usuario '{gitUser}'")
            return
        print("Repositorios de "+gitUser)
        i=0
        print("\n=== Repositorios encontrados ===")
        list=[]
        for item in repo_list:
            href=item.get('href')
            print(f"--{i} repositorio: {href}")
            ssh = f"git@github.com:{href}.git"
            #https = f"https://github.com{href}.git"
            i=i+1
            list.append(ssh)
        print("===============================\n")
        num = input("🔹 Ingresa el número del repositorio para obtener el SSH: ")
        command = f"git clone {list[int(num)]}"
        try:
            pyperclip.copy(command)
            print(f"✅ Comando copiado al portapapeles:\n{command}")
        except PyperclipException:
            print(f"⚠️ No se encontró ninguna herramienta de copy/paste. Usa el comando manualmente:\n{command}")
    except RequestException as e:
        print(f" ❌ Error de peticion  :{e}")
        sys.exit(1)
    except Exception as e:
        print(f" ❌ Error inesperado{e}")
