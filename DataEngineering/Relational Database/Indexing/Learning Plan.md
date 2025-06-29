# 🧠 2-Week Database Indexing Mastery Plan

- Index types & algorithms
- Query optimization
- Index strategies for different filters

---

## 📅 Week 1: Core Indexing Concepts

### ✅ Day 1: Introduction to Indexing
- What is an index?
- Why indexes improve SELECT performance
- Trade-offs with INSERT/UPDATE
- Hands-on:
  - Create table
  - Run queries with/without index
  - Compare query time

---

### ✅ Day 2: B-Tree Indexes
- B-Tree structure & traversal
- Best for:
  - `=`, `<`, `>`, `BETWEEN`
- Default in MySQL/PostgreSQL
- Hands-on:
  - Create B-Tree index
  - Use `EXPLAIN`

---

### ✅ Day 3: Hash Indexes
- Uses hash function for fast `=` lookups
- Not suitable for range or `LIKE` queries
- Best for:
  - Equality filters (`col = val`)
- Hands-on:
  - Create `USING HASH` index in PostgreSQL
  - Benchmark vs B-Tree

---

### ✅ Day 4: Indexing by Filter Type
- Filters and their behavior with indexes:
  - `col = val`
  - `col IN (...)`
  - `col LIKE 'abc%'` vs `'%abc'`
  - `IS NULL`, `IS NOT NULL`
- Composite vs single-column index
- Hands-on:
  - Apply different queries
  - Observe query plan & timing

---

### ✅ Day 5: Composite & Covering Indexes
- Multi-column indexes
- Index column order matters
- Covering indexes (when query can be satisfied entirely by index)
- Hands-on:
  - Create composite index
  - Try `WHERE a=?`, `WHERE b=?`, `WHERE a=? AND b=?`

---

### ✅ Day 6: Index Maintenance and Cost
- Index size, storage cost
- Impact on write-heavy workloads
- Index fragmentation
- Hands-on:
  - Measure insert/update times
  - View index stats

---

### ✅ Day 7: Review and Practice
- Recap concepts
- Revisit hands-on labs
- Analyze query plans using:
  - `EXPLAIN ANALYZE` (PostgreSQL)
  - `EXPLAIN FORMAT=JSON` (MySQL)

---

## 📅 Week 2: Advanced Indexing & Optimization

### ✅ Day 8: Full-Text Indexing
- Handles `LIKE '%word%'` efficiently
- PostgreSQL: `tsvector`, `tsquery`
- Hands-on:
  - Add FTS to blog/product descriptions
  - Use `to_tsquery`, `plainto_tsquery`

---

### ✅ Day 9: Bitmap Indexes
- Ideal for low-cardinality columns (e.g., `gender`, `status`)
- Used in OLAP/columnar DBs (e.g., ClickHouse, Apache Druid)
- Hands-on:
  - Simulate via materialized views or use a columnar DB

---

### ✅ Day 10: GIN & GiST Indexes (PostgreSQL)
- GIN: fast indexing of arrays, full-text, JSONB
- GiST: spatial, fuzzy match, custom data types
- Hands-on:
  - Create GIN index on JSONB/array columns
  - Query with `@>`, `?|`, `LIKE` fuzzy match

---

### ✅ Day 11: Expression & Partial Indexes
- Index on expression: `LOWER(name)`
- Partial index: `WHERE status = 'active'`
- Hands-on:
  - Create partial indexes
  - Monitor planner decisions with `EXPLAIN`

---

### ✅ Day 12: JSON & Array Indexing
- JSONB indexing via GIN
- Array contains/overlaps
- Hands-on:
  - Create JSONB dataset
  - Index nested keys

---

### ✅ Day 13: Query Optimization Using Indexes
- Index-only scan
- Avoiding full table scan
- Redundant/unused indexes
- Hands-on:
  - Tune a poorly performing query using indexes
  - Remove unused indexes using statistics

---

### ✅ Day 14: Final Capstone Project
- Build mini e-commerce database
- Add and test:
  - B-Tree for IDs and timestamps
  - Full-text for products
  - GIN on JSON specs
  - Partial for active products
- Document:
  - Index types used
  - Query improvements
  - Query plans before/after

---

## 📚 Bonus Resources

### 🔖 Books
- *SQL Performance Explained* – Markus Winand
- *PostgreSQL Up & Running* – Regina Obe

### 🔍 Tools
- `EXPLAIN`, `pg_stat_user_indexes`, `auto_explain` (PostgreSQL)
- `SHOW INDEX`, `EXPLAIN FORMAT=JSON` (MySQL)

### 🌐 Websites
- [https://use-the-index-luke.com](https://use-the-index-luke.com)
- [https://explain.dalibo.com](https://explain.dalibo.com)

---

🏁 By the end of this plan, you’ll:
- Master when & how to use different index types
- Understand underlying algorithms like B-Tree, Hash, GIN, GiST
- Confidently optimize complex SQL queries
