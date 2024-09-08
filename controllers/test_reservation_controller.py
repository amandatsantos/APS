from reservations_controller import ReservationController

def test_reservation_controller():
    controller = ReservationController()
    
    # Teste de registro de empréstimo
    controller.registrarEmprestimo('2024-09-10', '2024-09-15', 1, 1)
    
    # Teste de consulta de empréstimo
    controller.consultarEmprestimo(1)
    
    # Teste de finalização de empréstimo
    controller.finalizarEmprestimo(1)

    # Teste de cálculo de valor
    valor = controller.calculoEmprestimo('2024-09-10', '2024-09-15')
    print(f"Valor calculado: {valor}")

# Executar o teste
test_reservation_controller()
