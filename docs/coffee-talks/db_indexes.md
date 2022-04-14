# Database indexing in PostgreSQL

## Index
- 
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

Database index (Wikipedia)
https://en.wikipedia.org/wiki/Database_index

B-tree (Wikipedia)
https://en.wikipedia.org/wiki/B-tree

Log-structured merge-tree
https://en.wikipedia.org/wiki/Log-structured_merge-tree

Database Indexing Explained (with PostgreSQL)
https://www.youtube.com/watch?v=-qNSXK7s7_w

Lesson #3 - How to Create Indexes? - Deep Dive Into PostgreSQL Indexes Course
https://www.youtube.com/watch?v=bBxeBxnLl_4
