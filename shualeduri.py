# Python - შუალედური გამოცდა #1
# --------------------------------
# #1 მინი-ბიბლიოთეკა
# --------------------
# თქვენი მიზანია შექმნათ „მინი-ბიბლიოთეკის მართვის სისტემა“, სადაც:
#
# - მომხმარებელს შეუძლია დაამატოს წიგნი (სათაური, ავტორი, წელი)
# - შეინახოს ისინი სიაში
# - მოძებნოს წიგნი სათაურით
# - დაინახოს ყველა წიგნის სია (სათაური + ავტორი)
#
# დეტალები:
# -----------
# 1. შექმენით წინასწარი "სია" სადაც მოთავსებული იქნება 10 თქვენს მიერ არჩეული
# წიგნის სახელი/ავტორი და წელი
# 2. მომხმარებელს აქვს საშუალება: წიგნი დაამატოს ამ ფორმატით სახელი/ავტორი
# და წელი
# 3. მომხმარებელს აქვს საშუალება: ნახოს უკვე არსებული წიგნები რაც
# ბიბლიოთეკაშია (10 წიგნი)
# 4. აირჩიოს მისთვის სასურველი და გაიტანოს ბიბლიოთეკიდან "წასაკითხად"
# 5. მომხმარებლის მიერ დამატებული წიგნი უნდა დაემატოს ბიბლიოთეკის სიას და
# მომდევნო გამოძახებაზე 10-ის მაგივრად უნდა გამოჩნდეს 11 და ა.შ. სანამ
# მომხმარებელი დაამატებს წიგნებს
# 6. ვალიდაცია არაა საჭირო lower/upper და ა.შ. (მომხმარებელს ყოველთვის შეჰყავს
# სწორი ინფორმაცია)
# import random

##### დასაწყისი
# booksdict = [
#     {"title" : "title1" , "author" : "author1", "year" : 1951},
#     {"title" : "title2" , "author" : "author2", "year" : 1952},
#     {"title" : "title3" , "author" : "author3", "year" : 1953},
#     {"title" : "title4" , "author" : "author4", "year" : 1954},
#     {"title" : "title5" , "author" : "author5", "year" : 1955},
#     {"title" : "title6" , "author" : "author6", "year" : 1956},
#     {"title" : "title7" , "author" : "author7", "year" : 1957},
#     {"title" : "title8" , "author" : "author8", "year" : 1958},
#     {"title" : "title9" , "author" : "author9", "year" : 1959},
#     {"title" : "title10", "author" : "author10", "year": 1960}
# ]
#
# def add_book():
#     title = input("შეიყვანეთ წიგნის სათაური: ")
#     author = input("შეიყვანეთ ავტორი: ")
#     year =  input("შეიყვანეთ წელი: ")
#     booksdict.append({"title": title, "author": author, "year":year})
#     print("წიგნი დამატებულია!")
#
# def show_bookdict():
#     for book in booksdict:
#         print(book)
#
#
# def search_book(search_title):
#     for book in booksdict:
#         if book["title"] == search_title:
#             print(book)
#
#
# def take_to_read(title):
#     for book in booksdict:
#         if book["title"] == title:
#             booksdict.remove(book)
#             print(f"წიგნი '{title}' გატანილია წასაკითხად")
#             return
#     print("წიგნი ვერ მოიძებნა")
#
#
# while True:
#     print("1. ყველა წიგნის ნახვა")
#     print("2. წიგნის დამატება")
#     print("3. წიგნის გატანა")
#     print("4. წიგნის ძებნა")
#     print("5. გამოსვლა")
#
#     result = input("აირჩიეთ მოქმედება: ")
#     if result == "1":
#         show_bookdict()
#     if result == "2":
#         add_book()
#     if result == "3":
#         bookname = input("ჩაწერეთ წიგნის სათაური: ")
#         take_to_read(bookname)
#     if result == "4":
#         book_title = input("შეიყვანეთ მოსაძებნი წიგნი: ")
#         search_book(book_title)
#     if result == "5":
#         break

