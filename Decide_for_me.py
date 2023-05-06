import random
print(
    """
    # # # # # # # # # # # # #
    $                       $
    $     DECIDE FOR ME     $
    $                       $
    # # # # # # # # # # # # #
                Try me, tough guy!
    """)

print("How many options you have?")
number_of_options = int(input())

presents_list = []

while number_of_options != 0:
    option = input("Option: ")
    presents_list.append(option)
    number_of_options -= 1

# print(presentslist)
dice = random.choice(presents_list)
print("Fate decided that it would be: ", dice)

print("\n\nWhat now?"
      "\n1: Ah, I preferred something else, draw again...."
      "\n2: We're done.")
choice = input("I'm choosing: ")

if choice == "1":
    dice = random.choice(presents_list)
    print("Fate decided that it would be: ", dice)
else:
    print("Good bye!")
input("\n\nHit Enter to quit.")
