import random


def run_quiz():
    questions = [
        (
            "Vilken huvudstad har Sverige? \n 1. Oslo \n 2. Stockholm \n 3. Köpenhamn \n Skriv ditt svar --> ",
            {"2", "stockholm"},
        ),
        (
            "Vilken huvudstad har Norge? \n 1. Oslo \n 2. Bergen \n 3. Trondheim \n Skriv ditt svar --> ",
            {"1", "oslo"},
        ),
        (
            "Vilket år började andra världskriget? \n 1. 1939 \n 2. 1945 \n 3. 1914 \n Skriv ditt svar --> ",
            {"1", "1939"},
        ),
    ]
    random.shuffle(questions)

    points = 0
    print("Dags att quizza!")
    for question, correct_answers in questions:
        tries = 2
        while tries > 0:
            answer = input(question).strip().lower()
            if answer in correct_answers:
                print("Rätt!")
                points += 1
                break
            tries -= 1
            print(f"Fel! Du har {tries} försök kvar.")

    print(f"Du fick {points} av {len(questions)} poäng!")


if __name__ == "__main__":
    while True:
        run_quiz()
        again = input("Vill du spela igen? (ja/nej) --> ").lower()
        if again != "ja":
            print("Tack för att du spelade! Hej då!")
            break
        print("Okej, vi spelar igen!")