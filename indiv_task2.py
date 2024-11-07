from abc import ABC, abstractmethod
import math

class Triangle(ABC):
    def __init__(self, side1: float, side2: float, angle_between: float):
        """
        Инициализация треугольника с двумя сторонами и углом между ними в градусах.
        """
        self.side1 = side1
        self.side2 = side2
        self.angle_between = angle_between  # угол в градусах

    @abstractmethod
    def area(self) -> float:
        """
        Вычисление площади треугольника.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вычисление периметра треугольника.
        """
        pass

class RightTriangle(Triangle):
    def __init__(self, side1: float, side2: float):
        """
        Инициализация прямоугольного треугольника с двумя катетами.
        Угол между ними равен 90 градусам.
        """
        super().__init__(side1, side2, 90)

    def area(self) -> float:
        """
        Вычисление площади прямоугольного треугольника.
        """
        return 0.5 * self.side1 * self.side2

    def perimeter(self) -> float:
        """
        Вычисление периметра прямоугольного треугольника.
        """
        hypotenuse = math.sqrt(self.side1**2 + self.side2**2)
        return self.side1 + self.side2 + hypotenuse

class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side: float, base: float, angle_between: float):
        """
        Инициализация равнобедренного треугольника.
        equal_side: равные стороны
        base: основание
        angle_between: угол между равными сторонами в градусах
        """
        super().__init__(equal_side, equal_side, angle_between)
        self.base = base

    @classmethod
    def from_equal_side_and_angle(cls, equal_side: float, angle_between: float):
        """
        Альтернативный конструктор для равнобедренного треугольника,
        вычисляющий основание по равным сторонам и углу между ними.
        """
        angle_rad = math.radians(angle_between)
        base = 2 * equal_side * math.sin(angle_rad / 2)
        return cls(equal_side, base, angle_between)

    def area(self) -> float:
        """
        Вычисление площади равнобедренного треугольника.
        """
        angle_rad = math.radians(self.angle_between)
        return 0.5 * self.side1 * self.side2 * math.sin(angle_rad)

    def perimeter(self) -> float:
        """
        Вычисление периметра равнобедренного треугольника.
        """
        return 2 * self.side1 + self.base

class EquilateralTriangle(Triangle):
    def __init__(self, side: float):
        """
        Инициализация равностороннего треугольника.
        Все стороны равны, угол между ними 60 градусов.
        """
        super().__init__(side, side, 60)
        self.side3 = side  # Все три стороны равны

    def area(self) -> float:
        """
        Вычисление площади равностороннего треугольника.
        """
        return (math.sqrt(3) / 4) * self.side1**2

    def perimeter(self) -> float:
        """
        Вычисление периметра равностороннего треугольника.
        """
        return 3 * self.side1


if __name__ == '__main__':
    # Демонстрация работы прямоугольного треугольника
    right = RightTriangle(3, 4)
    print("Прямоугольный треугольник:")
    print(f"Площадь: {right.area()}")
    print(f"Периметр: {right.perimeter()}\n")

    # Демонстрация работы равнобедренного треугольника
    isosceles = IsoscelesTriangle.from_equal_side_and_angle(5, 60)
    print("Равнобедренный треугольник:")
    print(f"Площадь: {isosceles.area()}")
    print(f"Периметр: {isosceles.perimeter()}\n")

    # Демонстрация работы равностороннего треугольника
    equilateral = EquilateralTriangle(6)
    print("Равносторонний треугольник:")
    print(f"Площадь: {equilateral.area()}")
    print(f"Периметр: {equilateral.perimeter()}")