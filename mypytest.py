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



