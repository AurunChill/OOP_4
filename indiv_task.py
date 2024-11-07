class Man:
    def __init__(self, name, age, gender, weight):
        self._name = name      # Имя
        self._age = age        # Возраст
        self._gender = gender  # Пол
        self._weight = weight  # Вес

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value):
        self._age = new_value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, new_value):
        self._gender = new_value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_value):
        self._weight = new_value


class Student(Man):
    def __init__(self, name, age, gender, weight, study_year):
        super().__init__(name, age, gender, weight)
        self._study_year = study_year  # Год обучения

    @property
    def study_year(self):
        return self._study_year

    @study_year.setter
    def study_year(self, new_value):
        self._study_year = new_value

    def increase_study_year(self):
        """Увеличить год обучения на 1"""
        self.study_year += 1


if __name__ == '__main__':
    # Создаем объект Man
    man = Man("Алексей", 30, "М", 75)
    print(f"Ман: {man.name}, Возраст: {man.age}, Пол: {man.gender}, Вес: {man.weight}")

    # Изменяем имя, возраст и вес
    man.name = "Иван"
    man.age = 31
    man.weight = 78
    print(f"После изменений: {man.name}, Возраст: {man.age}, Вес: {man.weight}")

    # Создаем объект Student
    student = Student("Мария", 20, "Ж", 60, 2)
    print(f"Студент: {student.name}, Возраст: {student.age}, Пол: {student.gender}, Вес: {student.weight}, Год обучения: {student.study_year}")

    # Переназначаем и увеличиваем год обучения
    student.study_year = 3
    student.increase_study_year()
    print(f"После изменений: Год обучения: {student.study_year}")