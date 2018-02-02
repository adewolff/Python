'''Imports suess.txt, and turns all i into I where appropriate,
   then writes it to a new txt file'''
def main():
    importer()

def importer():
    '''Imports suess.txt, and turns all i into I where appropriate,
       then writes it to a new txt file'''

    suess = open('suess.txt', 'r')
    content = suess.read()
    content = content.replace('i ', 'I ')
    content = content.replace('i-', 'I-')
    print(content, file=open('suess_fix.txt', 'w'))

if __name__ == '__main__':
    main()
