quiz = {
    "What is Kenya's largest Mountain" : "MT.kenya",
    "Who is Kenya's current President" : "Dr.William Ruto",
    "How many Countries are in Africa" : "Fifty six"
}
score = 0

for questions, answer in quiz.items():
    user_answer = input(questions + " ")

    if user_answer.lower() == answer.lower():
        print('Correct')

        score += 1
    else:
        print("Incorrect, the correct answer is " + answer + ".")