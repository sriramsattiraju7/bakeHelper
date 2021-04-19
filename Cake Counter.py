import math
eggs = int(input("The number of eggs is: "))
flour = int(input("The number of flour in cups is: "))
sugar = int(input("The number of sugar in cups is: "))
eggsCake = True
flourCake = True
sugarCake = True
 
if eggs >= 3:
    eggsCake = True
else:
    eggsCake = False
    print("You need", 3 - eggs, "more egg(s) to make one cake.")
if flour >= 2:
    flourCake = True
else:
    flourCake = False
    print("You need", 2 - flour, "more cup(s) of flour to make one cake.")
if sugar >= 2:
    sugarCake = True
else:
    sugarCake = False
    print("You need", 2 - sugar, "more cup(s) of sugar to make one cake.")
    exit()
    
dividedEggs = math.floor(eggs/3)
dividedFlour = math.floor(flour/2)
dividedSugar = math.floor(sugar/2)
cakeAmountArray = [dividedEggs, dividedFlour, dividedSugar]
minimumCake = min(cakeAmountArray)
print("You have", dividedEggs, "portion(s) of eggs for a cake.")
print("You have", dividedFlour, "portion(s) of flour for a cake.")
print("You have", dividedFlour, "portion(s) of sugar for a cake.")
print("The amount of cakes that you can make is:", minimumCake)
if minimumCake > 0:
    print("After making", minimumCake, "cake(s), you will have", minimumCake - minimumCake, "portion(s) of eggs,", dividedFlour - minimumCake, "portion(s) of flour, and", dividedSugar - minimumCake, "portion(s) of sugar left after baking your cake.")
else:
    exit()
    
