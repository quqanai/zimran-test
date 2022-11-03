# zimran-test

### Setup

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

### Endpoints
###### Client `http:localhost:8080`
###### Stock-Market `http://localhost:8000`
- get news `GET /news`  
params: `page`, `size`


- get news details `GET /news/<news_id>`


- get company news `GET /companies/<symbol>/news`  
params: `page`, `size`, `date_from`, `date_to`

###### Subscriptions `http://localhost:9000`
- create subscription `POST /`  
json: `{"email": ..., "symbol": ...}`
