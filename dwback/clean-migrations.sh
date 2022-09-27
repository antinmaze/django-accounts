find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

docker exec -i  postgres-db psql -U postgres <<EOF
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

DROP DATABASE diwidb;
DROP USER diwiuser;

CREATE DATABASE diwidb;
CREATE USER diwiuser WITH PASSWORD 'HelloDevWorld!';
ALTER ROLE diwiuser SET client_encoding TO 'utf8';
ALTER ROLE diwiuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE diwiuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE diwidb TO diwiuser;
\q
EOF

python manage.py makemigrations
python manage.py migrate

