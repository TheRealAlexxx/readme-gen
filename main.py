import time

space=(' ')

def start():
    print('welcome to the README generator! DO NOT answer these in full sentences!')
    title=input('please enter your project name/title: ')
    print('okay! your title is now: ' +title )
    summary=input('now, please enter a small summary of your project. this should be only 1-2 sentences: ')
    print('okay! your summary is now: ' +summary)
    what_langs_they_used=input('please enter what languages you used to make this: ')
    print('okay! you used ' +what_langs_they_used ' to make this project')
    what_hackclub_program=input('please emter what hack club program you made this project for. if you did not make your project for a hack club program, respond to this with \'none\':')
    if what_hackclub_program == 'none' or 'None':
        print('okay! you didnt ship this for a hack club program.')
    else:
        print('okay! you shipped this to ' +what_hackclub_program)
    name=input('finally, please enter your name: ')
    concatonation()

def concatonation():
    print('okay ' +name ', im generating your README now! please wait...')
    readme=('#' +title)
    readme+=('\n\n')
    readme+=('i made ' +summary)
    readme+=('\n')
    readme+=('i used: ' +what_langs_they_used)
    if what_hackclub_program != 'none' or 'None':
        readme+=('this was built for the hack club program \''+what_hackclub_program + '\')
    readme+=('built with <3 by ' +name)
finale()

def finale():
    time.sleep(2)
    print('okay ' +name '! heres your README: \n\n')
    print(readme)
    time.sleep(2)
    print('\n\n')
    print('i hope you like your readme!')