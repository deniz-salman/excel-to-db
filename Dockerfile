FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=dtbspss

COPY init.sql /docker-entrypoint-initdb.d/

RUN echo "[mysqld]\ndefault_authentication_plugin=mysql_native_password" >> /etc/mysql/my.cnf