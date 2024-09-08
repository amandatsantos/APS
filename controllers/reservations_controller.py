import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.models import connect_db, get_available_cars, reserve_car
from datetime import datetime

class ReservationController:
    def __init__(self):
        self.data_inicio = None
        self.data_final = None
        self.valor = 0.0
        self.status = False
    
    def registrarEmprestimo(self, data_inicio, data_final, user_id, car_id):
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.valor = self.calculoEmprestimo(data_inicio, data_final)
        self.status = False
        reserve_car(user_id, car_id, data_inicio, data_final, self.valor)
        print(f"Reserva registrada: {data_inicio} a {data_final} com valor de {self.valor}")

    def consultarEmprestimo(self, dado):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations WHERE id = %s", (dado,))
        reserva = cursor.fetchone()
        conn.close()
        if reserva:
            print(f"Reserva encontrada: {reserva}")
        else:
            print("Reserva não encontrada.")

    def finalizarEmprestimo(self, reserva_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE reservations SET status = TRUE WHERE id = %s", (reserva_id,))
        conn.commit()
        conn.close()
        print(f"Reserva com ID {reserva_id} finalizada.")

    def calculoEmprestimo(self, data_inicio, data_final):
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        data_final = datetime.strptime(data_final, '%Y-%m-%d')
        dias = (data_final - data_inicio).days
        valor_diario = 50.0  # valor diário fixo para simplificação
        return dias * valor_diario

    def getDataIni(self):
        return self.data_inicio

    def setDataIni(self, data_inicio):
        self.data_inicio = data_inicio

    def getDataFim(self):
        return self.data_final

    def setDataFim(self, data_final):
        self.data_final = data_final

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status