# #2 პროგრამა "21" ქულა
# ---------------------
# წესები:
#
# - დასტა შედგება 52 კარტისაგან - 4 ვარიანტი ("ყვავი" "ჯვარი" "გული" "აგური")
# - 2-დან 10-მდე + Jack + Queen + King + Ace
# - კარტების ღირებულება - 2-10მდე = თავისივე მნიშვნელობა (ანუ 3 = 3, 7 = 7 და ა.შ.)
# ; J,Q,K = 10 ; Ace = 11 (მარტივი ვარიანტი, უდრის მხოლოდ 11-ს)
# - მოთამაშე და კომპიუტერი იღებენ კარტებს (თავდაპირველად 2-2,
# შემთხვევითობის პრინციპით)
# - მოთამაშეს შეუძლია აირჩიოს "add" (დამატება) ან "stop" (გაჩერდეს)
# - კომპიუტერი თავის მხრივ იღებს კარტებს მანამ, სანამ ქულა < 17
# - ვინც 21-ს მიუახლოვდება, მაგრამ არ გადააჭარბებს, ის იგებს
#
# თუ მოთამაშე მოიგებს გამოგვაქვს "თქვენ მოიგეთ" თუ კომპიუტერი "თქვენ
# წააგეთ" ფრეზე ვარიგებთ ხელახლა.
#
# შეგიძლიათ გამოიყენოთ:
# ------------------------
# 1. ციკლები
# 2. პირობითი ოპერატორები
# 3. ფუნქცია
# 4. მოდულები


######## დასაწყისი
# import random
# while True:
#     cardsdict ={"2guli":2,"3guli":3,"4guli":4,"5guli":5,"6guli":6, "7guli":7, "8guli":8, "9guli":9, "10guli":10, "J_guli":10, "Q_guli":10, "K_guli":10, "A_guli":11,
#                 "2aguri":2,"3aguri":3,"4aguri":4,"5aguri":5,"6aguri":6, "7aguri":7, "8aguri":8, "9aguri":9, "10aguri":10, "J_aguri":10, "Q_aguri":10, "K_aguri":10, "A_aguri":11,
#                 "2jvari":2,"3jvari":3,"4jvari":4,"5jvari":5,"6jvari":6, "7jvari":7, "8jvari":8, "9jvari":9, "10jvari":10, "J_jvari":10, "Q_jvari":10, "K_jvari":10, "A_jvari":11,
#                 "2yvavi":2,"3yvavi":3,"4yvavi":4,"5yvavi":5,"6yvavi":6, "7yvavi":7, "8yvavi":8, "9yvavi":9, "10yvavi":10, "J_yvavi":10, "Q_yvavi":10, "K_yvavi":10, "A_yvavi":11}
#
#     player_points = 0
#     player_list = []
#     computer_points = 0
#     computer_list = []
#
#     for i in range (2):
#         card = random.choice(list(cardsdict))
#         points = cardsdict[card]
#         player_list.append(card)
#         player_points += points
#         cardsdict.pop(card)
#
#     for i in range (2):
#         card = random.choice(list(cardsdict))
#         points = cardsdict[card]
#         computer_list.append(card)
#         computer_points += points
#         cardsdict.pop(card)
#
#     print(f"მოთამაშის ქულა {player_points}, მოთამაშის კარტები {player_list}")
#     print(f"კომპიუტერის ქულა {computer_points}, კომპიუტერის კარტები {computer_list}")
#     #print(cardsdict)
#
#     while player_points <=21:
#         answer = input("choose add or stop: ")
#         if answer == "add":
#             card = random.choice(list(cardsdict))
#             points = cardsdict[card]
#             player_list.append(card)
#             player_points += points
#             cardsdict.pop(card)
#             print(f"მოთამაშის ქულა {player_points}, მოთამაშის კარტები {player_list}")
#         else:
#             print(f"მოთამაშის ქულა {player_points}, მოთამაშის კარტები {player_list}")
#             break
#     if player_points > 21:
#         print("თქვენ გადააჭარბეთ 21 ქულას და წააგეთ :(")
#     else:
#         while computer_points < 17:
#             card = random.choice(list(cardsdict))
#             points = cardsdict[card]
#             computer_list.append(card)
#             computer_points += points
#             cardsdict.pop(card)
#             print(f"კომპიუტერის ქულა {computer_points}, კომპიუტერის კარტები {computer_list}")
#
#     if computer_points > 21 :
#         print("გილოცავთ თქვენ მოიგეთ")
#         break
#     elif player_points > computer_points:
#         print("გილოცავთ თქვენ მოიგეთ")
#         break
#     elif player_points < computer_points:
#         print("თქვენ წააგეთ")
#         break
#     else:
#         print("დაფიქსირდა ფრე, ახალი დარიგება")
#         continue
#
#
# #3 ATM Machine
#
# --------------
#
# პროგრამა მუშაობს როგორც ბანკომატი:
#
# - მომხმარებელს აქვს ანგარიშზე X თანხა რომელსაც წინასწარ ვინახავთ
# - მომხმარებელს შეუძლია შეამოწმოს ბალანსი (ბრძანებით)
# - მომხმარებელს შეუძლია თანხის: "გატანა", "შემოტანა", ბალანსის ნახვა
# - აუცილებელი ვალიდაციები: ვერ უნდა გაიტანოს იმაზე მეტი რაც ანგარიშზე აქვს
# და ასევე ერთჯერადად ვერ უნდა შეიტანოს 1000ზე მეტი
# - ბანკომატი მუშაობს მხოლოდ ლარზე
# - ყველა ოპერაცია უნდა ჩაიწეროს ლოგერში და შეიხანოს ლოგ ფაილში (გატანა,
# შემოტანა)
# - მომხმარებელს ყოველთვის შემოჰყავს სწორი ბრძანებები არაა საჭირო ცალკე
# ვალიდაციების გაწერა

