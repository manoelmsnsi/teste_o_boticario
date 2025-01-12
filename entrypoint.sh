#!/bin/bash
set -e

echo "Aguardando 20s -> PostgreSQL iniciar..."
sleep 20

# Função para criar o banco de dados
function create_database() {
    echo "Criando o banco de dados 'teste_manoel'..."


    DB_USER=$(echo $DATABASE_URL | cut -d':' -f2 | cut -d'/' -f3)
    DB_PASSWORD=$(echo $DATABASE_URL | cut -d':' -f3 | cut -d'@' -f1)
    DB_HOST=$(echo $DATABASE_URL | cut -d'@' -f2 | cut -d':' -f1)
    DB_PORT=$(echo $DATABASE_URL | cut -d':' -f4 | cut -d'/' -f1)
    DB_NAME=$(echo $DATABASE_URL | cut -d'/' -f4)
    # PARA DEBUG
    # echo $DB_USER
    # echo $DB_PASSWORD
    # echo $DB_HOST
    # echo $DB_PORT
    # echo $DB_NAME
    PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d postgres -c "SELECT 1 FROM pg_database WHERE datname = 'teste_manoel'" | grep -q 1 || PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d postgres -c "CREATE DATABASE teste_manoel"
}


# Cria o banco de dados
create_database
# Executa as migrações do Alembic
alembic upgrade head
# Inicia a aplicação
exec "$@"
