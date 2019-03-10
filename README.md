# Projeto de CRUD com Flask, sqlalchemy e marshmallow

# Dependências
```sh
pip install -r requirements.txt
```

# Como rodar esse Projeto
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

# Migrações
```sh
flask db init
flask db migrate
flask db upgrade
```