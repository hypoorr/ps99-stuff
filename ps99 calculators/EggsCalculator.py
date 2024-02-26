TotalXP = int(input("Total Xp needed to level up? "))
ViewMore = False

print(round((TotalXP / 20)), "hatches needed")

ViewMore = str(input("View time taken? (not 100% accurate) yes/no "))

if ViewMore == "yes":
    print("an estimated time of about", ((TotalXP / 20)*3.6), "seconds")

while True:
    True


