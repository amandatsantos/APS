from models import  create_tb, seed_data, authenticate_user, get_available_cars, reserve_car

create_tb()
print("tabela criada")

seed_data()
print("Dados iniciais inseridos com sucesso.")

user = authenticate_user('admin@example.com', '1234')
print("Usuário autenticado:", user)


cars = get_available_cars()
print("Carros disponíveis:", cars)

# Verifique o estado antes da reserva
print("Antes da reserva:", get_available_cars())

# Faça uma reserva
reserve_car(1, 1, '2024-09-10', '2024-09-15', 100.00)

# Verifique o estado após a reserva
print("Após a reserva:", get_available_cars())