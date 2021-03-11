# Initial setup

>`docker-compose build`<br>
`docker-compose up`<br>
`docker-compose exec web python manage.py init_setup`
<hr>

# Django
>Admin: http://localhost:8000/admin/ <br>
Swagger: http://localhost:8000/swagger/ <br>
Redoc: http://localhost:8000/redoc/ <br>
Default credentials: <br>
*Username: admin* <br>
*Password: 1234* <br>
<hr>

# Redis
****TODO: Make sure redis stores data***
>Connect: <br>
`docker exec -it albert-test_redis_1 sh` <br>
`redis-cli`
