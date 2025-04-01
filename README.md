# API de Restaurantes com Python

## Descrição do Projeto

Este projeto foi desenvolvido para consumir uma API externa de restaurantes e exibir os cardápios de diferentes estabelecimentos. Utilizando **Python**, **FastAPI** para criar a API, e **Requests** para fazer as requisições HTTP, o objetivo é permitir que os usuários consultem informações sobre os cardápios dos restaurantes em formato **JSON**.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para criar APIs rápidas e eficientes.
- **Requests**: Biblioteca para consumir APIs externas.
- **JSON**: Formato de dados utilizado para armazenar as informações.
- **Uvicorn**: Servidor ASGI utilizado para rodar a aplicação FastAPI.

## Funcionalidades

### **Script de Consumo de API** (`app.py`)
   - Consome a API externa (`https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`).
   - Armazena as informações de cardápios em arquivos `.json` separados por restaurante.

### **API FastAPI** (`main.py`)
   - **`GET /api/hello`**: Retorna uma mensagem simples de boas-vindas.
   - **`GET /api/restaurantes/`**: Exibe todos os cardápios de todos os restaurantes ou filtra por restaurante específico com o parâmetro `restaurante`.

---

## Como Rodar o Projeto

### 1. **Clone o Repositório**
Clone o repositório para a sua máquina local utilizando o comando:

```bash
git clone https://github.com/rafaelmunetiko/RestaurantesAPI
```

### 2. **Crie o Ambiente Virtual (venv)**
É recomendável criar um ambiente virtual para garantir que as dependências sejam isoladas e não afetem outros projetos:

```bash
python -m venv venv
```

### 3. **Ative o Ambiente Virtual**
Ative o ambiente virtual.

```bash
.\venv\Scripts\activate
```

### 4. **Instale as Dependências**
Entre no diretório do projeto e instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. **Rodando o Script app.py**

Este script consome a API externa e gera os arquivos `.json` contendo os cardápios. Para rodá-lo, utilize:

```bash
python app.py
```

### 6. **Rodando a API com FastAPI**

Para rodar a API localmente, use o Uvicorn:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### Exemplos de Endpoints da API

## 1. **GET /api/hello**
Retorna uma mensagem simples de boas-vindas.

Resposta:

```json
{
  "Hello": "World"
}
```

## 2. **GET /api/restaurantes/**
Retorna todos os cardápios de todos os restaurantes.

Resposta:

```json
{
  "Dados": [
    {
      "Company": "McDonald's",
      "Item": "Hamburger",
      "price": "R$ 32,42",
      "description": "Uma explosão de sabores em cada mordida."
    },
    {
      "Company": "KFC",
      "Item": "Limited Time Cinnabon Dessert Biscuits",
      "price": "R$ 58,53",
      "description": "Uma explosão de sabores em cada mordida."
    }
  ]
}
```

## 3. **GET /api/restaurantes/?restaurante=McDonald's**
Retorna o cardápio de **McDonald's**.

Resposta:

```json
{
  "Restaurante": "McDonald's",
  "Cardapio": [
    {
      "item": "Hamburger",
      "price": "R$ 32,42",
      "description": "Uma explosão de sabores em cada mordida."
    },
    {
      "item": "Cheeseburger",
      "price": "R$ 38,81",
      "description": "Uma opção saudável e equilibrada."
    },
    {
      "item": "Double Cheeseburger",
      "price": "R$ 50,18",
      "description": "Leve e saboroso, perfeito a qualquer hora."
    }
  ]
}
```

## 4. **GET /api/restaurantes/?restaurante=KFC**
Retorna o cardápio de **KFC**.

Resposta:

```json
{
  "Restaurante": "KFC",
  "Cardapio": [
    {
      "item": "Limited Time Cinnabon Dessert Biscuits",
      "price": "R$ 58,53",
      "description": "Uma explosão de sabores em cada mordida."
    },
    {
      "item": "Limited Time ORIGINAL RECIPE CHICKEN Chicken Breast",
      "price": "R$ 45,72",
      "description": "Sabores autênticos que aquecem o coração."
    },
    {
      "item": "Limited Time ORIGINAL RECIPE CHICKEN Chicken Limited Time Drumstick",
      "price": "R$ 30,51",
      "description": "Sabores autênticos que aquecem o coração."
    }
  ]
}
```

---

## Melhorias Futuras e Ideias para Expansão

**Autenticação e Autorização:** Implementar um sistema de autenticação para controlar o acesso à API.

**Banco de Dados:** Integrar um banco de dados para armazenar os cardápios de maneira mais escalável.

**Filtragem Avançada:** Adicionar filtros para pesquisar cardápios por preço, tipo de comida, ou localização dos restaurantes.

**Frontend:** Criar uma interface gráfica para tornar a visualização do cardápio mais interativa.

**Deploy:** Hospedar a API em plataformas como Heroku, AWS, ou Azure para acessibilidade pública.

## Link para o Repositório no GitHub
## [Clique aqui para acessar o repositório](https://github.com/rafaelmunetiko/RestaurantesAPI)
