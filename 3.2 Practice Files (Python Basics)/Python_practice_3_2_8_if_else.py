#What is the score?
score = int(input("What score did you recieve on the test?"))
if score>=90:
    print("Congratulations, you recieved an 'A'")
else:
    if score>=80:
        print("Well done, you recieved a 'B'")
    else:
        if score>=70:
            print("Good job, you recieved a 'C'")
        else:
            if score>=60:
                print("You recieved a 'D'")
            else:
                print("You recieved an 'F'. Better luck next time.")
