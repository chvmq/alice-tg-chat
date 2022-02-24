### You can use row sql query to migrate

```
cat add_chating.sql | docker exec -i db_alice psql -U postgres
```

### Alembic

Or install alembic migration tool, Just was lazy to install
