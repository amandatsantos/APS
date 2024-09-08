import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import register_user, authenticate_user, create_tb

class UserController:
    def __init__(self):
       create_tb()
    
    def register_user(self, nome, cpf_cnpj, email, idade, cnh, endereco, telefone, senha):
        # Aqui você pode adicionar validações adicionais
        register_user(nome, cpf_cnpj, email, idade, cnh, endereco, telefone, senha)
        print(f"Usuário {nome} registrado com sucesso.")
    
    def login(self, email, senha):
        user = authenticate_user(email, senha)
        if user:
            print(f"Login bem-sucedido. Bem-vindo, {user[1]}.")
        else:
            print("Credenciais inválidas.")