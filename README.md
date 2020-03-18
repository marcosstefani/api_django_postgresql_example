# api_django_postgresql_example
API example using Django and PostgreSQL

## EndPoints:
POST http://127.0.0.1:8000/users/ >> Add list of Users
GET http://127.0.0.1:8000/users/birthdays >> Find All Users
GET http://127.0.0.1:8000/users/birthdays?from=date&to=date >> Find Filtered Users
GET http://127.0.0.1:8000/users/birthdays/sum >> Return the sum of ages

GET http://127.0.0.1:8000/tools/letter/digit?str=text >> return all possibilities of cases on string

# Compose:
sudo docker-compose up