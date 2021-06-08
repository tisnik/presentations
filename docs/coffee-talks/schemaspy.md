# SchemaSpy

A Java-based tool that with the aid of Graphviz can generate a rough
documentation for existing database as a collection of interlinked HTML pages

## Installation

1. Download SchemaSpy Java archive from https://github.com/schemaspy/schemaspy/releases/tag/v6.1.0
1. Download JDBC driver for PostgreSQL from https://jdbc.postgresql.org/download.html

Both Java archives (JARs) needs to be stored in the same directory!

## Usage

In order to run SchemaSpy against selected database, a lot of parameters needs to be specified

* `-t` database type
* `-u` user name (who has access to database)
* `-p` password
* `-host` hostname where PostgreSQL runs (port is optional)
* `-o` output diretory
* `-dp` path to JDBC driver (a JAR file)

### An example of SchemaSpy invocation

```
```

## Practical examples

Database schemes inspired by ...

### Tables without primary keys nor foreign keys

```sql
```

Construct new database and create all tables in that database:

```
```

Generate HTML pages with database description:

```
```

Results can be seen [here](./schemaspy/db1/index.html)



### Tables with primary keys, but without foreign keys

```sql
```

Construct new database and create all tables in that database:

```
```

Generate HTML pages with database description:

```
```

Results can be seen [here](./schemaspy/db2/index.html)



### Tables with primary keys and also foreign keys

```sql
```

Construct new database and create all tables in that database:

```
```

Generate HTML pages with database description:

```
```

Results can be seen [here](./schemaspy/db3/index.html)



## Useful links

* SchemaSpy home page: http://schemaspy.org/ 
* SchemaSpy on PostgreSQL wiki: https://wiki.postgresql.org/wiki/SchemaSpy
* SchemaSpy download page: https://github.com/schemaspy/schemaspy/releases/tag/v6.1.0
* JDBC driver for PostgreSQL: https://jdbc.postgresql.org/download.html
