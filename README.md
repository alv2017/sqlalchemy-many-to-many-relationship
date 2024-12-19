# SQLAlchemy: Many-to-Many relationship

On this branch the fix that enables FK support for SQLite has been applied.
That is how our scenarios are looking now.

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

Expectation: Script execution will fail due to Foreign Key constraint violation.

Actual Result: OK
```
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) FOREIGN KEY constraint failed
[SQL: INSERT INTO association_table (parent_id, child_id, extra_data) VALUES (?, ?, ?)]
[parameters: (1, 1, 'TEST-01')]

```

After we enabled "PRAGMA foreign_keys=ON", both scenarios work as expected.