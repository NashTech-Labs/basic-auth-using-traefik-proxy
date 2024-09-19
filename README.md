# MyApp with Traefik Reverse Proxy

This project sets up a simple Flask application (`myapp`) behind a Traefik reverse proxy with basic authentication.

## Prerequisites

- Docker and Docker Compose installed.

## Project Structure

```
├── Dockerfile
├── docker-compose.yml
└── app.py
```

## Configuration

### `docker-compose.yml`

- **Traefik Service**: Routes traffic, exposes ports 80 (HTTP) and 8080 (dashboard).
- **MyApp Service**: Flask application with Traefik routing and basic authentication for users `test` and `test2`.

### `app.py`

A simple Flask app with one route:

- **`/home`**: Returns a welcome message.

### `Dockerfile`

- Base image: `python:3.8-slim-buster`.
- Installs Flask and exposes port 4000.

## Running the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd myapp
   ```
   
2. Build and run:
   ```bash
   docker-compose up --build
   ```

3. Access the Traefik dashboard at `http://localhost:8080`.

## Accessing the Application

Visit `http://example.com/home` in your browser. Basic authentication is required.