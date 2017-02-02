#!/bin/sh

MYSQL=mysql

MAIN_DB=sqlalchemy_test

MAIN_DB_SQL=db/sqlalchemy_test.sql

if [ $# -ne 1 ]; then
    printf "Enter MySQL Password> "
    stty -echo
    read PASSWORD
    stty echo
else
    PASSWORD=$1
fi

RESET_SQL="
drop schema if exists $MAIN_DB;
create schema if not exists $MAIN_DB;
grant all on $MAIN_DB.* to 'sqlalchemy_test'@'localhost' identified by 'pa55w0rd';
grant all on $MAIN_DB.* to 'sqlalchemy_test'@'192.168.%.%' identified by 'pa55w0rd';
"

echo "$RESET_SQL" | $MYSQL -u root --password=$PASSWORD
$MYSQL -u root --password=$PASSWORD $MAIN_DB < $MAIN_DB_SQL

echo "\ndone"
