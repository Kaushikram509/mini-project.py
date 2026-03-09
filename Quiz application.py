user_input = input("Enter your value: ")
score = 0
quiz = {"capital of India" : "delhi", "Capital of pakistan": "Islamabad", "5 + 3" : "8", "capital of Telengana" : "Hyderabad"}
for key, value in quiz.items():
    if(user_input.lower()==value.lower()):
        print("Your answer is correct..")
        score += 1
        break
    else:
        print("Guess the answer again....")
        break
