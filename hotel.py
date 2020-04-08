# The goal of the small exercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

#Write functions to:

#- is_vacant(which_hotel, '101')
#- check if a room is occupied
#- check_in('101', guest_dictionary)
#- assign a person to a room
#- check_out('101')
#- returns the person dictionary in that room

#Please look back at any notes or slides for how to perform any of these actions.


guest = {
    'name': ' ',
    'phone_number': ' ',
    
}

hotel = {
    '101': ' ',
    '102': ' ',
    '103': ' ',
    '104': ' ',
    '105': ' ',

}

    
guest['name'] = input('What is your name? ')
guest['phone_number'] = input('What is your phone number? ')

what_room = input('Which room? 101, 102, 103, 104, or 105? ')
hotel[what_room] = guest
for key in hotel.keys():
    print(f'{key}: {hotel[key]}')
print(hotel)

if hotel[key] == ' ':
    print(f'{key} is vacant')
else:
    print(f'{key} is occupied by {hotel[key]["name"]}')

    check_out = input('Are you checking out? Y or N: ')
if check_out == 'Y':
    hotel[guest] = ' '
    print('Thanks! We will see you next time! ')

