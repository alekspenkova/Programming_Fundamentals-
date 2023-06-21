event = input()

coffees = 0

event_lower = ['coding', 'movie', 'dog', 'cat']
event_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while event != 'END':

    if event in event_lower:
        coffees += 1
    elif event in event_upper:
        coffees += 2

    event = input()

    if event == 'END':
        if coffees > 5:
            print('You need extra sleep')
        else:
            print(coffees)