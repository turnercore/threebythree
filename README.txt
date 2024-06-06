# Flask Image Grid App

This is a simple Flask application that allows users to upload 9 images, processes them into a 3x3 grid, and provides the resulting image for download.

## Features

- Upload 9 images
- Resize and arrange images into a 3x3 grid
- Download the processed image

## Requirements

- Docker
- Docker Compose

## Setup and Usage

### 1. Create a Project Folder

Create a folder on your local machine to hold the project files.

```sh
mkdir my-flask-app
cd my-flask-app
```

2. Clone the Project
Download the project files into the created folder. You can clone the repository or download the files manually.

# If using git clone
`git clone <repository_url> .`

3. Project Structure
Ensure your project folder has the following structure:
my-flask-app/
├── api/
│   └── index.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

4. Build and Run the Docker Container
Navigate to your project directory and run the following command to build and start your Flask app:

sh
Copy code
docker-compose up --build
5. Access the Application
Open your web browser and go to http://localhost:5024 to see your Flask app running.