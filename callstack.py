def funtion_three():
    print("three")

def funtion_two():
    funtion_three()
    print("two")

def funtion_one():
    funtion_two()
    print("one")

funtion_one()    