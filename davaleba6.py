# #1 მოცემულია JSON მასივი:
# jsonarr = \
# [
#   {"id": 1, "price": 50},
#   {"id": 2, "price": 200},
#   {"id": 3, "price": 150}
# ]
#
# for item in jsonarr:
#     if item["price"] > 100:
#         print (item["id"])
#
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.
#
#
# #2 მოცემულია რთული JSON:
#
# myarr = {
#   "company": {
#     "departments": [
#       {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#       {"name": "HR", "employees": [{"name": "Nino"}]}
#     ]
#   }
# }
# for item in myarr["company"]["departments"]:
#       for internalitem in item["employees"]:
#           print(internalitem["name"])
#
# ამოიღე ყველა თანამშრომლის სახელი
#
# #3 მოცემულია სტუდენტების სია:
# import statistics
# mylist = \
# [
#   {"name": "Ana", "grades": [90, 80, 95]},
#   {"name": "Beka", "grades": [70, 85, 88]},
#   {"name": "Nino", "grades": [100, 95, 99]}
# ]
#
# gradelist = []
# for item in mylist:
#     gradelist.append(statistics.mean(item["grades"]))
#
# print(max(gradelist))

# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო შედეგი.
#
# # #4 მოცემულია კომპანიების სია:
# companies = \
# {
#   "companies": [
#     {
#       "name": "TechCorp",
#       "employees": [
#         {"name": "Ana", "salary": 3000},
#         {"name": "Beka", "salary": 4500}
#       ]
#     },
#     {
#       "name": "SoftPlus",
#       "employees": [
#         {"name": "Nino", "salary": 5000},
#         {"name": "Giorgi", "salary": 2500}
#       ]
#     }
#   ]
# }
#
# for item in companies["companies"]:
#     print(item["name"])
#     for initem in item["employees"]:
#         if initem["salary"] > 4000:
#             print(initem["name"])
#
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე მათი სახელები + კომპანიის სახელი.
#
#
# #5 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და დაბეჭდე პირველი მომხმარებლის სახელი.
#
# import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# getlist = response.json()
# print(getlist[0]["name"])
#


# #6 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და შექმენი ახალი პოსტი შემდეგი მონაცემებით:
## {"title": "Test", "body": "Hello World", "userId": 5}
# import  requests
# mypost = requests.post("https://jsonplaceholder.typicode.com/posts",json={"title": "Test", "body": "Hello World, I AM GIGA", "userId": 5})
# print(f"Status Code: {mypost.status_code}, Response: {mypost.json()}")

#
# #7 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False - https://jsonplaceholder.typicode.com/todos
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todolist = response.json()
#
# countcompleteditems = 0
# countincompleteditems = 0
# for item in todolist:
#     if item["completed"] == True:
#         countcompleteditems += 1
#     else:
#         countincompleteditems += 1
#
# print(f"შესრულებული ტასკებია {countcompleteditems} ხოლო შეუსრულებელი {countincompleteditems}")

# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)
#
#
# #8 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name"
#
# გამოიტანე მხოლოდ პირველი 5
#
#
#
#
# დავალება დაწერეთ 1 ფაილში და ისე ატვირთეთ Classroom-ში ან გამიზიარეთ Github-ის მისამართი.
#
# SQL-ზე სავარჯიშოდ გამოიყენეთ ეს მისამართი: https://www.hackerrank.com/domains/sql
#
# დაიწყეთ - SQL (Basic) -ით 1-დან 10-ის ჩათვლით (არასავალდებულო)
