def quiz():
    questions = [
        "What is the capital of France?\n(a) Paris\n(b) Berlin\n(c) London\n\n",
        "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n\n",
        "What is the name of the first man to walk on the moon?\n(a) Neil Armstrong\n(b) Buzz Aldrin\n(c) Yuri Gagarin\n\n",
        "Who is the author of 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) Mark Twain\n(c) Ernest Hemingway\n\n",
        "What is the name of the process by which plants make their own food?\n(a) Photosynthesis\n(b) Respiration\n(c) Fermentation\n\n"
    ]

    answers = [
        "a",
        "b",
        "a",
        "a",
        "a"
    ]

    score = 0
    for i, question in enumerate(questions):
        answer = input(question)
        if answer == answers[i]:
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect.\n")

    return score


def scoring_system(score):
    if score >= 4:
        return "A"
    elif score >= 3:
        return "B"
    elif score >= 2:
        return "C"
    elif score >= 1:
        return "D"
    else:
        return "F"


# Example usage
result = quiz()
print("You got " + str(result) + " out of 5 questions correct.")
print("Your grade is: " + scoring_system(result))
