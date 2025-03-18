# Docker running guidance

## Part 1

### Create requirement.txt


> Run this command it will create automatically
```
pip freeze > requirements.txt
```

### Create Dockerfile



```
# Use an official Python runtime as a parent image
FROM python:3.11<br>

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the Python script
CMD ["python", "persistent.py"]```



### Create docker compose



```
services:  
  persistent_app:  
    build: .  
    container_name: persistent_app  
    depends_on:  
      - my_pgvector  
      - ollama  
    environment:  
      DATABASE_HOST: my_pgvector  
      DATABASE_PORT: 5432  
      DATABASE_USER: user  
      DATABASE_PASSWORD: 1  
      DATABASE_NAME: mydb  
      OLLAMA_HOST: ollama  # Thêm host của Ollama  
    networks:  
      - my_network  
  
  my_pgvector:  
    image: ankane/pgvector  
    container_name: my_pgvector  
    restart: always  
    environment:  
      POSTGRES_USER: user  
      POSTGRES_PASSWORD: 1  
      POSTGRES_DB: mydb  
    ports:  
      - "5432:5432"  
    networks:  
      - my_network  
  
  ollama:  
    image: ollama/ollama  
    container_name: ollama  
    restart: always  
    ports:  
      - "11434:11434"  
    networks:  
      - my_network  
    volumes:  
      - ollama_data:/root/.ollama  # Lưu cache model để tránh tải lại mỗi lần chạy  
    command: ["serve"]  # Chạy Ollama ở chế độ server  
  
networks:  
  my_network:  
    driver: bridge  
  
volumes:  
  ollama_data:```  
  
  
  
### Run docker-compose  

```
docker-compose up --force-recreate --build -d
```

### Delete old containers and volume

```
docker-compose down -v --remove-orphans
```

### See logs of container



```
docker logs <container_name>
```



## Part 2

### Network

> **Inspect network**
```
docker network inspect <network_name>
```

> **Create network**

```
docker network create <network_name>
```

> **Remove network**

```
docker network rm <network_name>
```

> **Connect containers' network**

```
docker network connect <network_name> <container_id_or_name>
```

> **Disconnect containers' network**

```
docker network disconnect <current_network> <container_id_or_name>
```

P/s: Make sure all containers same network

### Ollama

> **Pull model in ollama (using docker)**

```
docker exec -it ollama ollama pull mistral
```

### Postgre

> **Run postgre using docker**

```
docker exec -it my_postgres psql -U myuser -d mydatabase
```
> **Query username, password, database name, host in postgre using docker**

```
SELECT usename FROM pg_user;
SELECT datname FROM pg_database;
```
