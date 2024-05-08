def rand():
    import random

    greeting = ["bonjour", "hello", "bonsoir", "salut", "ca va"]
    number = random.randrange(0, 5)
    print(greeting[number])


rand()

def dataType(x):
    x = type(x)
    return x


name = dataType('prospe')
print(name);


def dataType(x):
    x = type(x)
    return x


name = dataType(112882)
print(name)
