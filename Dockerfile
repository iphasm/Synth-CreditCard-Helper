# Stage 1: Build the React Frontend
FROM node:18-alpine as build
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Setup the Python Backend
FROM python:3.10-slim

# Install system dependencies for Postgres (if needed)
# RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

# Copy Backend Requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Backend Code
COPY backend/ .

# Copy Built Frontend Assets from Stage 1 to a directory served by FastAPI
COPY --from=build /app/frontend/dist /app/static

# Expose Port (Railway/Heroku assigns PORT env var)
ENV PORT=8000
EXPOSE $PORT

# Run the application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
