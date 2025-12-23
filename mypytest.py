#4 pytest2
#
# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან
# pytest-ში გამოიყენეთ raises შეცდომის დასატესტად
#
# ნიმუში: raise ValueError
# import pytest
# mydict = {"user":"giga", "password":"mypass"}
#
# def autorization(userinp, passinp):
#     if mydict["user"] == userinp and mydict["password"] == passinp:
#         return "OK"
#     else:
#         raise ValueError("არასწორი მომხმარებელი ან პაროლი")
#
#
# def test_autorization_ОК():
#     assert autorization("giga","mypass") == "OK"
#
# def test_autorization_BAD():
#     with pytest.raises(ValueError):
#         autorization("giga","mypas")

# #5 pytest3
#
# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email (ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები
#
# import pytest
# def emailcheck (email):
#     if email.find("@") >= 0:
#         return "OK"
#     else:
#         raise ValueError("it is not email format")
#
# def test_email_OK():
#     assert emailcheck("giga@giga.ge") == "OK"
# def test_email_BAD():
#     with pytest.raises(ValueError):
#         emailcheck("noemailsymbol")


# #6 შექმენით თამაში HangMan - სადაც ცვლადში შეინახავთ სიტყვას და მომხმარებელს ექნება ასოების შემოტანის საშუალება, თუ
# გამოიცნობს სანამ ცდების რაოდენობა ამოიწურება გამოიტანე "თქვენ გამოიცანით სიტყვა" თუ ვერ გამოიცნობს და ამოეწურება ცდები
# გამოიტანე "თქვენ დამარცხდით". ამ ყველაფრისთვის გამოიყენეთ რომელიმე ტესტირების მოდული და გატესტეთ თქვენი დაწერილი კოდი.
# (აუცილებელია მომხმარებელმა შემოიტანოს მხოლოდ სტრინგი, სხვა მონაცემთა ტიპი უნდა ვუგულებელვყოთ).

import pytest

def hangman (my_word = "table",tries = 10, message = "თქვენ დამარცხდით"):
    for i in range(tries):
        user_word = input("გთხოვთ შეიყვანოთ სიტყვა: ")
        if user_word.isalpha():
            if my_word == user_word:
                message = "თქვენ გამოიცანით სიტყვა!"
                break
            else:
                print("კიდევ სცადეთ")
                tries -= 1
        else:
            raise ValueError("შეიყვანეთ მხოლოდ ანბანის სიმბოლოები")
    return message

# def test_alpha():
#     assert hangman() == "თქვენ გამოიცანით სიტყვა!" or hangman() == "თქვენ დამარცხდით"
# def test_nonalpha():
#     with pytest.raises(ValueError):
#         hangman()



