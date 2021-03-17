# Initial setup

>`docker-compose up --build`<br>
`docker-compose exec drf python manage.py init_setup`
<hr>

# Django
>Admin: http://localhost:8000/admin/ <br>
Swagger: http://localhost:8000/swagger/ <br>
Redoc: http://localhost:8000/redoc/ <br>
Default credentials: <br>
*Username: admin* <br>
*Password: 1234* <br>
<hr>

# React
****TODO: Add front representation of users and channels***
>Front: http://localhost:3000/ <br>
<hr>

# Redis
****TODO: Make sure redis stores data***
>Connect: <br>
`docker exec -it base-test_redis_1 sh` <br>
`redis-cli`
<hr>

****TODO: Make tests***
