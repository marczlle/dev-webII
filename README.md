# Microsserviço FastAPI com Nginx Load Balancer

Este projeto é um exemplo de microsserviço em **FastAPI** para multiplicação (`/mult`) com balanceamento de carga via Nginx, incluindo réplicas e container de backup.
Caso o container mult1 caia, o tráfego é enviado para mult2.
Caso ambos os containers principais caiam, o tráfego é enviado para mult_backup.

---
## Rodando o projeto

1. Tenha instalado na sua máquina **Docker** e **Docker Compose**.
2. No terminal, vá para a pasta "mult/" do projeto.
3. Suba os containers:
    ```docker-compose up --build```
4. Acessando o endpoint de mutiplicação:

    GET: http://localhost:8080/mult?op1=2&op2=3

    POST:

    POST http://localhost:8080/mult
    {
    "op1": 7,
    "op2": 9
    }

5. Parar o projeto:
    ```docker-compose down```


