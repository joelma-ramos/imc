 E-Shop Brasil – Solução Big Data e Banco de Dados NoSQL

 Introdução

A E-Shop Brasil é uma das maiores plataformas de e-commerce do país, com mais de 5 milhões de clientes ativos e uma média de 100 mil pedidos por dia. 
Diante do crescimento exponencial de dados, a empresa enfrenta desafios relacionados à:

- Gestão eficiente de dados;
- Personalização da experiência do cliente;
- Otimização logística e controle de estoque;
- Garantia de segurança e privacidade dos dados.

Objetivos do Projeto

Este projeto visa propor uma aplicação prática com foco nas seguintes metas:

- Utilizar banco de dados NoSQL (MongoDB) para armazenar e manipular grandes volumes de dados não estruturados.
- Criar uma interface interativa com Streamlit para gestão e visualização de dados.
- Containerizar a solução usando Docker para facilitar implantação e escalabilidade.
- Simular funcionalidades úteis para marketing, logística e análise de comportamento de clientes.


Descrição do Projeto

Tecnologias Utilizadas

- **MongoDB: Banco NoSQL para armazenar dados de clientes, pedidos e navegação.
- **Streamlit: Interface web interativa para análise de dados.
- **Docker/Docker Compose:** Ambientes isolados e padronizados.

Funcionalidades da Aplicação

A aplicação `app.py` permite:

- Inserção de novos dados de usuários, pedidos e comportamentos.
- Consulta e filtragem de dados do MongoDB.
- Simulação de personalização de recomendações com base no histórico de navegação.
- Visualização de dados logísticos (tempo de entrega, estoque por região, etc).


Estrutura de Containers

MongoDB Container: Armazena os dados dos clientes e operações.

App Container: Executa a interface Streamlit e conecta ao MongoDB via `pymongo`.

docker-compose up
docker build -t eshop-app .
docker run -p 8501:8501 eshop-app

{
  "nome": "Maria Silva",
  "email": "maria@example.com",
  "historico_navegacao": ["notebook", "smartphone"],
  "compras": [ {"produto": "Notebook Dell", "valor": 4500, "data": "2025-04-10"}
  ]
}

{
  "regiao": "Norte",
  "estoque_disponivel": 350,
  "tempo_medio_entrega": 6
}
- `docker-compose.yml`
- `Dockerfile`
- `app.py` (com inserção e leitura de dados do MongoDB)
- `requirements.txt`

