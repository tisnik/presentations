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
    - stored as sequence of pages
    - 8kB per page
* index
    - basically key:value-type storage
    - mapping (value1, value2, ...) -> (page, rowID)
    - i.e. index contains real/live data!
        - some queries performed just against index(es)
    - it's sorted! (stored in B-tree usually)
        - `ORDER BY` "for free"
    - small index (in bytes)
        - fewer pages to access
        - usually cached
        - -> faster (a lot faster)



## Indexes and tables size comparison

* an example taken from documentation/talk
    - table size ~24MB
    - index size ~2MB
* but better to check real scenario

## Indexes and tables size comparios - real example

* Start PostgreSQL client

```
$ psql -U postgres

psql (9.6.10)
Type "help" for help.

postgres=# 
```

* Switch DB to `aggregator`

```
postgres=# \c aggregator
```

* List all tables + their sizes

```
aggregator=# \d+
 public | advisor_ratings                    | table | postgres | 8192 bytes | 
 public | cluster_rule_toggle                | table | postgres | 40 kB      | 
 public | cluster_rule_user_feedback         | table | postgres | 8192 bytes | 
 public | cluster_user_rule_disable_feedback | table | postgres | 64 kB      | 
 public | consumer_error                     | table | postgres | 11 MB      | 
 public | migration_info                     | table | postgres | 8192 bytes | 
 public | recommendation                     | table | postgres | 7680 kB    | 
 public | report                             | table | postgres | 8032 kB    | 
 public | rule_disable                       | table | postgres | 16 kB      | 
 public | rule_hit                           | table | postgres | 22 MB      | 
```

* Retrieve path to DB files:

```
aggregator=# show data_directory;
 /var/lib/pgsql/data
```

* Retrieve name of directory where Aggregator database files are stored

```
aggregator=# SELECT oid from pg_database WHERE datname = 'aggregator';
 25273
```

* Retrieve name of file for given database table file:

```
aggregator=# SELECT relname, relfilenode FROM pg_class WHERE relname = 'report'; 
 report  |      160819
```

* Do the same, now for specified index:

```
aggregator=# SELECT relname, relfilenode FROM pg_class WHERE relname = 'report_cluster_key'; 
 report_cluster_key |      160826
```

* Check real table and index sizes

```
$ cd /var/lib/pgsql/data/base

$ cd 25273

$ ls -l 160819 160826
-rw-------. 1 postgres postgres 8192000 Apr 20 08:48 160819
-rw-------. 1 postgres postgres  335872 Apr 20 08:48 160826
```

* first is table, second is index



## Page and rowID

* can be read from pseudo-column `ctid`
* page + local index/offset pair

```
aggregator=# \d report
 org_id          | integer                     | not null
 cluster         | character varying           | not null
 report          | character varying           | not null
 reported_at     | timestamp without time zone | 
 last_checked_at | timestamp without time zone | 
 kafka_offset    | bigint                      | not null default 0
 gathered_at     | timestamp without time zone | 

aggregator=# select ctid, org_id, cluster from report limit 10;
 (0,1) | 61209472 | 49d95631-6933-466c-80a8-1e97556c2289
 (0,2) | 55509440 | 2ba44dd8-57e0-4b5a-ac60-84c0ba2739e8
 (0,3) | 43095178 | afe74bd6-971f-4aaa-8b76-0be3c380147d
 (0,4) |  3521457 | db4fbd44-9784-4881-bf28-7dcfca1a2f44
 (1,1) | 89176743 | 3d55fabd-4d7d-4cce-a58a-b03c58f076c3
 (1,2) | 15300416 | 0a208530-d192-4250-888d-457467a91c86
 (1,3) | 93025343 | 7bb5075a-3b15-4a29-a0b7-d0e64cc0f220
 (1,4) | 89748839 | 1ef6b89d-a3b0-4d30-a92d-ba352f2a197c
 (2,1) | 80046742 | 2014fcb4-ad5d-4474-8420-053606439ac2
 (2,2) | 73131361 | 42abe1e0-7a08-4606-9b5f-5a1f1e3a1d58
```


## Index

- every primary key has an index (usually B-tree)

## Index as data structure
- Bitmap index
- B-tree
- Log-structured merge-tree (LSM tree)

### Bitmap index
* works well for low-cardinality columns
* basically it stores following information:
    - this record exists
    - this record does not exist
* return pages to read

### B-tree data structure

* self-balancing search tree
* very wide fance-out
    - "flat tree"
* list(s) at lowest level

### Log-structured merge-tree data structure

* good for transaction log data
* key-value pairs as usual
* usually two or more structures
    - synchronization

### GIN: Generalised Inverse iNdex

* for full-text
* based on "tsvector"

## Index and heap

* ideally index should be stored in heap
    - super fast operation
    - small records in index needed
    - (not cluster_id for example)

## Index stored in physical file

```
create index idx_foo on bar(id);
select relfilenode from pg_class wheren relname like `idx_foo`;
```

* Directory structure

```
$PGDATA/xyz/xyz
```

