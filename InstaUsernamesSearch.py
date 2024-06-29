__author__ = "NetMalware"
__license__ = "Apache"

import requests

def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200 and 'profilePage_' in response.text:
        return True
    else:
        return False

def main():
    while True:
        username = input('''Search the User or type ":quit" to keep up: ''').strip()
        if username.lower() == 'sair':
            break

        if check_username_availability(username):
            print(f"Ops! That user already exists!")
        else:
            print(f"Private or not exists 7w7")

if __name__ == "__main__":
    main()