######### დასაწყისი
# import logging
# logging.basicConfig(filename="account.log", level=logging.INFO, format="%(asctime)s - %(message)s")
#
# class AtmMachine:
#
#     def __init__(self, balance, currency = "GEL"):
#         if currency != "GEL":
#             raise ValueError("ოპერაციის შესრულება შესაძლებელია მხოლოდ ლარში")
#         self.__balance = balance
#         self.currency = currency
#
#
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount  ):
#         if 0 < amount <= 1000:
#             self.__balance += amount
#             logging.info(f"{amount} added and is now {self.__balance}")
#         else:
#             print("შეტანის მაქსიმალური ლიმიტია 1000 ლარი")
#
#     def withdraw(self, amount):
#         if amount >0 and (self.__balance-amount) >=0:
#             self.__balance -= amount
#             logging.info(f"{amount} withdrawed and is now {self.__balance}")
#         else:
#             print("გასატანი თანხა უნდა იყოს ნულზე მეტი და არსებული ბალანსის ტოლი ან ნაკლები")
#
# atm = AtmMachine(100)
# while True:
#     print("1. ბალანსის ნახვა")
#     print("2. თანხის შეტანა")
#     print("3. თანხის გატანა")
#     print("4. გამოსვლა")
#
#     choice = input("აირჩიე ოპერაცია: ")
#
#     if choice == "1":
#         print(f"ბალანსი: {atm.get_balance()} GEL")
#
#     elif choice == "2":
#         amount = int(input("შეიყვანე შესატანი თანხა: "))
#         atm.deposit(amount)
#
#     elif choice == "3":
#         amount = int(input("შეიყვანე გასატანი თანხა: "))
#         atm.withdraw(amount)
#
#     elif choice == "4":
#         print("მადლობა სარგებლობისთვის")
#         break


# #4 ლატარიის სიმულატორი
# --------------------------
# - კომპიუტერი ირჩევს 6 შემთხვევით რიცხვს 1–დან 49-მდე
# - მოთამაშეს შეჰყავს 6 რიცხვი
# - ითვლება, რამდენი დაემთხვა
# - წინასწარ გაწერილია გასათამაშებელი თანხა
# - logging ინახავს ყველა გათამაშებას და შედეგს
# - მომხმარებელს ყოველთვის შემოჰყავს სწორი მნიშვნელობები
# --------------------------------------------------------
# ლოგიკა:
# 1. 6-6 დამთხვევის შემთხვევაში თამაშდება JACKPOT
# 2. 6-5 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 40%-ს
# 3. 6-4 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 60%-ს
# 4. 6-3 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 80%-ს
# 5. 6-2 და 6-1 დამთხვევის შემთხვევაში მოთამაშე ვერაფერს ვერ იგებს
# ####### დასაწყისი
# import random
# import logging
# logging.basicConfig(filename="lottery.log", level=logging.INFO, format="%(asctime)s - %(message)s",encoding="utf-8")
# numberlist = []
# jackpot = 1000
# for i in range (1, 49):
#     numberlist.append(i)
#
# computerlist = []
#
# for i in range(6):
#     x = random.choice(numberlist)
#     computerlist.append(x)
#     numberlist.remove(x)
#
# print(computerlist)
# logging.info(f"კომპიუტერის რიცხვები არის : {computerlist}")
# userpoints = 0
#
# for i in range (6):
#     usernumber = int(input(f"გთხოვთ შეიყვანოთ რიცხვი, რიგითობა {i+1}: "))
#     if usernumber in computerlist:
#         userpoints += 1
#         logging.info(f"მომხმარებელმა აირჩია {usernumber} დამთხვევათა რაოდენობა შეადგენს {userpoints}")
#     else:
#         logging.info(f"მომხმარებელმა აირჩია {usernumber} , ეს რიცხვი არცერთს არ ემთხვევა")
#
#     print(f"მომხარებლის დამთხვევათა რაოდენობა {userpoints}")
#
#
# if userpoints == 6:
#     print(f"გილოცავთ, თქვენ მოიგეთ ჯეკპოტი {jackpot}")
#     logging.info(f"მოგებული თანხა შეადგენს {jackpot}")
# elif userpoints == 5:
#     print(f"გილოცავთ, თქვენ მოიგეთ ჯეკპოტი {jackpot*0.6}")
#     logging.info(f"მოგებული თანხა შეადგენს {jackpot*0.6}")
# elif userpoints == 4:
#     print(f"გილოცავთ, თქვენ მოიგეთ ჯეკპოტი {jackpot*0.4}")
#     logging.info(f"მოგებული თანხა შეადგენს {jackpot * 0.4}")
# elif userpoints == 3:
#     print(f"გილოცავთ, თქვენ მოიგეთ ჯეკპოტი {jackpot*0.2}")
#     logging.info(f"მოგებული თანხა შეადგენს {jackpot * 0.2}")
# else:
#     print("სამწუხაროდ თქვენ წააგეთ :(")
#     logging.info(f"თანხა მოგებული არ არის")

