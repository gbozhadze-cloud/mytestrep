#1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
##Word = “CODE”

# def my_generator(word):
#     for symbol in word:
#         yield symbol
#
#
# gen = my_generator("code")
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და
# მომხმარებელი უნდა მიწვდეს შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ უნდა გავიდეს.

#arr = [1, 2, 3,4,5,6,7,8,9]


#3 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა,
# მიღებული პასუხებიდან უნდა განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი game.log და შევინახოთ
# ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი
# import logging
#
# logging.basicConfig(filename="game.log" , level=logging.INFO)
#
# question1 = input("1 + 1?")
# answer1 = "2"
# question2 = input("2 + 2?")
# answer2 = "4"
# question3 = input("3 + 3?")
# answer3 = "6"
# question4 = input("4 + 4?")
# answer4 = "8"
# question5 = input("5 + 5?")
# answer5 = "10"
# points = 0
#
# if question1 == answer1:
#     points += 10
#     logging.info(f"10 point added and is now {str(points)}")
# if question2 == answer2:
#     points += 10
#     logging.info(f"10 point added and is now {str(points)}")
# if question3 == answer3:
#     points += 10
#     logging.info(f"10 point added and is now {str(points)}")
# if question4 == answer4:
#     points += 10
#     logging.info(f"10 point added and is now {str(points)}")
# if question5 == answer5:
#     points += 10
#     logging.info(f"10 point added and is now {str(points)}")
#
# print (points)
#

#4 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა
# უნდა უპასუხოს ყველა შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.
#
# import logging
# logging.basicConfig(filename="quiz.log" , level=logging.INFO)
#
# def question_gen ():
#
#     answer1 = input("question1?")
#     logging.info (f"pasuxia {answer1}")
#     yield answer1
#
#     answer2  = input("question2?")
#     logging.info(f"pasuxia {answer2}")
#     yield answer2
#
#     answer3  = input("question3?")
#     logging.info(f"pasuxia {answer3}")
#     yield answer3
#
#     answer4  = input("question4?")
#     logging.info(f"pasuxia {answer4}")
#     yield answer4
#
#     answer5  = input("question5?")
#     logging.info(f"pasuxia {answer5}")
#     yield answer5
#
# x = question_gen()
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

#5 შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი
# შემთხვევითობის პრინციპით ირჩევს ამ სამიდან 1-ს , ასევე ტერმინალში მომხმარებელი წერს ერთ-ერთს, ერთნაირის შემთხვევაში ფრეა
# და გრძელდება თამაში 3-მდე, ვინც პირველი მიაღწევს 3-ს გამოიტანე შეტყობინება …..-მ გაიმარჯვა.

import random
points = 0
mylist = ["qva","bade","makrateli"]

pc1 = random.choice(mylist)
pc2 = random.choice(mylist)
pc3 = random.choice(mylist)

# for i < points:
#     if pc1 == input("first try"):
#         points +=1
#
#
# print(pc1)







#6 პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2, თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ,
# თუ ფრეა ვიმეორებთ, სხვა შემთხვევაში მოგებული მოთამაშე გამოგვაქვს ტერმინალში.


#დავალება მოამზადეთ მხოლოდ 1 ფაილში და ისე ატვირთეთ, გამოიყენეთ PEP8 სტანდარტი და მიჰყევით მხოლოდ ამოცანის პირობას.
# (აიტანეთ გითჰაბზე და დავალების ველში დატოვეთ რეპოზიტორიის მისამართი).
