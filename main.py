import os
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

print(30*'=')
print('WELCOME THE GAME')
print('LETS REGISTER')
print(30*'=')
name = str(input('Name: '))
age = str(input('Age: '))
nickname = str(input('Nickname: '))
print(30*'=')

limpar_terminal() 

print(30*'=')
print("Hello {}! Let's start?".format(nickname))
print(30*'=')

score = 0
print('RESPOND WITH 1 OR 2')
print('Current score: 0')
print()
print('QUESTION 1')
pergunta1 = int(input('What of the capital of Brazil?  \n[1]Brasília or [2]Salvador\n '))
limpar_terminal()
if pergunta1 == 1:
    score += 1
    print('Correct Answer')
    print('CONGRATULATIONS!')
    print('Current score: {}'.format(score))
elif pergunta1 == 2:
    print('Incorret Answer')
    print('FAIL!')
    print('Current score: {}'.format(score))
    
print()
print('QUESTION 2')
pergunta2 = int(input('Who discovered Brazil?  \n[1]Pedro Álvares Cabral or [2]Luiz Inácio Lula\n '))
limpar_terminal()
if pergunta2== 1:
    score += 1
    print('Correct Answer')
    print('CONGRATULATIONS!')
    print('Current score: {}'.format(score))
elif pergunta2 == 2:
    print('Incorret Answer')
    print('FAIL!')
    print('Current score: {}'.format(score))
    
print()
print('QUESTION 3')
pergunta3 = int(input('What color of the coffe? \n [1]Red or [2]Black \n '))
limpar_terminal()
if pergunta3== 2:
    score += 1
    print('Correct Answer')
    print('CONGRATULATIONS!')
    print('Current score: {}'.format(score))
elif pergunta2 == 1:
    print('Incorret Answer')
    print('FAIL!')

    
    

