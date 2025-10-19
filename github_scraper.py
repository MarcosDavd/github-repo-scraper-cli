import sys
import requests
import pyperclip

from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def main():
    gitUser = input("Ingresa el nombre de usuario de Github:")
    url = f"https://github.com/{gitUser}?tab=repositories"
    try:
        repos = requests.get(url)

        repos.raise_for_status()
        soup = BeautifulSoup(repos.text,'html.parser')
        repo_list = soup.select('ul li div div h3 a')  
        print("Repositorios de "+gitUser)
        i=0
        list=[]
        for item in repo_list:
            href=item.get('href')
            print(f"{i} repositorio: {href}")
            ssh = f"git@github.com:{href}.git"
            #https = f"https://github.com{href}.git"
            i=i+1
            list.append(ssh)
        num = input("Ingresa el numero de repositorio para obetener el SSH :")
        command = f"git clone {list[int(num)]}"
        pyperclip.copy(command)
        print("El comando se copio al portapapeles !!")
    except RequestException as e:
        print(f"Error de peticion :{e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado{e}")
