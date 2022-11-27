import pickle

def save_dictionary(my_input: dict) -> bool:
    with open("save.pickle") as f:
        pickle.dump(f, my_input)
    return True

def load_dictionary(name: str) -> dict:
    with open(name) as f:
        return pickle.load()

test = {1: 2, 3: 4}
save_dictionary(test)
print(load_dictionary("save.pickle"))