# SchemaSpy

A Java-based tool that with the aid of Graphviz can generate a rough
documentation for existing database as a collection of interlinked HTML pages

## Installation

1. Download SchemaSpy Java archive from [https://github.com/schemaspy/schemaspy/releases/tag/v6.1.0](https://github.com/schemaspy/schemaspy/releases/tag/v6.1.0)
1. Download JDBC driver for PostgreSQL from [https://jdbc.postgresql.org/download.html](https://jdbc.postgresql.org/download.html)

Both Java archives (JARs) needs to be stored in the same directory!

## Usage

In order to run SchemaSpy against selected database, a lot of parameters needs to be specified:

* `-t` database type
* `-u` user name (who has access to database)
* `-p` password
* `-host` hostname where PostgreSQL runs (port is optional)
* `-s` schema name
* `-o` output diretory
* `-db` database name
* `-dp` path to JDBC driver (a JAR file)

### An example of SchemaSpy invocation

```
java -jar schemaspy-6.1.0.jar -cp . -t pgsql -u postgres -p postgres -host localhost -s public -o test1 -db test1 -dp postgresql-42.2.20.jre7.jar
```

## Practical examples

Database schemes inspired by [Employees Test Database](https://github.com/cristiscu/employees-test-database)

### Tables without primary keys nor foreign keys

```sql
CREATE TABLE department (
   ID       integer NOT NULL,
   name     varchar(20) NOT NULL,
   location varchar(20) NOT NULL
);

CREATE TABLE employee (
   ID         integer NOT NULL,
   name       varchar(20) NOT NULL,
   job        varchar(20) NOT NULL,
   manager    integer,
   hiredate   date NOT NULL,
   salary     integer NOT NULL,
   comment    integer,
   department integer NOT NULL
);

CREATE TABLE project (
   ID        integer NOT NULL,
   employee  integer NOT NULL,
   startdate date NOT NULL,
   enddate   date NOT NULL
);
```

Construct new database and create all tables in that database:

```
psql -U postgres
create database test1
\c test1
\i db1.sql
\dt
\d employee
\d department
\d project
\q
```

Generate HTML pages with database description:

```
java -jar schemaspy-6.1.0.jar -cp . -t pgsql -u postgres -p postgres -host localhost -s public -o test1 -db test1 -dp postgresql-42.2.20.jre7.jar
```

Results can be seen [here](./schemaspy/db1/index.html)



### Tables with primary keys, but without foreign keys

```sql
CREATE TABLE department (
   ID       serial PRIMARY KEY,
   name     varchar(20) NOT NULL,
   location varchar(20) NOT NULL
);

CREATE TABLE employee (
   ID         serial PRIMARY KEY,
   name       varchar(20) NOT NULL,
   job        varchar(20) NOT NULL,
   manager    integer,
   hiredate   date NOT NULL,
   salary     integer NOT NULL,
   comment    integer,
   department integer NOT NULL
);

CREATE TABLE project (
   ID        serial PRIMARY KEY,
   employee  integer NOT NULL,
   startdate date NOT NULL,
   enddate   date NOT NULL
);
```

Construct new database and create all tables in that database:

```
psql -U postgres
create database test2
\c test2
\i db2.sql
\dt
\d employee
\d department
\d project
\q
```

Generate HTML pages with database description:

```
java -jar schemaspy-6.1.0.jar -cp . -t pgsql -u postgres -p postgres -host localhost -s public -o test2 -db test2 -dp postgresql-42.2.20.jre7.jar
```

Results can be seen [here](./schemaspy/db2/index.html)



### Tables with primary keys and also foreign keys

```sql
CREATE TABLE department (
   ID       integer NOT NULL,
   name     varchar(20) NOT NULL,
   location varchar(20) NOT NULL,
   
   PRIMARY KEY (ID)
);

CREATE TABLE employee (
   ID         integer NOT NULL,
   name       varchar(20) NOT NULL,
   job        varchar(20) NOT NULL,
   manager    integer,
   hiredate   date NOT NULL,
   salary     integer NOT NULL,
   comment    integer,
   department integer NOT NULL,
   
   PRIMARY KEY (ID),
   CONSTRAINT fk_manager FOREIGN KEY (manager) REFERENCES employee (ID)
      ON DELETE SET NULL
      ON UPDATE CASCADE,
   CONSTRAINT fk_department FOREIGN KEY (department) REFERENCES department (ID)
      ON DELETE RESTRICT
      ON UPDATE NO ACTION
);

CREATE TABLE project (
   ID        integer NOT NULL,
   employee  integer NOT NULL,
   startdate date NOT NULL,
   enddate   date NOT NULL,
   
   PRIMARY KEY (ID),
   CONSTRAINT fk_project FOREIGN KEY (employee) REFERENCES employee (ID)
      ON DELETE NO ACTION
      ON UPDATE CASCADE
);
```

Construct new database and create all tables in that database:

```
psql -U postgres
create database test2
\c test2
\i db2.sql
\dt
\d employee
\d department
\d project
\q
```

Generate HTML pages with database description:

```
java -jar schemaspy-6.1.0.jar -cp . -t pgsql -u postgres -p postgres -host localhost -s public -o test3 -db test3 -dp postgresql-42.2.20.jre7.jar
```

Results can be seen [here](./schemaspy/db3/index.html)



## Useful links

* [SchemaSpy home page](http://schemaspy.org/)
* [SchemaSpy on PostgreSQL wiki](https://wiki.postgresql.org/wiki/SchemaSpy)
* [SchemaSpy download page](https://github.com/schemaspy/schemaspy/releases/tag/v6.1.0)
* [JDBC driver for PostgreSQL](https://jdbc.postgresql.org/download.html)
* [Employees Test Database](https://github.com/cristiscu/employees-test-database)
