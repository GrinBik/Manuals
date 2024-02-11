import pickle


class Cats:
    def __init__(self):
        self.name = 'Cat'
        self.color = 'black'

    def meow(self):
        print(f"{self.name} say: meow meow")


cat = Cats()
byte_cat = pickle.dumps(cat)
print(len(byte_cat))
