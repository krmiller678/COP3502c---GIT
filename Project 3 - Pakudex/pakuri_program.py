"""
This is the Driver program - serves to 
1) Display Welcome Message
2) Prompt for / read pakudex capacity
3) Display the menu
4) Prompt for input
"""

from pakudex import Pakudex

def welcome_message():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    #while loop implemented to ensure value captured is valid
    while True:
        capacity = input('Enter max capacity of the Pakudex: ')
        if capacity.isdigit():
            capacity = int(capacity)
        else:
            print('Please enter a valid size.')
            continue
        print(f'The Pakudex can hold {capacity} species of Pakuri.')
        print()
        return capacity


def print_menu():
    print('Pakudex Main Menu\n'
          '-----------------\n'
          '1. List Pakuri\n'
          '2. Show Pakuri\n'
          '3. Add Pakuri\n'
          '4. Evolve Pakuri\n'
          '5. Sort Pakuri\n'
          '6. Exit\n')


if __name__ == '__main__':
    capacity = welcome_message()
    new_paku = Pakudex(capacity)
    while True:
        print_menu()

        #gather user input for menu option select
        user_input = input('What would you like to do? ')

        if user_input not in ['1', '2', '3', '4', '5', '6']:
            print('Unrecognized menu selection!')
            print()
            continue

        #implement Pakudex class methods on new_paku instance to handle other options
        #option 6 prints exit message and breaks loop

        if user_input == '1':
            
            list = new_paku.get_species_array()
            if list == None:
                print('No Pakuri in Pakudex yet!\n')
            else:
                counter = 1
                print('Pakuri In Pakudex:')
                for names in list:
                    print(f'{counter}. {names}')
                    counter += 1
                print()

        elif user_input == '2':
            species = input('Enter the name of the species to display: ')
            stats = new_paku.get_stats(species)
            if stats == None:
                print('Error: No such Pakuri!\n')
            else:
                    print(f'\nSpecies: {species}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}\n')

        elif user_input == '3':
            if new_paku.size >= new_paku.capacity:
                print('Error: Pakudex is full!\n')
            else:
                species = input('Enter the name of the species to add: ')
                add_success = new_paku.add_pakuri(species)
                if add_success == True:
                    print(f'Pakuri species {species} successfully added!\n')
                else:
                    print('Error: Pakudex already contains this species!\n')


        elif user_input == '4':
            evolve = input('Enter the name of the species to evolve: ')
            evolve_success = new_paku.evolve_species(evolve)
            if evolve_success == True:
                print(f'{evolve} has evolved!\n')
            else:
                print('Error: No such Pakuri!\n')

        elif user_input == '5':
            new_paku.sort_pakuri()
            print('Pakuri have been sorted!\n')

        else:
            #Exit message
            print('Thanks for using Pakudex! Bye!')
            break


        



        