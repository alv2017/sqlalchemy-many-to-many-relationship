# SQLAlchemy: Many-to-Many relationship

### Scenario 1:

1) run app01.py

```
python -m app01

```
Expected result: The app01 creates an empty database defined in the **db.py**

Actual result: OK

2) Let's open SQLite browser and run the following query:

```
INSERT INTO association_table VALUES(1, 1, "TEST-01");

```
Expected result: Query execution fails due to Foreign Key constraints.

Actual result: OK

```
Execution finished with errors.
Result: FOREIGN KEY constraint failed
At line 1:
INSERT INTO association_table VALUES(1, 1, "TEST-01");
```

### Scenario 2

Let's replicate the actions from the **Scenario 1** with SQLAlchemy.

**app02.py** does exactly that:

```
python -m app02

```

1) First, it creates a sqlite database as defined in **db.py**
2) Second, it attempts to create the Association, violating Foreign Key constraints (and succeeds!!!)
3) Finally, we extract the newly created Association from the database

Expectation: Association creation fails due to Foreign Key constraints.

Actual Result: Association successfully created.


### Why is that?

SQLite does not enforce FK constraints by default.

https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#foreign-key-support




