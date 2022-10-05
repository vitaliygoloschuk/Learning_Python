from models.models import Toyota

while True:
    print("1.Add new Cars\n" +
          "2.Get all list cars\n" +
          "3.Get cars by id\n" +
          "4.Input id for car what need to modify color or gear\n" +
          "5.Stop App\n")
    flag = int(input("Choose menu item:\n"))
    if flag == 1:
        car = input("Input car model:\n")
        shift_gear = input("Input shift_gear:\n")
        change_color = input("Input car color:\n")
        cars = Toyota(car, shift_gear, change_color)
        cars.save()
    elif flag == 2:
        Toyota.get_all_cars()
    elif flag == 3:
        id = int(input("Type id to search:\n"))
        Toyota.get_by_id(id)
    elif flag == 4:
        id = int(input("Type id for search:\n"))
        Toyota.update_by_id(id)

    elif flag == 5:
        break