# #5 რეგისტრაციის სიმულატორი
# -------------------------------
# მომხმარებელს ვარეგისტრირებთ ჩვენს ვებ-გვერდზე სადაც არის 4 ველი: "ელ-
# ფოსტა", "სახელი", "ზედმეტსახელი" და პაროლი
#
# - სახელის გარდა ყველა ველი უკვე შევსებულია, რომელსაც ვინახავთ წინასწარ მაგ:
# user@mail.com, ... george777 და password123
# - მომხმარებელს შეჰყავს მხოლოდ სახელი, რომელიც აუცილებლად უნდა იყოს
# ტექსტური ტიპი (ლათინური ასოები და პატარა ასოები)
# - სხვა ნებისმიერი ტიპის მონაცემთა ტიპის შემთხვევაში უნდა გავუტანოთ
# შესაბამისი შეტყობინება
# - მაგალითი 1: შემოიყვანა: 123 -> "შემოყვანილია რიცხვითი მნიშვნელობა,
# შემოიტანეთ მხოლოდ string პატარა რეგისტრში"
#
# - მაგალითი 2: შემოიყვანა: @# -> "შემოყვანილია სიმბოლოები, შემოიტანეთ
# მხოლოდ string პატარა რეგისტრში" და ა.შ. ყველა შესაძლო ტიპი უნდა
# განსაზღვროთ
# - ლათინურისგან განსხვავებულს უნდა დაუწეროთ რომ არის სხვა ენა
# - მომხმარებელი თუ შემოიყვანს სტრინგს უნდა დაარეგისტრიროთ და
# გამოიტანოთ ყველა შენახული მონაცემი:"ელ-ფოსტა", "სახელი", "ზედმეტსახელი"
# და პაროლი

# import string
#
# email = "gbozhadze@gmail.com"
# nickname = "gigla"
# pwd = "mypass"
#
#
#
# while True:
#     name = input("გთხოვთ შეიყვანეთ სახელი (უნდა შეიცავდეს მხოლოდ დაბალი რეგისტრის ლათინურ სიმბოლოებს: ")
#
#     if not name.isascii():
#         print("შეცდომა: შეიცავს არალათინურ სიმბოლოებს")
#
#     elif name == "":
#         print("შეცდომა: სახელის ველი ცარიელია, გთხოვთ შეიყვანოთ დაბალი რეგისტრის ლათინური სიმბოლოები")
#
#     elif any(ch.isdigit() for ch in name):
#         print("შეცდომა: შეიცავს ციფრებს")
#
#     elif any(ch in string.punctuation for ch in name):
#         print("შეცდომა: შეიცავს სპეციალურ სიმბოლოებს (!@#$ და სხვ.)")
#
#     elif any(ch.isspace() for ch in name):
#         print("შეცდომა: შეიცავს სფეისს ან ტაბს")
#
#     elif not name.islower():
#         print("შეცდომა: უნდა იყოს მხოლოდ დაბალი რეგისტრის ასოები")
#
#     elif not name.isalpha():
#         print("შეცდომა: შეიცავს დაუშვებელ სიმბოლოებს")
#
#     else:
#         print("რეგისტრაცია წარმატებულია!")
#         print (f"ელ. ფოსტა: {email}, სახელი: {name}, ზედმეტსახელი: {nickname}, პაროლი: {pwd}")
#         break




