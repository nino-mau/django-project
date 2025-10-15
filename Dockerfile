# Use the official Python base image
FROM nikolaik/python-nodejs:python3.14-nodejs24

# Set the working directory
WORKDIR /app

# Install pnpm for django-tailwind
RUN npm install --global corepack@latest && corepack enable pnpm

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000
