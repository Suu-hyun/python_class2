# 상속
# 부모 클래스의 속성과 메소드를 자식 클래스가 물려받음

# super()
# 부모 클래스를 부르는 것

# 메소드 오버라이딩
# 부모 클래스의 메소드를 자식 클래스에서 재정의(Overriding)하는 것
# 같은 이름의 메소드를 자식 클래스에서 다시 정의하여 동작을 변경하는 것

# 다중 상속
# 두 개 이상의 부모 클래스로부터 속성과 메소드를 상속받는 것
# 즉, 자식 클래스가 여러 부모 클래스로부터 기능을 물려받을 수 있음
# 코드 재사용성 향상, 다양한 기능 조합 가능
# ==============================================================================

# 상속

# class Parent:
#     def introduce(self):
#         print("저는 부모입니다.")
#
# class Child(Parent):
#     def introduce(self):
#         print("저는 자식입니다.")
#
# child = Child()
# child.introduce() # 상속과 메소드 오버라이딩이 일어남

# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price

#     def drive(self):
#         print(f"{self.model}가 앞으로 전진합니다.")

# class ElecCar(Car):
#     def __init__(self, model, price, energy_efficiency):
#         super().__init__(model, price) # ==Car.__init__(self, model, price)
#         self.energy_efficiency = energy_efficiency

#     def drive(self):
#         super().drive() # 부모 클래스의 drive(메소드)를 그대로 호출한 것
#         print(f"{self.model}이 전기로 전진합니다.") # 메소드 오버라이딩

# ev6 = ElecCar("ev6", "5000", "60kwh")
# ev6.drive()

# 다단계 상속
# class GrandParents:
#     def introduce(self):
#         print("우리는 할머니 할아버지")

# class Parent(GrandParents):
#     def introduce(self):
#         super().introduce()
#         print("우리는 엄마 아빠")

# class Child(Parent):
#     def introduce(self):
#         super().introduce()
#         print("우리는 자식")

# child1 = Child()
# child1.introduce()

# 다중 상속
# class Father:
#     def drive(self):
#         print("운전을 잘함.")
#
# class Mother:
#     def cook(self):
#         print("요리를 잘함")
#
# class Child(Father, Mother):
#     def study(self):
#         print("공부를 잘함")
#
# child1 = Child()
# child1.drive()
# child1.cook()
# child1.study()

# class Animal:
#     def breathe(self):
#         print("숨을 쉴 수 있어요")
#
# class Swimmer:
#     def swim(self):
#         print("헤엄을 칠 수 있어요")
#
# class Fish(Animal, Swimmer):
#     pass
#
# nimo = Fish()
# nimo.swim()
# nimo.breathe()

# class GrandParent:
#     def smart(self):
#         print("똑똑해요")
#
# class Father:
#     def doctor(self):
#         print("나는 의사")
#
# class Mother:
#     def rich(self):
#         print("나는 부자")
#
# class Child(Father, Mother, GrandParent):
#     pass
#
# child = Child()
# child.rich()
# child.smart()
# child.doctor()

# class A:
#     def introduce(self):
#         print("나는 A")

# class B:
#     def introduce(self):
#         print("나는 B")

# class C:
#     def introduce(self):
#         print("나는 C")

# class Child(A, B, C):
#     def introduce(self):
#         print(Child.mro())
#         super().introduce() # MRO(Method Resolution Order)에 따라 첫 번째
#         super(A, self).introduce() # A 다음의 클래스를 불러옴
#         C.introduce(self) # c를 직접 불러옴

# child = Child()
# child.introduce()

#MRO
# => Method Resolution Order 메소드 결정 순서

# 예제1
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print(f"{self.brand}의 {self.model}가 시동을 겁니다.")
#
#     def stop(self):
#         print(f"{self.brand}의 {self.model}가 정지합니다.")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity
#
#     def charge(self):
#         print(f"{self.brand}의 {self.model}가 배터리를 충전합니다.")
#
# class GasolineCar(Car):
#     def __init__(self, brand, model, fuel_capacity):
#         super().__init__(brand, model)
#         self.fuel_tank_capacity = fuel_capacity
#
#     def refuel(self):
#         print(f"{self.brand}의 {self.model}가 연료를 주유합니다.")
#
# class HybridCar(ElectricCar, GasolineCar):
#     def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
#         super().__init__(brand, model, battery_capacity)
#         super(ElectricCar, self).__init__(brand, model,fuel_tank_capacity)
#
#
#     def switch_mode(self, mode):
#         if mode == "electric":
#             print(f"{self.brand}의 {self.model}가 전기모드로 전환됩니다.")
#         elif mode == "gasoline":
#             print(f"{self.brand}의 {self.model}가 내연기관모드로 전환됩니다.")
#         else:
#             print("잘못된 모드입니다.")


# hybrid = HybridCar("hyundai", "sonata", "60kWh", "50L")
# hybrid.switch_mode("electric")

# 해결방법
# class HybridCar(Car, ElectricCar, GasolineCar):
# def __init__(self, brand, model, battery_capacity, fuel_tank_capacity):
# car.__init__(self, brand, meodel)
# ElectricCar.__init__(self, battery_capacity)
# GasolineCar.__init__(self, fuel_tank_capacity) 로 바꿔줌

# 끝