## Expression index

## How to check if/how index is used

```sql
EXPLAIN SELECT name FROM bar WHERE id = 1234;
```

## B-tree

- it's possible to choose the B-tree for index

```sql
CREATE INDEX idx_foo ON bar USING BTREE(id);
```

## Use EXPLAIN to figure out what's happening

- Index Only Scan: ok, very effective
    - data are read just from index
    - the best
- Bitmap (Heap) Index Scan: ok, index is used
    - bits with flags for pages
    - i.e. needs another read (from pages)
- Seq Scan: the worst thing
- Parallel Seq Scan: still almost the worst thing
    - can't scale properly with DB size!
- Heap Fetches
    - if 0, information available in index, the best
    - if not in index (like `name`), it will be less effective

enabled/visible

## When not to use index?

* Column with almost the same values

## Index containing other data

* Possible to use
* But not the best solution
    - cache misses
    - not in heap

## Partial indexes

* Index just for records we want

```sql
CREATE INDEX ON x ()
WHERE active = TRUE;
```

* cost (page hits) lower

* "Active orders"

## Problematic queries

* `select *`
    - expensive
    - especially for fields not indexed
    - conversions, block moves, network moves etc.
* Large text fields
    - TOAST - pointer to another table with text
    - ineffective
    - especially when page size is exceed (8k)
* `like '%xyz$'`
* `upper`, `lower` etc/ functions in queries
    - it will basically skip index
    - index on results of expression

## Composite index

* index for multiple columns
    - (name, surname)
* left to right!
    - left-hand side column in query!!!
* `"left" and "right"` is perfect
* `"left" or "right"` problematic
* possibly large index!

## Unused indexes

* it's possible to figure out how much time index was used

```sql
SELECT relname, indexrelname, idx_scan
  FROM pg_catalog.pg_stat_user_indexes;
```

## Indexes and partitioning


## Useful links

* Database index (Wikipedia)<br>
  [https://en.wikipedia.org/wiki/Database\_index](https://en.wikipedia.org/wiki/Database_index)

* B-tree (Wikipedia)<br>
  [https://en.wikipedia.org/wiki/B-tree](https://en.wikipedia.org/wiki/B-tree)

* Log-structured merge-tree<br>
  [https://en.wikipedia.org/wiki/Log-structured\_merge-tree](https://en.wikipedia.org/wiki/Log-structured_merge-tree)

* Database Indexing Explained (with PostgreSQL)<br>
  [https://www.youtube.com/watch?v=-qNSXK7s7\_w](https://www.youtube.com/watch?v=-qNSXK7s7_w)

* Lesson #3 - How to Create Indexes? - Deep Dive Into PostgreSQL Indexes Course<br>
  [https://www.youtube.com/watch?v=bBxeBxnLl\_4](https://www.youtube.com/watch?v=bBxeBxnLl_4)

* Is SELECT * Expensive?<br>
  [https://www.youtube.com/watch?v=QQVNVOneZNg](https://www.youtube.com/watch?v=QQVNVOneZNg)

* Be careful while working with large text fields in Postgres - TOAST<br>
  [https://www.youtube.com/watch?v=UUFMAZswhU](https://www.youtube.com/watch?v=_UUFMAZswhU)

* Horizontal vs Vertical Database Partitioning<br>
  [https://www.youtube.com/watch?v=QA25cMWp9Tk](https://www.youtube.com/watch?v=QA25cMWp9Tk)

* When indexes are useless<br>
  [https://www.youtube.com/watch?v=oebtXK16WuU](https://www.youtube.com/watch?v=oebtXK16WuU)

* Partial Indexing<br>
  [https://www.youtube.com/watch?v=WL2NXQmUOC0](https://www.youtube.com/watch?v=WL2NXQmUOC0)

* Postgres index bloat<br>
  [https://www.youtube.com/watch?v=qcInj-XW1Vc](https://www.youtube.com/watch?v=qcInj-XW1Vc)

* What is the cost of Indexing too many columns<br>
  [https://www.youtube.com/watch?v=YeYIxbiupoo](https://www.youtube.com/watch?v=YeYIxbiupoo)

* PostgreSQL Indexing : How, why, and when<br>
  [https://www.youtube.com/watch?v=clrtT\_4WBAw](https://www.youtube.com/watch?v=clrtT_4WBAw)

* A Deep Dive Into PostgreSQL Indexing - PostgreSQL Index Tutorial<br>
  [https://www.youtube.com/watch?v=yWrJC2k1C8A](https://www.youtube.com/watch?v=yWrJC2k1C8A)

* Scaling Postgres Episode 56 | Indexing | Vertical Scale | Partition Migration | FDW Performance<br>
  [https://www.youtube.com/watch?v=equ1RwizkHE](https://www.youtube.com/watch?v=equ1RwizkHE)

* 5 Ways to Accelerate and Scale Out PostgreSQL<br>
  [https://www.youtube.com/watch?v=AeAWrCsWrYI](https://www.youtube.com/watch?v=AeAWrCsWrYI)
