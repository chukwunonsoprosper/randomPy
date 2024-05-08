def rand():
    import random
    greeting = ['bonjour', 'hello', 'bonsoir', 'salut', 'ca va']
    number = random.randrange(0, 5)
    print(greeting[number])
rand()