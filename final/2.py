

points = int(input("Please enter your points: "))
if points <= 49:
    print("Ваша оцінка: незадовільно.")
elif points <= 69:
    print("Ваша оцінка: задовільно.")
elif points <= 89:
    print("Ваша оцінка: добре.")
else:
    print("Ваша оцінка: відмінно.")