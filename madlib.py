# # # string concatenation (aka how to put strings together)
# # # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Mehul" # some string variable
# print("Subcribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
adj = input("Adjective :  ")
verb1 = input("Verb : ")
verb2 = input("Verb : ")
famous_person = input("Famous Person : ")
madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because\
I love to {verb1} . Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)