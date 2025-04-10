# This is a program that creates quizzes
while True: # A loop that allow user to input many questions 
    quiz_question = input("Enter a question: ") #Ask the user the questions they want to input
    # These are the choices or possible answers to the question
    letter_a = input("Enter letter a: ")
    letter_b = input("Enter letter b: ")
    letter_c = input("Enter letter c: ")
    letter_d = input("Enter letter d: ")

    while True: # This is a nested loop to validate correct answer
        correct_ans = input("What letter is the correct answer? ")
        if correct_ans in ['a', 'b', 'c', 'd']:
            break  # Exit loop
        else:
            print("Invalid.") # The input shpould be a, b, c, d only

