from question_class import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "What is bigger?\n(a) Elephant\n(b) Bird\n(c) Ant\n\n",
    "What is smaller?\n(a) Cat\n(b) Mouse\n(c) Horse\n\n",
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
    Question(question_prompts[3],"a"),
    Question(question_prompts[4],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.\n")

run_test(questions)