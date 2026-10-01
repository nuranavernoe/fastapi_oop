class RobotVacuum:
    def __init__(self, batteryLevel, dustbimCapacity, currentAmountOfDebris):
        self.__batteryLevel = batteryLevel
        self.__dustbimCapacity = dustbimCapacity #объем контейнера для мусора
        self.__currentAmountOfDebris = currentAmountOfDebris
        self.__buttonOn = None

        if currentAmountOfDebris < 0 or currentAmountOfDebris > dustbimCapacity:
            print("Ошибка: количество мусора выходит за пределы контейнера")
            currentAmountOfDebris = 0

    def start(self):
        if self.__batteryLevel == 0:
            print("Недостаточный уровень заряда или контейнер переполнен")
            return

        if self.__currentAmountOfDebris >= self.__dustbimCapacity:
            print("Контейнер мусора переполнен")
            return
        
        self.__buttonOn = True
        print("Уборка запущена")

    def stop(self):
        if self.__buttonOn == True:
            self.__buttonOn = False
            print("Робот остановлен")
        

    def charge(self, amount):
        if self.__batteryLevel + amount > 100:
            print("Нельзя зарядить батарею выше 100%")
            return
        self.__batteryLevel += amount 
        print("Начало зарядки")

    def addTrash(self, amount):
        if self.__currentAmountOfDebris + amount >= self.__dustbimCapacity:
            print("Ошибка: контейнер переполнен")
            return
        self.__currentAmountOfDebris += amount
        print("мусор добавлен")




class Robot:
    def __init__(self, name, x, speed):
        self.name = name
        self.x = x
        self.speed = speed

    def move(self, time):
        distance = self.speed * time
        self.x += distance
        print(f"{self.name} переместился со скоростью {self.speed}. Позиция: {self.x}")


class FlyingRobot(Robot):
    def __init__(self, name, x, speed, height):
        super().__init__(name, x, speed)
        self.height = height

    def move(self, time):
        distance = self.speed * time
        self.x += distance

        print(f"{self.name} переместился со скоростью {self.speed} "
              f"на высоте {self.height}. Позиция: {self.x}")


class WalkingRobot(Robot):
    def __init__(self, name, x, speed, stepLength):
        super().__init__(name, x, speed)
        self.stepLength = stepLength

    def move(self, time):
        distance = self.speed * time
        steps = distance / self.stepLength
        self.x += distance

        print(f"{self.name} переместился. "
              f"Количество сделанных шагов: {steps}. "
              f"Позиция: {self.x}")
        
# class WalkingRobot(Robot):
#     def __init__(self, name, x, speed, stepLength):
#         super(WalkingRobot, self).__init__(name, x, speed)
#         self.stepLength = stepLength

#     def move(self, time):
#         steps = self.speed * time
#         distance = steps * self.speed
#         self.x += distance
#         print("f"{self.name} переместился. Количество сделанных шагов: {self.stepLength}. Позиция: {self.x}"")

robot1 = WalkingRobot("Шурик", 0, 60, 50)
robot1.move(5)
