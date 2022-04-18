# Database indexing in PostgreSQL

## Index

* indexes are a cost storage/time trade-off 
* basically save work by doing it once
    - during `INSERT` or `UPDATE`
* based on actual DB usage (queries)
    - `WHERE`
    - `ORDER BY`
* TANSTAAFL / NEJÍZDA
    - as usual in IT
    - in almost all areas

## Indexes and tables

* table
    - sequence of pages
    - 8kB per page
* index
    - basically key:value-type storage
    - mapping (value1, value2, ...) -> (page, rowID)
    - i.e. index contain real/live data!
        - some queries performed just against index(es)
    - it's sorted! (stored in B-tree usually)
        - `ORDER BY` "for free"
    - small index (in bytes)
        - fewer pages to access

- every primary key has an index (usually B-tree)

## Index as data structure
- Bitmap index
- B-tree
- Log-structured merge-tree (LSM tree)

### Bitmap index
- work well for low-cardinality columns

### B-tree data structure

### Log-structured merge-tree data structure

## Index stored in physical file

create index idx_foo on bar(id);
select relfilenode from pg_class wheren relname like `idx_foo`;

$PGDATA/xyz/xyz

## How to check if/how index is used

EXPLAIN SELECT name FROM bar WHERE id = 1234;

## B-tree
create index idx_foo on bar using BTREE(id);

## Useful links

* Database index (Wikipedia) 
  [https://en.wikipedia.org/wiki/Database\_index](https://en.wikipedia.org/wiki/Database_index)

* B-tree (Wikipedia) 
  [https://en.wikipedia.org/wiki/B-tree](https://en.wikipedia.org/wiki/B-tree)

* Log-structured merge-tree 
  [https://en.wikipedia.org/wiki/Log-structured\_merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree)

* Database Indexing Explained (with PostgreSQL) 
  [https://www.youtube.com/watch?v=-qNSXK7s7\_w](https://www.youtube.com/watch?v=-qNSXK7s7_w)

* Lesson #3 - How to Create Indexes? - Deep Dive Into PostgreSQL Indexes Course 
  [https://www.youtube.com/watch?v=bBxeBxnLl\_4](https://www.youtube.com/watch?v=bBxeBxnLl_4)

* Is SELECT * Expensive? 
  [https://www.youtube.com/watch?v=QQVNVOneZNg](https://www.youtube.com/watch?v=QQVNVOneZNg)
