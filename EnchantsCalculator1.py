# 15 xp per tier 1 book upgraded
# 35 xp per tier 2 book upgraded
# 65 xp per tier 3 book upgraded
# 90 xp per tier 4 book upgraded
# 120 xp per tier 5 book upgraded
# 160 xp per tier 6 book upgraded
# tier 7 unknown currently

TierBook = int(input("what tier book are you planning to use? "))
TotalXP = int(input("how much total xp needed for next level? "))

if TierBook == 1:
    print(round((TotalXP / 15)), "Upgrades needed to upgrade all the way to next level")
    
elif TierBook == 2:
    print(round((TotalXP / 35)), "Upgrades needed to upgrade all the way to next level")
        
elif TierBook == 3:
    print(round((TotalXP / 65)), "Upgrades needed to upgrade all the way to next level")
            
elif TierBook == 4:
    print(round((TotalXP / 90)), "Upgrades needed to upgrade all the way to next level")

elif TierBook == 5:
    print(round((TotalXP / 120)), "Upgrades needed to upgrade all the way to next level")

elif TierBook == 6:
    print(round((TotalXP / 160)), "Upgrades needed to upgrade all the way to next level")

else:
    print("Tier provided is either non existed or tier 7 was specified. Tier 7 is currently unknown but will be updated when found.")
    