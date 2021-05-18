from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if question['answer'] == answer else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    correctoption=ques['answer']
    optiontodelete1=0
    optiontodelete2=0
    if correctoption==1:
        optiontodelete1=2
        optiontodelete2=3
    elif correctoption==2:
        optiontodelete1=1
        optiontodelete2=3
    elif correctoption==3:
        optiontodelete1=1
        optiontodelete2=2
    elif correctoption==4:
        optiontodelete1=2
        optiontodelete2=3
    #deleting option from dictionary
    del ques['option{}'.format(optiontodelete1)]
    del ques['option{}'.format(optiontodelete2)]

    return ques

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    lifeline=1
    totalmoney=0
    round=0
    while(round<15):
        print(f'\tQuestion {round+1}: {QUESTIONS[round]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[round]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[round]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[round]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[round]["option4"]}')
        
        ans = input('Jawab dene ke liye ( 1-4 ) , lifeline lene ke liye (Y): ').lower()
        if lifeline==1:
            if ans=='y':
                newdic=lifeLine(QUESTIONS[round])
                a=list(QUESTIONS[round].keys())
                print(f'\t\t\t{a[1]} : {QUESTIONS[round][f"{a[1]}"]}')
                print(f'\t\t\t{a[2]} : {QUESTIONS[round][f"{a[2]}"]}')
                ans=int(input(f'{a[1]} or {a[2]} in (1-4): '))
                    
                
        

        # check for the input validations

        if isAnswerCorrect(QUESTIONS[round], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            totalmoney+=QUESTIONS[round]['money']
            print(f'\nSahi Jawab,aap jeet te hai {totalmoney} rs')
            if round==4: 
                print(f'\n Isi ke saath pehla padhaav samapt')
            elif round==10:
                print(f'\n Isi ke saath aapne dusra padhav paar kar liya hai')  

        else:
            # end the game now.
            # also print the correct answer
            correct=QUESTIONS[round]['answer']
            print('\n O oo ooh Galat Jawab !')
            print(f'\n Sahi option {correct} tha')
            break
        round+=1
        # print the total money won in the end.
    if round==15:
        print(f'Aap Jit te hai {totalmoney} rs kya kijeyaga is dhanraashi ka?')
    elif round<4:
        print('Koi baat nahi mahashay agli baar double mehnat karke aaye')
    elif 10>round>=4:
        print('Ye 10000 rs seedha aapke bank mein transfer kardeta hun Devsnest bank ki app se')
    else:
        print('Ye 3,20,000 axis bank ki app se seedhe aapke account mein.')

kbc()
