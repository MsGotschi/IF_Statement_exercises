user_location = input("Where do you live? ")
user_age = input("How old are you? ")
if int(user_age)<19 and user_location.lower() == "london":
	print("You are eligable for an oyster!")
else:
	print("Sorry, you are not eligable for an oyster.")

