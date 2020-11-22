class polygon:
    __width = None
    __height = None

    def set_value(self, width, height):
        self.__width = width
        self.__height = height


    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(polygon):
    def area(self):
        return self.get_width() * self.get_height()


class Triangle(polygon):
    def area(self):
        return self.get_width() * self.get_height() / 2



rect = Rectangle()
tri = Triangle()

rect.set_value(40, 50)
tri.set_value(40, 50)

print(rect.area())
print(tri.area())
