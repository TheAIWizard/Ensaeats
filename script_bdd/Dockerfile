FROM postgres 
ENV POSTGRES_PASSWORD postgres 
ENV POSTGRES_DB SCRIPT_SQL_BDD
COPY script_sql_bdd.sql /docker-entrypoint-initdb.d/
