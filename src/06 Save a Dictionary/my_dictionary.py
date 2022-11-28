import pickle

def save_dictionary(my_input: dict) -> dict:
    with open("save.pickle", "wb") as f:
        return pickle.dump(my_input, f)

def load_dictionary(name: str) -> dict:
    with open(name, "rb") as f:
        return pickle.load(f)

test = {1: 2, 3: 4}
save_dictionary(test)
print(load_dictionary("save.pickle"))