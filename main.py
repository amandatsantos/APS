from controllers.user_controller import UserController
from controllers.home_controller import HomeController

def main():
    user_controller = UserController()
    home_controller = HomeController()
    
    while True:
        print("1. Registrar")
        print("2. Login")
        print("3. Ver Carros Disponíveis")
        print("4. Selecionar Carro")
        print("5. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            nome = input("Nome: ")
            cpf_cnpj = input("CPF/CNPJ: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            cnh = input("CNH: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            senha = input("Senha: ")
            user_controller.register_user(nome, cpf_cnpj, email, idade, cnh, endereco, telefone, senha)
        
        elif choice == '2':
            cpf_cnpj = input("CPF/CNPJ: ")
            senha = input("Senha: ")
            user_controller.login(cpf_cnpj, senha)
        
        elif choice == '3':
            home_controller.display_home()
        
        elif choice == '4':
            car_id = input("Digite o ID do carro que deseja selecionar: ")
            home_controller.select_car(car_id)
        
        elif choice == '5':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()