import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER
import mysql.connector
from datetime import datetime

#conexão_db
def connect_db():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


def create_tb():
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela de Usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        cpf_cnpj VARCHAR(20) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        idade INT NOT NULL,
        cnh VARCHAR(20) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        password VARCHAR(255) NOT NULL
    )''')

    # Tabela de Carros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INT AUTO_INCREMENT PRIMARY KEY,
        chassi VARCHAR(50) NOT NULL UNIQUE,
        modelo VARCHAR(255) NOT NULL,
        placa VARCHAR(20) NOT NULL UNIQUE,
        ano INT NOT NULL,
        cor VARCHAR(50) NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        quilometragem FLOAT NOT NULL,
        disponivel BOOLEAN NOT NULL
    )''')

    # Tabela de Reservas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        car_id INT,
        data_inicio DATE NOT NULL,
        data_final DATE NOT NULL,
        valor FLOAT NOT NULL,
        status BOOLEAN NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(car_id) REFERENCES cars(id)
    )''')

    conn.commit()
    conn.close()

    # Função para inserir dados iniciais
def seed_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Adicionando usuários e carros iniciais
    cursor.execute("INSERT IGNORE INTO users (nome, cpf_cnpj, email, idade, cnh, endereco, telefone, password) VALUES ('Admin', '12345678900', 'admin@example.com', 30, '1234567890', 'Rua Exemplo, 123', '123456789', '1234')")
    cursor.execute("INSERT IGNORE INTO cars (chassi, modelo, placa, ano, cor, categoria, quilometragem, disponivel) VALUES ('ABC123', 'Carro A', 'XYZ-1234', 2020, 'Preto', 'Sedan', 15000, TRUE), ('DEF456', 'Carro B', 'XYZ-5678', 2021, 'Branco', 'SUV', 8000, TRUE)")

    conn.commit()
    conn.close()

# Função de autenticação de usuário
def authenticate_user(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def register_user(nome, cpf_cnpj, email, idade, cnh, endereco, telefone, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (nome, cpf_cnpj, email, idade, cnh, endereco, telefone, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (nome, cpf_cnpj, email, idade, cnh, endereco, telefone, password))
    conn.commit()
    conn.close()

# Função para obter carros disponíveis
def get_available_cars():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE disponivel = TRUE")
    cars = cursor.fetchall()
    conn.close()
    return cars

# Função para reservar um carro
def reserve_car(user_id, car_id, data_inicio, data_final, valor):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (user_id, car_id, data_inicio, data_final, valor, status) VALUES (%s, %s, %s, %s, %s, %s)", (user_id, car_id, data_inicio, data_final, valor, False))
    cursor.execute("UPDATE cars SET disponivel = FALSE WHERE id = %s", (car_id,))
    conn.commit()
    conn.close()

def get_car_by_id(car_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE id = %s", (car_id,))
    car = cursor.fetchone()
    conn.close()
    return car

def reserve_car(user_id, car_id, start_date, end_date, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (user_id, car_id, start_date, end_date, value, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, car_id, start_date, end_date, value, False))
    conn.commit()
    conn.close()

def finalize_reservation(reservation_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE reservations SET status = TRUE WHERE id = %s", (reservation_id,))
    conn.commit()
    conn.close()

def is_car_available(car_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM reservations WHERE car_id = %s AND status = FALSE AND (
            (start_date <= NOW() AND end_date >= NOW()) OR
            (start_date <= NOW() AND end_date >= NOW()) OR
            (start_date >= NOW() AND end_date <= NOW())
        )
    """, (car_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0