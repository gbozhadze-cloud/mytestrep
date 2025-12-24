# #1 ამოცანა 1
# შექმენი კლასი BankAccount, რომელსაც ექნება:
# დახურული ატრიბუტები: __balance, __owner.
# მეთოდი deposit(amount) – თანხის დამატება.
# მეთოდი withdraw(amount) – თანხის გამოტანა (არ უნდა გადავიდეს მინუსში).
# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის.
# დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.
#
# class BankAccount:
#     def __init__(self, balance, owner):
#         self.__balance = balance
#         self.__owner = owner
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount >0 and (self.__balance-amount) >=0:
#             self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(1000, "Giga")
# account.deposit(500)
# x = account.get_balance()
# print(x)

# #2 ამოცანა 2
# შექმენი კლასი ShoppingCart, რომელსაც ექნება:
#
# ატრიბუტი items (სიაში პროდუქტების რაოდენობა).
#
# __len__() დააბრუნებს პროდუქტების რაოდენობას.
#
# __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.
#
# გააკეთე 2 კალათა და შეადარე.
# გააკეთე 3 კალათა და შეადარე.
# გააკეთე 4 კალათა და შეადარე.

# class ShoppingCart:
#     def __init__(self, items):
#         self.items = items
#
#     def __len__(self):
#         return len(self.items)
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#
#
# mycart = ShoppingCart (["skami", "magida", "tumbo"])
# mycart2 = ShoppingCart (["skami", "magida",])
#
# print(len(mycart)) #სიაში პროდუქტების რაოდენობა
# print(mycart==mycart2) #ორი კალათის შედარება
#
# mycart3 = ShoppingCart(["item1", "item2"])
# print(mycart==mycart2==mycart3) #3 კალათა და შეადარე
#
# mycart4 = ShoppingCart(["item1", "item2"])
# print(mycart==mycart2==mycart3==mycart4) #4 კალათა და შეადარე.
#
# #3 ამოცანა 3
# გამოიყენე @dataclass მოდული კლასის Book შესაქმნელად:
#
# ველები: title, author, year.
#
# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970.
#
# შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.


# from dataclasses import dataclass
# @dataclass()
# class Book:
#     title: str
#     author: str
#     year: int
#
#     def is_classic(self):
#         if self.year < 1970:
#             return True
#         else:
#             return False
#
#
# book1 = Book("book1","author1", 1965)
# book2 = Book("book2","author2", 1975)
#
# print(book1)
# print(book1.is_classic())
# print(book2)
# print(book2.is_classic())

# #4 ამოცანა 4
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del-ით.
#
#
#
# #5 ამოცანა 5
# შექმენი კლასი CustomList, რომელიც:
#
# ინახავს ელემენტებს.
#
# __getitem__() – აბრუნებს ელემენტს ინდექსით.
#
# __setitem__() – ცვლის ელემენტს.
#
# __iter__() – Iterable უნდა იყოს.
#
# გამოიყენე for ციკლში შენი CustomList.
#
#
# #6 ამოცანა 6
# შექმენი კლასი Refrigerator, რომელსაც ექნება:
#
# ატრიბუტი items (სია).
#
# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია ("milk" in fridge).
#
# __str__() – "Fridge with N items".
#
# __del__() – "Fridge unplugged!".
#
# დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.
#
#
# #7 ამოცანა 7
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:
#
# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".
#
# __mul__() – აბრუნებს "Multiplication is too mainstream...".
#
# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"
#
# __str__() – "I’m the funniest calculator in Python!".
#
# ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.