# #1 შექმენი თამაში
# შექმენით Character კლასი (სახელი, სიცოცხლე, ძალა)
# გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer
# გამოიყენეთ super() რომ მშობლის კონსტრუქტორი გამოიძახოთ
# თამაში: ორი გმირი ებრძვის ერთმანეთს (attack() მეთოდი).
# Warrior სჯობს Mage-ს , Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს
# ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა
# დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი ვალიდაციები და
# პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.

# class Character:
#     def __init__(self, name, life, power):
#         self.name = name
#         self.life = life
#         self.power = power
#
# class Profession (Character):
#     def __init__(self, name, life, power, prof):
#         super().__init__(name, life, power)
#         self.prof = prof
#
#     def attack (self, other):
#         hero1 = self.prof
#         hero2 = other.prof
#
#         if hero1 == "Warrior" and hero2 == "Mage":
#             return self.name + " is winner"
#         if hero2 == "Warrior" and hero1 == "Mage":
#             return other.name + " is winner"
#
#         if hero1 == "Mage" and hero2 == "Archer":
#             return self.name + " is winner"
#         if hero2 == "Mage" and hero1 == "Archer":
#             return other.name + " is winner"
#
#         if hero1 == "Archer" and hero2 == "Warrior":
#             return self.name + " is winner"
#         if hero2 == "Archer" and hero1 == "Warrior":
#             return other.name + " is winner"
#
# attack_hero1 = Profession("joni", 1000, 500, "Warrior")
# attack_hero2 = Profession("gela", 1200, 400, "Mage")
#
# x = attack_hero1.attack(attack_hero2)
# print(x)

# #2 პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც:
# შექმენით Monster კლასი.
# დაამატეთ classmethod create_from_level(level), რომელიც ქმნის მონსტრს სიძლიერის
# მიხედვით.
# სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი.
# შექმენი მინიმუმ 10 მონსტრი რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული :)
# (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე” არაა საჭირო ზედმეტი ვალიდაციები და პირობის
# ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.
# import random
# class Monster:
#     def __init__(self, name, level = 0):
#         self.name = name
#         self.level = level
#     @classmethod
#     def create_level (cls, name):
#         x = cls(name)
#         x.level = random.randint(0, 10)
#         return x
#
#     def __str__(self):
#         return  f"{self.name} (Level {self.level})"
#
# obj = Monster.create_level("დევი")
# print(f"{obj}")


# #3 მარტივი კაზინო თამაში
# შექმენით SlotMachine კლასი.
# გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად.
# გამოიყენეთ classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები
# მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.
#
# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.




# #4 გმირის ქულების სისტემა
# შექმენით Hero კლასი.
# private health, private score.
# staticmethod random_event() -> შემთხვევითი მოვლენა (ქულა ემატება ან ჯანმრთელობა
# აკლდება).
#
# classmethod from_name(cls, name) -> ქმნის გმირს სახელით.
# მემკვიდრე SuperHero -> დამატებითი ძალა.
# super() გამოიძახეთ მშობლის კონსტრუქტორისთვის.
# თამაში გრძელდება სანამ გმირის health > 0.
#
# #5 პროგრამა კარტზე
# Card კლასი (rank, suit).
# Deck კლასი -> private cards list.
# classmethod create_standard_deck() აბრუნებს სტანდარტულ 52 კარტიან დასტას.
# staticmethod shuffle(cards) აურევს კარტებს.
# მოთამაშე იღებს 5 კარტს და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია” (მაგ: ორი ერთნაირი)
# აუცილებლად გატესტეთ კოდი, შეასრულეთ მხოლოდ პირობაში მოცემული ვარიანტი, არაა საჭირო
# დამატება.