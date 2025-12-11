# #1 დაწერეთ პაროლის გენერატორი.
# დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list, სტრიქონის ფორმატირება.
#
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”
#
# **უნდა გვქონდეს 4 ინფუთი - სიგრძე / რიცხვები უნდა თუ არა / დიდი და პატარა ასოები თუ უნდა / თუ უნდა სიმბოლოები
#
# **უნდა დაწეროთ ლოგიკა იმის მიხედვით რასაც აირჩევს მომხმარებელი და ბოლოს დაუგენერიროთ პაროლი.
# import random
# import string
#
# pwdlenght = input("შეიყვანეთ სიგრძე (number)")
# pwdnumbers = input("შეიცავდეს რიცხვებს (yes/no)")
# pwdalphabet = input("შეიცავდეს დიდ და პატარა ასოებს (yes/no)")
# pwdsymbols = input ("შეიცავდეს სიმბოლოებს (yes/no)")
# symbolstochoose = ""
# pwd = ""
# i=0
# while i < int(pwdlenght):
#     if pwdnumbers == "yes":
#         symbolstochoose = string.digits
#     if pwdalphabet == "yes":
#         symbolstochoose = symbolstochoose + string.ascii_letters
#     if pwdsymbols == "yes":
#         symbolstochoose = symbolstochoose + string.punctuation
#
#     pwd = pwd + random.choice(symbolstochoose)
#     i += 1
#
# print(f"{pwd}")
# # #2 დაწერე ფუნქცია (ფიბონაჩის რიგი) - რა არის ფიბონაჩი - ბოლო ორი ელემენტის ჯამით ვამატებთ ახალ რიცხვს,
# # სანამ სიგრძე არ გახდება მომხმარებლის მიერ შემოყვანილი რიცხვი, აუცილებლად უნდა შემოიტანოს რიცხვი,
# # სხვა რამის შემოტანის დროს უნდა შემოწმდეს რა შემოიტანა მომხმარებელმა და უნდა
# # დაუსახელო აღნიშნული და უთხრა რომ მხოლოდ რიცხვი შემოიტანოს.
# # მაგ: შემოიტანა სიმბოლო, უნდა უთხრა შენ შემოიტანე სიმბოლო არასწორია, მხოლოდ რიცხვი!
# #from os.path import split
#
# length = input("შემოიტანე რიცხვი ")
# while not length.isdigit():
#         print(f"შენი შემოტანილი სიმბოლო არასწორია {type(length)}")
#         length = input("შემოიტანე რიცხვი ")
#
# fibolist = [0, 1 ]
# while len(fibolist) < int(length):
#     fibolist.append(fibolist[-1] + fibolist[-2])
# print (fibolist)
#
# #3 ზედმეტსახელების გენერატორი
# #მომხმარებელს შემოაქვს მხოლოდ ერთი სიტყვა(სხვა შემთხვევები დაბლოკე) და შენ სთავაზობ 5 ზედმეტსახელს ამ სიტყვასთან კავშირში.
# myname = input("გთხოვთ შემოიყვანოთ ერთი სიტყვა: ")
# while len(myname.split()) > 1:
#         myname = input("გთხოვთ შემოიყვანოთ ერთი სიტყვა!: ")
# addonwords = ["წითელი", "მაღალი", "შავტუხა", "მორბენალი", "პროგრამისტი"]
#
# i = 0
#
# while i < 5:
#
#     print(f"{addonwords[i]} {myname}")
#     i += 1
#

# #4 სორტირება
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა)
# პროგრამა სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად ან მხოლოდ უნიკალური მონაცემები დატოვოს.
# რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე დალაგებული სია.
import random
mynumbers = []
usernumber = input("Enter a number: ")
while usernumber != "end":
    mynumbers.append(int(usernumber))   #რადგან ტექსტად კი არა რიცხვებად დასორტილიყო
    usernumber = input("Enter a number again or write 'end': ")

sorttype = input("how do you want to sort? (asc, desc, ran, uni: )")
if sorttype == "asc":
    mynumbers.sort()
    print(mynumbers)
