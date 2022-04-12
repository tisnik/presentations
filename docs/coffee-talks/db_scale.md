# How to scale relational database?

## Two distinct terms
* partitioning
* replication

## Partitioning
* division of table into distinct independent tables
* horizontal
    - by row
* vertical
    - by column
* enables scaling

## Why partitioning?
* hard limits
* table size 32TB
* performance
* table scans
* index scans
* maintenance (DELETE, VACUUM)

## Partitioning is not
* silver bullet
* sharding
* perf. tuning (partially)

## A real problematic part
* dimensioning/planning!
* DB is not Agile-ready :)
* how to choose partition key
* merging partitions back

## Partitioning in Postgres
* method
* partition key
    - column(s) or expression(s)
* partition boundaries
* subpartitioning

```sql
CREATE TABLE reports
       ...
       ...
       ...
       PARTITION BY range(org_id)
```

```sql
CREATE TABLE reports
       ...
       ...
       ...
       PARTITION OF changed_at FOR VALUES FROM (2020-01-01) TO (2020-12-31)
```

```sql
ALTER TABLE report DETACH PARTITION foobar
```

Good part of relational databases
- ACID
    - atomicity
    - consistency
    - isolation
    - durability
- any scaling/partitioning break ACID in some way!

## Fallacies of distributed computing
* The network is reliable
* Latency is zero
* Bandwidth is infinite
* The network is secure
* Topology doesn't change
* There is one administrator
* Transport cost is zero
* The network is homogeneous

## Anyway...we need to scale/replicate from time to time

## Replication
* DB writes to all slaves
* very good for optimizing reads/queries
* write operation is still the bottleneck
* replication lag

## Shard(s)
* DB writes to just only selected shard
* hashing
* `org_id % len(shards)`
* complex queries
* joins difficult/impossible
    - is it our problem?
    - not yet
    - but...

## Shards can be replicated too
