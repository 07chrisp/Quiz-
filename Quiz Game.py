#10/18/25 Quiz Game

incorrect=0
correct=0
correct_answers=("C","B","D","A","D","C")


start=int(input('Welcome to my quiz game. Enter 1 to begin: '))
while start != 1:
    start=int(input('Welcome to my quiz game. Enter 1 to begin: '))
#if you hit spacebar or leave it empty it counts
#as an answer it counts as correct. fix it
if start == 1:
    Q1=input('What year was the last time the Mets won the World Series?\nA. 2015\nB. 1989\nC. 1986\nD. 1969\nEnter your answer: ')
    if Q1 in correct_answers[0]:
        correct+=1
    else:
        incorrect+=1
    Q2=input('When was the last year that the Mets made the playoffs?\nA. 2025\nB. 2024\nC. 2019\nD. 2015\nEnter your answer: ')
    if Q2 in correct_answers[1]:
        correct+=1
    else:
        incorrect+=1
    Q3=input('Who is the Mets all-time HR leader?\nA. Dwight Gooden\nB. Tom Seaver\nC. David Wright\nD. Pete Alonso\nEnter your answer: ')
    if Q3 in correct_answers[2]:
        correct+=1
    else:
        incorrect+=1
    Q4=input('Who is the Mets all-time ERA leader?\nA. Jacob deGrom\nB. Tom Seaver\nC. Dwight Gooden\nD. John Franco\nEnter your answer: ')
    if Q4 in correct_answers[3]:
        correct+=1
    else:
        incorrect+=1
    Q5=input('Who won the 2023 World Series?\nA. New York Mets\nB. Arizona Diamondbacks\nC. Philadelphia Phillies\nD. Texas Rangers\nEnter your answer: ')
    if Q5 in correct_answers[4]:
        correct+=1
    else:
        incorrect+=1
    Q6=input('How many World Series Championships have the Mets won?\nA. 0\nB. 3\nC. 2\nD. 1\nEnter your answer: ')
    if Q6 in correct_answers[5]:
        correct+=1
    else:
        incorrect+=1

average=(correct/6)*100
print(f'Correct: {correct}\nIncorrect: {incorrect}\nAverage: %{average:.2f}')
