import time

def after_usage():
    print('okay! usage section finished')

def main_program():
    print('welcome to the README generator! DO NOT answer these in full sentences!')
    title=input('please enter your project name/title: ')
    print('okay! your title is now: ' +title )
    summary=input('now, please enter a small summary of your project. this should be only 1-2 sentences: ')
    print('okay! your summary is now: ' +summary)
    what_langs_they_used=input('please enter what languages you used to make this: ')
    print('okay! you used ' + what_langs_they_used + ' to make this project')
    what_hackclub_program=input('please enter what hack club program you made this project for. if you did not make your project for a hack club program, respond to this with \'none\':')
    if what_hackclub_program == 'none' or what_hackclub_program == 'None':
        print('okay! you didnt ship this for a hack club program.')
    else:
        print('okay! you shipped this to ' +what_hackclub_program)
    demo=input('would you like to have a demo link?')
    if demo == 'yes' or demo == 'Yes':
        demo_link=input('please enter your demo link: ')
        while not (demo_link.startswith('https://') or demo_link.startswith('https://')):
            print('invalid link. please provide https://')
            demo_link=input('please enter your demo link: ')
        print('okay! your link is valid')

    def usage_count():
        usage_number=1
        while usage_number <= 10:
            usage=input(str(usage_number) + '. ')
            if usage == 'done' or usage == 'Done':
                break
            usage_number+=1
        print('okay!')

    usage=input('would you like to add a usage section?: ')
    if usage == 'yes' or usage == 'Yes':
        print('okay! add steps to how people need to use it. you have a maximum of 10 steps. reply to the step after the one that you have finished on with "done"')
        usage_count()
    else:
        print('okay! usage will not be a section in your readme.')

#   usage=input("would you like a usage section?: ')
#   if usage == 'yes' or usage == 'Yes':
#     print('okay! usage is a bit more complicated. this time, you have steps that you need to use. you have maximum 10 steps, but you probably wont use them all. just type "done" in the step once you have done, and it will stop.')
#       time.sleep(2)
#       usage1=input('1. ')
#       print('okay! the first step is: ' +usage1)
#       if usage1 == 'done' or usage1 == 'Done':
#           after_usage()
#       usage2=input('2. ')
#       print('okay! the second step is: ' +usage2)
#       usage3=input('3. ')
#       print('okay! the third step is: ' +usage3)
#       usage4=input('4. ')
#       print('okay! the fourth step is: ' +usage4)
#       usage5=input('5. ')
#       print('okay! the fith step is: ' +usage5)
#       usage6=input('6. ')
#       print('okay! the sixth step is: ' +usage6)
#       usage7=input('7. ')
#       print('okay! the seventh step is: ' +usage7)
#       usage8=input('8. ')
#       print('okay! the eighth step is: ' +usage8)
#       usage9=input('9. ')
#       print('okay! the ninth step is: ' +usage9)
#       usage10=input('10. (this is your final step)')
#       print('okay! the tenth step is: ' +usage10)
        

    name=input('finally, please enter your name: ')
    print('okay ' + name + ', im generating your README now! please wait...')
    print('\n\n')

    readme=('# ' +title)
    readme+=('\n')

    readme+=('## about')
    readme+=('\n')
    readme+=('i made ' +summary)
    readme+=('\n')

    if demo == 'yes' or demo == 'Yes':
        readme+=('## demo')
        readme+=('\n')
        readme+=('this is the demo link: ' +demo_link)
        readme+=('\n\n')

    readme+=('## what i made it with')
    readme+=('\n')
    readme+=('i used: ' +what_langs_they_used)
    readme+=('\n')

    if what_hackclub_program != 'none' and what_hackclub_program != 'None':
        readme+=("this was built for the hack club program '" + what_hackclub_program + "'")
        readme+=('\n')
    readme+=('built with <3 by ' +name)
    time.sleep(2)
    print('\n\n')
    print('okay ' + name + '! heres your README: \n\n')
    print(readme)
    time.sleep(2)
    print('\n\n')
    print('i hope you like your readme!')

main_program()