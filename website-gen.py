import time

def readme_gen():
    print('welcome to the website generator!!')
    time.sleep(1)
    print('you will be asked a set of questions. please, DONT answer in full sentences. any questions that can be, please say yes or no as a response.')
    okay=input('are you with me so far?: ')
    if okay == 'yes' or okay == 'Yes':
        print('great! lets get started.')
        time.sleep(1)
    elif okay == 'no' or okay == 'No':
        print('i see. just try answer the questions as best as you can then.')
        time.sleep(1)
    else:
        print('please answer these sorts of questions with a simple yes or no. lets move on.')
        time.sleep(1)
    