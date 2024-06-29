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
        username = input("Digite o nome de usuário que deseja verificar (ou 'sair' para sair): ").strip()
        if username.lower() == 'sair':
            break

        if check_username_availability(username):
            print(f"O perfil '{username}' existe no Instagram.")
        else:
            print(f"O perfil '{username}' não existe ou é privado.")

if __name__ == "__main__":
    main()
