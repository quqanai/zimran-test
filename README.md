# zimran-test

###### Build
```bash
docker-compose build
```

###### Apply migrations
```bash
docker-compose run stock-market aerich upgrade
```
```bash
docker-compose run subscriptions aerich upgrade
```

###### Run
```bash
docker-compose up
```

###### (Optional) Check code-style
```bash
docker-compose run <service_name> flake8 code
```
