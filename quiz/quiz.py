print('Welcome to The Quiz')

playing=input('Do you want to play? ')

if playing.lower()!='yes':
    quit()
    
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for i in questions:
       
        print(i)
        for k in options[question_num-1]:
            print(k)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(i), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    
    print("RESULTS")
    

    print("Answers: ", end="")
    for j in questions:
        print(questions.get(j), end=" ")
    print()

    print("Guesses: ", end="")
    for j in guesses:
        print(j, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions = {
 "Who created Python?: ": "A",
 "What is the maximum length of a Python identifier": "D",
 "Which state has the largest area?: ": "A",
 "Which state has the largest population?: ": "B",
 "How is a code block indicated in Python?": "B",
 "Is the Earth round?: ": "A",
 "What is a correct syntax to output Hello World in Python?": "D"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 32", "B. 16", "C. 128", "D. No Fixed Length"],
          ["A. Maharashtra", "B. Madhya Pradesh", "C. Uttar Pradesh", "D. Rajasthan"],
          ["A. Maharashtra", "B. Madhya Pradesh", "C. Uttar Pradesh", "D. Rajasthan"],
          ["A. Brackets", "B. Indentation", "C. Key", "D. None of the above"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"],
          ["A. p(Hello World)","B. echo(Hello World)","C. write(Hello World)","D. print(Hello World)"]]

new_game()

while play_again():
    new_game()

print("Bye!")