first_word = "cookie"
second_word = "Cookie"

# These if statements are case sensitive

if first_word == second_word:
    print("\nYes")

if first_word != second_word:
    print("\nFirst_word is not equal to second_word")

# This conditional statement should be case insensitive
if first_word.lower() == "cookie":
    print("\nFirst_word passes the insensitive test")

if 4 == 4:
    print("\n4 passes the equality test")

if 4 != 4:
    print("\nThis will never be printed because the statement returns false and thus this print statement never exists")

if 4 >= 3:
    print("\n4 is bigger than 3")

if 4 <= 5:
    print("\n4 is smaller than 5")
    
if 3 < 5 and 4 < 5:
    print("\nThe and operator works")

if 3 < 4 or 5 < 4:
    print("\nThe or operator works")
# I really like these games.
first_list = ['FNAC','TJOC','POPGOES']

if "FNAC" in first_list:
    print("\nYes, FNAC is in the list.")

if "cookies" not in first_list:
    print("\nUnfortunately, there aren't any cookies in the FNAF Fangame Initiative :(")