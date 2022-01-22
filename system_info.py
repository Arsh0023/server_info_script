import os
import pwd
import grp
import re

def write_to_file(*args):
    '''Function to wite text to info.txt'''
    with open('info.txt','a') as file:
        for inp in args:
            file.write(inp)

def re_wtf(word : str):
    '''Searches for the word in /proc/cpuinfo and writes the line to info.txt'''
    
    os.system('cat /proc/cpuinfo > temp.txt')

    for i,line in enumerate(open('temp.txt')):
        if re.search(word,line):
            write_to_file(line)
            break

    os.remove('temp.txt')

if __name__ == '__main__':

    if not os.path.exists('info.txt'):
        os.system('touch info.txt')

    flag = 0

    try:
        write_to_file('Machine name: ')
        os.system('hostname >> info.txt')
    except Exception as e:
        print('ERROR!')
        print(e)
        flag+=1
    #Adding Users to info.
    try:
        inp = '\nUsers : Groups\n'
        for p in pwd.getpwall():
            inp += (2*'\t' + p[0] + ' - ' + grp.getgrgid(p[3])[0] +'\n')
        write_to_file(inp)
    except Exception as e:
        print("ERROR!")
        print(e)
        flag+=1

    #Getting CPU info - Find the Line with the word then add that line to the final file.
    #If the teacher asks why dont you just note the Line number and add them, it may happen that 
    #Some proc files maybe designed differently thats why going with regex is better.
    try:
        write_to_file('\nInfo from the /proc/cpuinfo:-\n','\nProcessor: ')
        os.system('cat /proc/cpuinfo | grep processor | wc -l >> info.txt') #The Processor may not be equal to actual cores because of threading.

        to_search = ['vendor_id','model','model name','cache size']
        for i in to_search:
            re_wtf(i)

    except Exception as e:
        print('ERROR!')
        print(e)
        flag+=1

    try:
        write_to_file('\nServices in the syste and their status\n')
        os.system('systemctl list-units --type=service --all >> info.txt')
    except Exception as e:
        print('ERROR!')
        print(e)
        flag+=1

    if flag == 0:
        print('Execution successful!')
        print(f"Information copied to - {os.path.abspath('info.txt')}")
    
    if flag > 0 and flag < 4:
        print('Incomplete Execution!!!')
        print(f"Information copied to - {os.path.abspath('info.txt')}")

    if flag == 4:
        print('EXECUTION FAILED!')