elif sorttype == "desc":
    mynumbers.sort(reverse=True)
    print(mynumbers)
elif sorttype == "ran":
    random.shuffle(mynumbers)
    print(mynumbers)
elif sorttype == "uni":
    print(set(mynumbers))

#
# #5 ტექსტის ფილტრი
# მომხმარებელი შეჰყავს ტექსტი.
# ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და სივრცეები.

import string
text = input("შეიყვანეთ დასამუშავებელი ტექსტი:")
letterlist = string.ascii_letters


i=0
while i < len(text):
    if text[i] not in letterlist and text[i] != " ":
       text = text.replace(text[i], "")
    i += 1
print(text)
##### ვერ მივხვდი მაგალითდ asd222! შემთხვევაში ბოლოში და მიტოვებს ! მაგრამ !asd222! შემთხვევაში სწორად მუშაობს

# #6 პირამიდა
# მომხმარებელს შეჰყავს რიცხვების სია (მაგ. 3,5,7,2).
# ა მოცანა: შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთაა წინა ორი რიცხვის ჯამი.
#
# 3  5  7  2
#  8 12  9
#  20 21
#  41

def myfunction(*args):
    mylist = list(args)
    print(mylist)
    for a in range(len(mylist) - 1):
        for i in range(len(mylist) - 1):
            mylist[i] = (mylist[i] + mylist[i + 1])
        del mylist[-1]
        print(mylist)

print(myfunction(3, 5, 7, 2, 22, 12, 33, 1, 4))

######## პირველადი ვარიანტი######
## def myfunction (*args):
##      mylist = list(args)
##     print(mylist)
##      for i in range(len(mylist) - 1):
##          mylist[i] = (mylist[i] + mylist[i + 1])
##      del mylist[-1]
##      print(mylist)
##      for i in range(len(mylist)-1):
##          mylist[i] = (mylist[i]+mylist[i+1])
##      del mylist[-1]
##      print(mylist)
##     for i in range(len(mylist)-1):
##          mylist[i] = (mylist[i]+mylist[i+1])
##      del mylist[-1]
##      print(mylist)
##
## print(myfunction(3,5,7,2,22 ))
#
#
# #7 მომხმარებელს შეჰყავს წინადადება, ამოცანა: გამოიანგარიშე თითოეული სიტყვის სიგრძე და დააბრუნე dictionary
# მაგალითად: "Python is fun" → {"Python": 6, "is": 2, "fun": 3}

# text = input("შეიყვანეთ წინადადება: ")
# text = text.split()
# textlist = list(text)
# lengthlist = []
# mydict = {}
# for i in range(len(textlist)):
#     lengthlist.append(len(textlist[i]))
# for a in range(len(textlist)):
#     mydict[textlist[a]] = lengthlist[a]
# print(mydict)

# # შექმენით გითჰაბზე რეპოზიტორია, დაკლონეთ ედიტორში, 1,2,3 ამოცანის ამოხსნის შემდეგ მთავარ ბრენჩზე გააკეთე დამატება , კომიტი და აიტანე გითჰაბზე ეს სამი ამოცანა,
# შემდეგ გააგრძელე მუშაობა, გააკეთე ახალი ბრენჩი სახელად “secondbranch” 4,5,6 ამოცანა ამოხსენი ამ ბრენჩზე და აიტანე გითჰაბზე,
# გააკეთე ფულ რექუესთი და დამერჯე მთავარ ბრენჩზე (main)-ზე. შემდეგ გააკეთე მესამე ბრენჩი “thirdbranch” გააკეთე დარჩენილი
# ამოცანები და აიტანე გითჰაბზე ანალოგიურად, ფულ რექუესთი და დამერჯე მეინზე.
#
# აუცილებლად გადაიღეთ სქრინები რასაც დაწერთ ტერმინალში თანმიმდევრობით და მიაბით დავალებასთან ერთად, ასევე გამიზიარეთ რეპოზიტორიის მისამართი.


#

