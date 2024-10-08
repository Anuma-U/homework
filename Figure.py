class Figure:
    def __init__(self, color, *sides, filled=False, sides_count=None):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled
        self.sides_count = sides_count

    def proverka(self):
        if len(self.__sides) != self.sides_count:
            self.__sides = [self.__sides[0]] * self.sides_count
            return self.__sides

    def get_color(self):
        return list(self.__color)

    def get_sides(self):
        if isinstance(self.__sides, int) or isinstance(self.__sides, float):
            return list(self.__sides)
        else:
            return list(self.__sides)

    def sidess_count(self):
        return len(self.get_sides())

    def __is_valid_color(self, r, g, b):
        r, g, b = r, g, b
        return ((r > 0) and (r < 255)) and ((g > 0) and (g < 255)) and ((b > 0) and (b < 255))

    def set_color(self, r, g, b):
        clr = (r, g, b)
        if self.__is_valid_color(r, g, b) == True:
            self.__color = list(clr)

    def __is_valid_sides(self, *sidese):
        sides = sidese
        if len(sides) == len(self.get_sides()):
            for side in sides:
                if (isinstance(side, int) and (side > 0)) == False:
                    return False
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        new_side = new_sides
        if self.sides_count != None:
            if len(new_side) == self.sides_count:
                self.__sides = new_side


    def __len__(self):
        return sum(self.get_sides())

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides, sides_count=1)
        self.proverka()
        self.__radius = int(sides)/(2*3.14)

    def get_square(self):
        return 3.14 * self.__radius

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=3)
        self.proverka()

    def get_square(self):
        stor = self.get_sides()
        a, b, c = map(int, stor)
        p = (sum(self.get_sides())) / 2
        return (p*(p - a)*(p - b)*(p - c))**0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides, sides_count=12)
        self.proverka()

    def get_volume(self):
        return self.get_sides()[0]**3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 =  Triangle((200, 200, 100), 10, 6)
triangle1.set_sides(1, 0)
print(triangle1.get_sides())
print(round(triangle1.get_square()))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
print(circle1.sides_count)
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(circle1.get_square())

