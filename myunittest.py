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
import unittest

mybalance = 0

def deposit(x):
    if x <= 0:
        print("შესატანი თანხა უნდა იყოს 0 ზე მეტი")
    return mybalance + x

class mydeposittest(unittest.TestCase):
    def deposit(self):
        return deposit(10)







#
# #3 unittest3
#
# შექმენით ფუნქცია რომელიც იღებს JSON (dict) response-ს და აბრუნებს "status"-ის მნიშვნელობას. თუ status არ არსებობს → შეცდომა.
# დაწერეთ ტესტები
