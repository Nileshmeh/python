Questions = (("Abhijit Dipke is from which party?: "),
            ("Papa ji kaun hai?: "),
            ("What is our national fruit?: "),
            ("who's the current CM of West Bengal?: "),
            ("What is the Quizzer's name?: "),
            ("what are you?: "))

Options = (("A. CJP", "B. BJP", "C. CONGRESS", "D. TMC"),
           ("A. Modihh", "B. Aloo", "C. Ghas", "D. Jhadu"),
           ("A. Mango", "B. Banana", "C. Pinapple", "D. Lichhi"),
           ("A. Subhendu", "B. mamata", "C. dilip", "D. bhaipo"),
           ("A. anmol", "B. Surinder", "C. bhupinder", "D. tejvender"),
           ("A. student", "B. teacher", "C. proffessional", "D. unemployed")
           )


Answers = ("A", "A", "A", "A", "C", "D")
guesses = []
score = 0
question_num = 0

for question in Questions:
    print("-" * 40)
    print(question)
    for option in Options[question_num]:
        print(option)
    print()
    
    guess = input("what is your answer: ").upper()
    guesses.append(guess)
    if guess == Answers[question_num]:
        score += 1
        print("CORRECT!")
        print("you're answer is correct!")

    else:

        print("INCORRECT!")
        print(f"correct is option {Answers[question_num]}")


    question_num += 1

print("-" * 40)
print("      Result      ")
print("-" * 40)

print("Answers: ", end=" ")
for answer in Answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print("-" * 40)

score = int(score / len(Questions) * 100)

for i in range(len(Questions)):
    print(f"Q{i+1}: Your guess: {guesses[i]}  |  Answer: {Answers[i]}")


print("-" * 40)

if score >= 60:
    print(f"you did quite well")
    print(f"Your score is {score}%")

else:
    print("Better luck next time!")
    print(f'Your score is {score}%')



           
           
           
           
  