# All Home Works List:

### TASK-1-Lection-1 (Intro to Linux and python environment. Робота з GIT)
Install linux as second OS or in VirtualBox

### TASK-2-Lection-2 (OOP)
Create app with class Toyota with methods to create different cars with different engines and colors.
Methods list:
* drive
* shift gear
* change color

### TASK-3-Lection-3 (OOP Practice)
Create ability to get all employees which work in salons and plant.

### TASK-4-Lection-4 (SQL and relational database )
Create table lessons with relation to teachers and rooms and upload dump for check.

### TASK-5-Leсtion-5 (SQL Practice)
1) Add class_id to table rozklad.
2) Rework this query to work with class_in in rozklad (not at room_class).

##### TIPS:
> SELECT t.first_name, t.last_name, l.name, r.number, c.name, rozklad.time FROM rozklad INNER JOIN lessons l ON l.id=rozklad.lesson_id INNER JOIN teachers t ON t.id=rozklad.teacher_id INNER JOIN rooms r ON r.id=rozklad.room_id INNER JOIN room_class rc ON rc.room_id=r.id INNER JOIN classes c ON c.id=rc.class_id WHERE time BETWEEN "11:00:00" AND "13:00:00";

### TASK-6-Leсtion-6 (Docker)
Create docker-compose and docker container with python script which will ping data api.github.com and print it

### TASK-7-Leсtion-7 (Networking)
Self learning about network

### TASK-8-Leсtion-8 (Flask Intro)
Create route for calculator if user type in url /calc/1/2 should display 3 in another case if user type in url /calc/3/5 should return 8
