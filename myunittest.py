# #1 unittest1
#
# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს ყველა მეთოდს.
# გაითვალისწინეთ 0-ზე გაყოფაც.
# გამოიყენეთ unittest მოდული
# def add (a,b):
#     return a + b
#
# def subtract (a,b):
#     return a - b
#
# def multiply (a,b):
#     return a * b
#
# def divide (a,b):
#     return a / b
#
# assert add(1,2) == 3
# assert subtract(4,3) == 1
# assert multiply(1,2) == 2
# assert divide(9,3) == 3
#
# print("ყველა ტესტი წარმატებულია")

# #2 unittest2
# შექმენით ფუნქციები deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:
# - სწორი ბალანსი
# - უარყოფითი თანხის შეტანისას შეცდომა
# - თანხის გამოტანა ბალანსზე მეტისას შეცდომა
#
# import unittest
#
# mybalance = 0
#
# def deposit(x):
#     global mybalance
#     if x <= 0:
#         raise ValueError("შესატანი თანხა უნდა იყოს 0 ზე მეტი")
#     mybalance += x
#     return mybalance
# def withdraw(x):
#     global mybalance
#     if x <= 0:
#         raise ValueError("თანხა უნდა იყოს 0 ზე მეტი")
#     if x > mybalance:
#         raise ValueError("არასაკმარისი ბალანსი")
#     mybalance -= x
#     return mybalance
#
# class deposittest(unittest.TestCase):
#
#     def ganuleba(self):
#         global mybalance
#         mybalance = 0
#     def testok(self):
#         deposit(100)
#         withdraw(40)
#         self.assertEqual(mybalance, 60)
#     def negative(self):
#         with self.assertRaises(ValueError):
#             deposit(-10)
#     def arasakmarisi(self):
#         with self.assertRaises(ValueError):
#             withdraw(100)
#
# if __name__ == "__main__":
#     unittest.main()
#
# #3 unittest3
#
# შექმენით ფუნქცია რომელიც იღებს JSON (dict) response-ს და აბრუნებს "stat1      s"-ის მნიშვნელობას. თუ status არ არსებობს → შეცდომა.
# დაწერეთ ტესტები
#
# import unittest
#
# def myfunction(x):
#     if x["status"] == "":
#         raise ValueError("სტატუსის შეცდომა")
#     else:
#         return x["status"]
#
#
# class mytest(unittest.TestCase):
#
#     def testok(self):
#         y = {"status":201}
#         myfunction(y)
#         self.assertEqual(myfunction(y), 201)
#
#     def testnegative(self):
#         with self.assertRaises(ValueError):
#             y = {"status": ""}
#             print(myfunction(y))
#
# if __name__ == "__main__":
#      unittest.main()








