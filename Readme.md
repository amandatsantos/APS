
---

# Sistema de Locação de Carros

Este é um sistema de locação de carros desenvolvido com Python utilizando a arquitetura **MVC (Model-View-Controller)**, com o backend utilizando **MySQL** como banco de dados.

## Funcionalidades
- **Login e Cadastro de Usuários**: Os usuários podem se cadastrar e fazer login no sistema para realizar reservas de carros.
- **Visualização de Carros Disponíveis**: A página inicial (home) permite a visualização de todos os carros disponíveis para locação.
- **Reserva de Carros**: Os usuários podem selecionar um carro disponível, definir o período da reserva e confirmar a locação.
- **Finalização de Reserva**: Após o período de locação, o usuário pode finalizar a reserva.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **MySQL**: Banco de dados para armazenar informações de carros, usuários e reservas.
- **Arquitetura MVC**: O sistema é organizado em três camadas principais:
  - **Model**: Gerencia os dados e a lógica de acesso ao banco de dados.
  - **View**: Interface para interação com o usuário (neste caso, via linha de comando).
  - **Controller**: Interage entre a Model e a View, realizando a lógica de negócio.
  
## Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado em sua máquina:

- **Python 3.x**
- **MySQL** (com um banco de dados configurado)
- **Bibliotecas Python**: Instale as dependências listadas no arquivo `requirements.txt`.

### Instalação das dependências
Instale as bibliotecas necessárias para rodar o projeto usando o pip:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Crie um banco de dados MySQL para o sistema de locação de carros e configure as credenciais de acesso no arquivo `config.py`. Exemplo de configuração:

```python
MYSQL_DATABASE = 'nome_do_banco'
MYSQL_USER = 'usuario'
MYSQL_PASSWORD = 'senha'
MYSQL_HOST = 'localhost'
```


## Estrutura do Projeto

```bash
.
├── controllers
│   ├── home_controller.py
│   ├── reservation_controller.py
│   └── user_controller.py
├── models
│   └── models.py
├── main.py
├── README.md
└── requirements.txt
```

### Principais Arquivos

- **main.py**: O arquivo principal para execução do sistema.
- **models/models.py**: Contém as interações com o banco de dados e as funções de lógica de negócio.
- **controllers/home_controller.py**: Controlador responsável por gerenciar a página inicial.
- **controllers/reservation_controller.py**: Controlador para gerenciar reservas de carros.
- **controllers/user_controller.py**: Controlador para gerenciar o login e cadastro de usuários.

## Como Executar o Projeto

### 1. Configurar o banco de dados

- Execute o script SQL fornecido para criar as tabelas necessárias no seu banco de dados MySQL.
- Configure suas credenciais MySQL no arquivo `config.py`.

### 2. Rodar o sistema

Execute o arquivo `main.py` para iniciar o sistema:

```bash
python main.py
```

### 3. Fluxo de uso

1. **Registrar usuário**: Selecione a opção `1` para criar uma nova conta de usuário.
2. **Login**: Selecione a opção `2` para fazer login.
3. **Ver carros disponíveis**: Após o login, use a opção `3` para visualizar os carros disponíveis para locação.
4. **Selecionar e reservar carro**: Selecione a opção `4` para escolher um carro e fazer a reserva, informando a data de início e fim da locação.
5. **Finalizar reserva**: Após o período de locação, selecione a opção `5` para finalizar a reserva.

## Como Testar o Projeto

Os testes podem ser executados para verificar a funcionalidade dos controladores e modelos. Certifique-se de ter os dados inseridos no banco de dados antes de testar.

Exemplo de comando para rodar testes:

```bash
python test_user_controller.py
python test_reservation_controller.py
```

## Melhorias Futuras

- Implementação de uma interface gráfica (GUI) para substituir a interface de linha de comando.
- Integração com APIs de terceiros para cálculo de rotas e tempo estimado de devolução do carro.
- Validações mais robustas para entrada de dados.

## Licença

Este projeto é de código aberto e licenciado sob os termos da licença MIT.

---

Com essa documentação, quem clonar o projeto terá informações claras sobre como configurar e rodar o sistema de locação de carros, além de instruções para executar e testar as funcionalidades.