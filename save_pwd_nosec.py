import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_FILE = os.path.join(BASE_DIR, "vault.json")

def save_password(name, password):
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, 'r') as file:
            data = json.load(file)
    
    else:
        data = {}
    
    data[name] = password

    with open(VAULT_FILE, 'w') as file:
        json.dump(data, file)

def load_password():
    if not os.path.exists(VAULT_FILE):
        return {}
        
    with open(VAULT_FILE, 'r') as file:
        return json.load(file)
        

if __name__ == "__main__":
    while True:
        cmd = input("Enter command (add/list/exit): ").strip().lower()
        if cmd == "add":
            name = input("Enter Service Name: ").strip()
            pwd = input("Enter Password: ").strip()
            save_password(name, pwd)
        elif cmd == "list":
            print(load_password())
        elif cmd == "exit":
            break
