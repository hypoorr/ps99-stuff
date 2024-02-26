# tier 1 upgrade gives 10 xp
# tier 2 upgrade gives 25 xp
# tier 3 upgrade gives 45 xp
# tier 4 upgrade gives 70 xp
# tier 5 upgrade gives 100 xp
# tier 6 upgrade gives 140 xp
# tier 7 upgrade gives 190 xp
# tier 8 unknown currently

PotionTier = int(input("What potion tier will you be using? "))
TotalXP = int(input("What is the total amount of XP needed for the next level? "))

if PotionTier == 1:
    print(round((TotalXP / 10)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 2:
    print(round((TotalXP / 25)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 3:
    print(round((TotalXP / 45)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 4:
    print(round((TotalXP / 70)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 5:
    print(round((TotalXP / 100)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 6:
    print(round((TotalXP / 140)), "Upgrades needed to upgrade all the way to next level")

elif PotionTier == 7:
    print(round((TotalXP / 190)), "Upgrades needed to upgrade all the way to next level")


else:
    print("Tier provided is either non existed or XP value is unknown")

while True:
    True