import os
import pwd
import grp

def write_to_file(inp : str):
    '''Function to wite text to info.txt'''
    with open('info.txt','a') as file:
        file.write(inp)

#get the machine name:
if __name__ == '__main__':

    if not os.path.exists('info.txt'):
        os.system('touch info.txt')
    write_to_file('Machine name: ')
    os.system('hostname >> info.txt')

    #Adding Users to info.
    try:
        inp = '\nUsers : Groups\n'
        for p in pwd.getpwall():
            inp += (2*'\t' + p[0] + ' - ' + grp.getgrgid(p[3])[0] +'\n')
        write_to_file(inp)
    except Exception as e:
        print("ERROR!")
        print(e)

    #Getting CPU info
