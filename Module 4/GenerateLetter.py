
def generate_letter():
    current = 97
    while True:
        yield (chr(current))
        current += 1
        if current == 102:
            current = 97

if __name__ == "__main__": 
    letter_generator = generate_letter()

    for i in range(0,10):
        print(next(letter_generator))