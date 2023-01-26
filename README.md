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

##### CHECK:
> SELECT t.first_name, t.last_name, l.name, r.number, c.name, rozklad.time FROM rozklad INNER JOIN lessons l ON l.id=rozklad.lesson_id INNER JOIN teachers t ON t.id=rozklad.teacher_id INNER JOIN rooms r ON r.id=rozklad.room_id INNER JOIN room_class rc ON rc.room_id=r.id INNER JOIN classes c ON c.id=rc.class_id WHERE time BETWEEN "11:00:00" AND "13:00:00";

### TASK-6-Leсtion-6 (Docker)
Create docker-compose and docker container with python script which will ping data api.github.com and print it

### TASK-7-Leсtion-7 (Networking)
Self learning about network

### TASK-8-Leсtion-8 (Flask Intro)
Create route for calculator if user type in url /calc/1/2 should display 3 in another case if user type in url /calc/3/5 should return 8

### TASK-9-Leсtion-9 (Flask practice)
Create a page which display details about plant, plant information and plant employees information.

### TASK-10-Leсtion-10 (Flask and Rest)
1. Rework your page which display details about Plant to work with SQLALCHEMY.
2. Create Employee table

### TASK-11-Leсtion-11 (Flask Practice)
1. Create ability to update employee.
2. Create ability to delete employee

### TASK-12-Leсtion-12 (Flask and SQLAclhemy)
Add validation of data to registration.

### TASK-13-Leсtion-13 (Flask Practice)
Create api endpoints for plant crud (CREATE, READ, UPDATE, DELETE)

### TASK-14-Leсtion-14 (Regular expressions)

Написати regexp який розпізнає частини email-у (юзер частина, домен частину) причому розпізнає кожен окреми піддомен в окремій групі якщо в нас багаторівневий домен. Зробити це засобами regexp , або regexp  + python

Optional:

22 сторінка - Huge Example, спробувати написати python програму на базі регулярок, яка б розпізнавала  ввод юзера, таким чином що для кожного рядку у нас в результаті було дві дати: дата початку і дата завершення. У разі якщо присутня одна дата, то вважати її початковою, а кінцеву дату зробити 01.01.2100.

На лекції я пояснював більше. В деяких рядках відстуня наприклад початкова дата. тоді її вирахувати згідно інформації про тривалість і кінцеву дату.

Optional:
23 сторінка презентації

Написати python програму яка завантажує зміст посилання і проходиться по тексту шукаючи і розпізнаючи пари значень

(посада,  email) за допомогою регулярних виразів.
Тобто на виході нам треба мати список  усіх email усіх контаків навчального закладу.


### TASK-15-Leсtion-15 (Flask + Templates + Sessions)
1. Create models, views and forms for Plants
2. Create simple templates (for example you have auth logic)

### TASK-16-Leсtion-16 (Flask Practice)
налаштувати SMTP, та створити шаблони для імейлу по відновленню пароля


### TASK-17-Leсtion-17 (Flask Practice)
зробити рефакторинг коду і персоніфікувати темплейти

### TASK-17-Leсtion-17 (Django Practice)
1. Create ability to add products to category when you add category
2. Create ability to update category
3**. Create ability to add images to the products
