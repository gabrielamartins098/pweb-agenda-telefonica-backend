Sistema de Gestão de Contactos – API REST

Projeto desenvolvido com Django REST Framework no backend e Vue 3 no frontend para gestão de contactos, municípios e províncias, com autenticação JWT.

Funcionalidades
Gestão de Contactos
Gestão de Municípios
Gestão de Províncias
Autenticação JWT por usuário
Filtragem e pesquisa de contactos por nome ou telefone

Endpoints Principais da API
Autenticação
+ POST /api/token/ : Realiza login e retorna token JWT
+ POST /api/token/refresh/ : Actualiza o token JWT

Contactos
+ GET /api/contactos/ : Listar contactos do usuário logado
+ POST /api/contactos/ : Criar contacto
+ PUT /api/contactos/{id}/ : Actualizar contacto
+ DELETE /api/contactos/{id}/ : Excluir contacto

Municípios
+ GET /api/municipios/ : Listar municípios
+ POST /api/municipios/ : Criar município
+ PUT /api/municipios/{id}/ : Actualizar município
+ DELETE /api/municipios/{id}/ : Excluir município

Províncias
+ GET /api/provincias/ : Listar províncias
+ POST /api/provincias/ : Criar província
+ PUT /api/provincias/{id}/ : Actualizar província
+ DELETE /api/provincias/{id}/ : Excluir província

Tecnologias

Backend: Python, Django, Django REST Framework, SQLite, JWT
Frontend: Vue 3, Vite, Pinia, TailwindCSS

Execução do Projeto
Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Frontend
npm install
npm run dev

Acesso
Frontend: http://localhost:5173
Backend: http://127.0.0.1:8000

Observações
Todos os endpoints de criação, actualização e exclusão exigem autenticação JWT.
Os contactos são sempre vinculados ao usuário logado.

A listagem de contactos permite pesquisa por nome ou telefone.

Cada município pertence a uma província.

Licença

MIT License