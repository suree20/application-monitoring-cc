# Log Analytics System

This project is a distributed log analytics system that collects, processes, and visualizes logs from an API server. It uses **Kafka** for message streaming, **PostgreSQL** for data storage, and **Grafana** for real-time visualization.

---

## 📁 Project Structure

- **API Server**: A Flask-based server with multiple endpoints for testing.
- **Workload Generator**: Simulates API requests and sends logs to Kafka.
- **Kafka Consumer**: Consumes logs from Kafka and stores them in PostgreSQL.
- **Database**: PostgreSQL database to store logs.
- **Grafana Dashboard**: Visualizes logs and metrics in real-time.

---

## ✅ Features

- Real-time log streaming and storage.
- Monitoring of API usage and performance.
- Visual dashboards for metrics and errors.
- Easily testable endpoints with workload simulation.

---

## 🛠 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---
## 🌐 Accessing Services
After the containers are up and running, you can access the services at:

- API Server: http://localhost:5000
- Grafana Dashboard: http://localhost:3000
Login with default credentials: admin / admin
---
## 📊 Grafana Dashboard
The Grafana dashboard provides real-time insights into the system. It includes:

- 📄 Real-time logs from API requests
- 📈 Requests per endpoint over time
- ⏱ Response time trends
-❗ Error rate percentage
-📊 Request distribution by endpoint
---
## 🧪 Testing the System
To verify that everything is working correctly:

1. Check if the API Server is running
curl http://localhost:5000/health

2. Check logs in PostgreSQL
docker exec -it <db-container-name> \
  psql -U postgres -d logsdb -c "SELECT * FROM logs;"
---
## 🧹 Cleanup
To stop and remove all containers:
docker-compose down

---
