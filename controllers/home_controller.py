from models.models import get_available_cars

class HomeController:
    def __init__(self):
        pass

    def display_home(self):
        cars = get_available_cars()
        if cars:
            print("Carros disponíveis:")
            for car in cars:
                print(f"ID: {car[0]} | Modelo: {car[1]} | Placa: {car[2]} | Ano: {car[3]} | Cor: {car[4]} | Quilometragem: {car[5]}")
        else:
            print("Nenhum carro disponível no momento.")
    
    def select_car(self, car_id):
        # Aqui você pode implementar a lógica para selecionar um carro e, por exemplo, iniciar o processo de reserva.
        print(f"Você selecionou o carro com ID: {car_id}")