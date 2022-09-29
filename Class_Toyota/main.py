class Toyota:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(self.name)

    def shift_gir(self):
        print(self.name)

    def change_color(self):
        print(self.name)



drive_version=Toyota((input("Please input name model: ")))
shift_gir_version=Toyota((int(input("Please input gir: "))))
change_color_version =Toyota((input("Please input color: ")))

# shift_gir.shift_gir()
# change_color.change_color()
drive_version.drive()
shift_gir_version.shift_gir()
change_color_version.change_color()