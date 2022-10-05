# All Home Works List:

### TASK-1
Create app with class Toyota with methods to create different cars with different engines and colors.
Methods list:
* drive
* shift gear
* change color

### TASK-2
Create ability to get all employees which work in salons and plant.

### TASK-3
Create table lessons with relation to teachers and rooms and upload dump for check.

### TASK#4:
1) Add class_id to table rozklad.
 2) Rework this query to work with class_in in rozklad (not at room_class).

#####TIPS:
> SELECT t.first_name, t.last_name, l.name, r.number, c.name, rozklad.time FROM rozklad INNER JOIN lessons l ON l.id=rozklad.lesson_id INNER JOIN teachers t ON t.id=rozklad.teacher_id INNER JOIN rooms r ON r.id=rozklad.room_id INNER JOIN room_class rc ON rc.room_id=r.id INNER JOIN classes c ON c.id=rc.class_id WHERE time BETWEEN "11:00:00" AND "13:00:00";
