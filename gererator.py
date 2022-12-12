import string
from random import choice
i_data = ["a", "b", "c"]

def custom_random(init_data):

    initial_data = init_data.copy()
    while True:
        if not initial_data:
            break
        data = choice(initial_data)
        initial_data.remove(data)
        print(initial_data)
        yield data
        #print("continue")

gen = custom_random(i_data)
print(next(gen))
print(next(gen))
print(next(gen))

gen_1 = custom_random(i_data)
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
