<h1 align="center">
  <br>
  <img alt="Static Badge" src="https://img.shields.io/badge/%20Redis-Multi--Container%20Application-red">
  
# Multi-Container Flask & Redis Application

## Project Summary

This project showcases a robust, scalable, and production-ready multi-container web application leveraging **Python Flask** and **Redis**, fully containerized using **Docker** and orchestrated with **Docker Compose**.

Designed to demonstrate proficiency in microservices architecture, containerization, and cloud-native application development, this app exemplifies best practices for state management, environment configuration, and scalability in distributed systems.

---

## Key Highlights & Technical Achievements

- **Flask Web Application with Clean  Routing:**
  - `/` route: Presents a user-friendly welcome message.
  - `/count` route: Implements a highly efficient visit counter leveraging Redis as a fast in-memory datastore.

- **State Persistence with Redis:**
  - Utilizes Redis as a reliable key-value store to maintain visit counts with atomic increments ensuring concurrency safety.
  - Employs Docker volumes to persist Redis data, guaranteeing fault tolerance and data durability beyond container lifecycle.

- **Containerization & Orchestration:**
  - Separates concerns by deploying Flask and Redis in isolated Docker containers.
  - Uses Docker Compose for seamless multi-container orchestration, networking, and service dependency management.
  - Demonstrates environment variable configuration for flexible, environment-agnostic deployments.

- **Scalability & Load Balancing:**
  - Enables horizontal scaling of Flask application instances effortlessly via Docker Compose (`docker-compose up --scale web=N`).
  - Illustrates load distribution using **nginx** principles in containerized microservices.

- **Clean Code & Modular Architecture:**
  - Implements error handling for Redis connection issues, ensuring graceful degradation.

---

## Technologies & Tools Used

| Technology          | Purpose                                 |
|---------------------|-----------------------------------------|
| Python Flask        | Web framework for building the app      |
| Redis               | In-memory key-value store for fast data |
| Docker              | Containerization of application services|
| Docker Compose      | Multi-container orchestration           |
| nginx load balancer | Scale and run multiple instances        |
| Environment Variables | Configuration management              |

---


## Usage

1. Start the application:
    ```bash
    docker-compose up --scale web=3 --build
    ```

![Screenshot 2025-06-01 171933](https://github.com/user-attachments/assets/fe7b34ff-0343-4ca0-8a52-326116630768)

---

2. Open your browser and go to `http://localhost:5002` to see the welcome message.


![Screenshot 2025-06-01 165915](https://github.com/user-attachments/assets/10519728-be22-4113-ac6a-263a1bed698a)

---

3. Navigate to `http://localhost:5002/count` to see the visit count increment each time you refresh the page.
   

![Screenshot 2025-06-01 131946](https://github.com/user-attachments/assets/c61f9a82-984e-44fc-b143-f95ca4c65334)

---

## Advanced Features & Best Practices

- **Persistent Redis Storage:**
  - Configured Redis with Docker volumes to ensure data durability and resilience against container restarts or failures.

- **Environment-Aware Configuration:**
  - Flask application to read Redis host and port from environment variables, enabling easy adaptation to different deployment environments (development, staging,     production).

- **Horizontal Scaling Demonstration:**
  - Using Docker Compose setup to support running multiple Flask instances for showcasing scalability and load balancing potential in microservices environments.

- **Robust Error Handling:**
   - Gracefully managed Redis connectivity errors with meaningful fallback behavior to maintain app availability.

---

## Why This Project Matters
This application reflects modern engineering principles including:

- **Microservices & Containerization:**
  - Illustrates how to architect apps as small, independently deployable services.
- **State Management:**
  - Demonstrates how to integrate persistent state via Redis in a stateless HTTP context.
- **DevOps & CI/CD Readiness:**
  - Containerized architecture facilitates continuous integration, deployment, and scalability.
- **Cloud-Native Design:**
  - Environment-agnostic configuration and orchestration prepare the app for seamless cloud deployments.

---

## Live Application Preview:


https://github.com/user-attachments/assets/ea504bc9-03de-4d8f-8eab-fd2bfbfee9b8


---

## Conclusion

This project demonstrates a scalable, containerized web application integrating Flask and Redis, showcasing best practices in microservices architecture, state management, and container orchestration.

Feel free to explore the application, contribute enhancements, or reach out with any questions or collaboration opportunities.

---

## Contact

**Kadar Ahmed**  
- Email: ka-sharif@outlook.com
- LinkedIn: [linkedin.com/in/ks-ahmed](https://linkedin.com/in/ks-ahmed)

---


