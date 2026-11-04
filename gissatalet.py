from random import randint

print("Hello, Guesser!")
while True:
    secret_number = randint(1, 10)
    guess = int(input("Ange ett tal mellan 1 - 10 --> "))

    print(f"Du gissade på {guess}.")
    if guess == secret_number:
        print(f"Rätt! Det hemliga talet var {secret_number}.")
    else:
        print(f"Fel! Det hemliga talet var {secret_number}.")

    again = input("Vill du spela igen? (ja/nej) --> ").lower()
    if again != "ja":
        print("Tack för att du spelade! Hej då!")
        break
    else:
        print("Okej, vi spelar igen!")
        continue
