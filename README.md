Theatre API Service

Theatre API Service is a web service built with Django and Django REST Framework.
It provides an API for managing and retrieving information about theatre plays, performances,
and reservations.

Project Structure
The project is organized into several apps, each serving a different part of the API:

theatre: Contains models, views, and serializers for managing theatre-related 
data such as genres, actors, theatre halls, plays, performances, and tickets.

user: Handles user registration and authentication.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Installation

Clone the repository:

git clone https://github.com/kstorozhenko/Theatre-API-Service

Navigate to the project directory:

cd theatre-api-service

Build the Docker images:

docker-compose build

Run the Docker containers:

docker-compose up

The API should now be accessible at http://localhost:8001/.


API Endpoints

The API includes the following endpoints:


/api/theatre/genres/

/api/theatre/actors/

/api/theatre/theatre_halls/

/api/theatre/plays/

/api/theatre/performances/

/api/theatre/reservations/

/api/user/register/

/api/user/token/

/api/user/token/refresh/

/api/user/token/verify/

/api/user/me/
