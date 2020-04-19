condition = True

while condition :
    print ('Enter Your Name : ', end='')
    yourname = str(input())
    print ('Halo ' + yourname + ', again (Y/N) ? ', end='')
    answer = str(input()).upper()
    if answer == 'Y' :
        continue
    else :
        condition = False
        break