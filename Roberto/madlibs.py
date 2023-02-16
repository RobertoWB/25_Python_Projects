# String concatenation (aka how to put string together)
# Suppose we want to create a string that says "subscribe to ______"
youtuber = "Roberto Wong" # Some string variable 

# A few ways to do this 
print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")


adj = input("Adjective")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Fampus person: ")

madlib = f"Computer programming is so {adj}! It makes me so exccited all the time because\
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

