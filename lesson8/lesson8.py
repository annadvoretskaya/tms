"""
Создайте класс Figure. У каждой фигуры есть имя, также можно найти площадь и периметр фигуры. 
Создайте классы Triangle, Circle, Rectangle производные от Figure. 
У класса Triangle есть 3 стороны: a, b, c; у Circle - радиус r; у Rectangle - стороны a и b. 
Переопределите методы нахождения площади и периметра для каждой фигуры (Triangle, Circle, Rectangle). 
Также для объектов классов должны работать операторы сравнения: ==, >, < <=, >=. 
Будем считать, что фигуры равны, если они имеют одинаковую площадь. 
Строковое представление объекта должно возвращать тип фигуры и её имя в следующем формате:
например для Circle(name='abc', r=2) - Circle:"abc"
Дополнительная функциональность приветствуется.
"""


circles = [Circle(name=f'r={i}', r=i) for i in range(1, 5)]
rectangles = [Rectangle(name=f'a={i}, b={i**2}', a=i, b=i**2) for i in range(1, 5)]
triangles = [Triangle(name=f'a={i+1}, b={i**2}, c={(i + i**2)//2}', a=i+1, b=i**2, c=(i + i**2)//2) for i in range(1, 4)]

figures = circles + triangles + rectangles
for figure in figures:
    print(f'My name is: {figure}')
    assert str(figure) == f'{figure.__class__.__name__}:"{figure.name}"'
    print(f'My perimeter is: {figure.perimeter()}')
    print(f'My square is: {figure.square()}', end=f"\n{'-'*35}\n")

assert Circle(name='1', r=2) == Circle(name='2', r=2)
assert Circle(name='1', r=2) < Circle(name='2', r=4)
assert Circle(name='1', r=4) >= Circle(name='2', r=4)


assert Rectangle(name='1', a=2, b=3) == Rectangle(name='2', b=2, a=3)
assert Rectangle(name='1', a=2, b=3) < Rectangle(name='2', a=4, b=10)
assert Rectangle(name='1', a=4, b=2) >= Rectangle(name='2', a=4, b=1)

assert Triangle(name='1', a=2, b=3, c=4) == Triangle(name='2', b=2, a=3, c=4)
assert Triangle(name='1', a=2, b=3, c=1.5) < Triangle(name='2', a=4, b=10, c=7)
assert Triangle(name='1', a=4, b=2, c=5) >= Triangle(name='2', a=4, b=5, c=1)
