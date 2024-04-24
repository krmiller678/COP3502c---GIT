import sys
from heifer_generator import HeiferGenerator
from dragon import Dragon
from ice_dragon import IceDragon

def list_cows(cows):
    # use for loop for cow in cows
        # print the name of the cow with cow.name
    
    print('Cows available:', end = ' ')

    for cow in cows:
        print(cow.name, end = ' ')


def list_file_cows(file_cows):
    # use for loop for cow in cows
        # print the name of the cow with cow.name
    
    print('\nFile cows available:', end = ' ')

    for cow in file_cows:
        print(cow.name, end = ' ')
        


def find_cow(name, cows):
    # iterate through cows and look at the name key
        # if equal return cow, if not equal return None amd print error message
    for cow in cows:
        if name == cow.name:
            return cow
        
    print(f'Could not find {name} cow!')
    return None


def find_file_cow(name, file_cows):
    # iterate through file_cows and look at the name key
        # if equal return cow, if not equal return None amd print error message
    for cow in file_cows:
        if name == cow.name:
            return cow
        
    print(f'Could not find {name} cow!')
    return None


if __name__ == '__main__':

    #print(sys.argv)
    cows = HeiferGenerator.get_cows()
    file_cows = HeiferGenerator.get_file_cows()

    if sys.argv[1] == '-l':
        # call list_cows(cows) 
        list_cows(cows)
        #call list_file_cows
        list_file_cows(file_cows)


    elif sys.argv[1] == '-n':
        # call find_cow(sys.argv[2], cows)
        cow = find_cow(sys.argv[2], cows)

        if cow != None:
            # print the message from sys.argv[3]
            for i in sys.argv[3:]:
                print(i, end = ' ')
            # print the cow.image
            print('\n', cow.image)
            try:
                if cow.can_breathe_fire() == True:
                    print("This dragon can breathe fire.")
                elif cow.can_breathe_fire() == False:
                    print("This dragon cannot breathe fire.")
            except:
                pass

    elif sys.argv[1] == '-f':
        # call find_cow(sys.argv[2], cows)
        cow = find_file_cow(sys.argv[2], file_cows)

        if cow != None:
            # print the message from sys.argv[3]
            for i in sys.argv[3:]:
                print(i, end = ' ')
            # print the cow.image
            print('\n', cow.image)
            
    else:
        #print message
        for i in sys.argv[1:]:
            print(i, end = ' ')

        print('\n',cows[0].image)