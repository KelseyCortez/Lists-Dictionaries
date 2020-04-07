
# Please use one dictionary to hold this information
# - Make sure you can 
#     - put someone in an unoccpied room
#     - make a room available by setting the occupant name to ''
#     - check if a room number is valid
#     - check if a room is occupied or not

# - The hotel has 5 rooms
# - The names of the rooms are 101, 102, 103, 104, 105
# - Store the occupant name for each of the rooms
#     - or an empty string if unoccpied

# hotel = {
#         'room_name' : [101, 102, 103, 104, 105],
#         'occupant_name': ['Betty', '', '', 'Ray', 'Steve'],
#         'is_vacant': []

#      }
betty = {
    'name': 'Betty',
    'phone_number': 4568752345,
    'is_prepaid?': True
}
steve = {
    'name': 'Steve',
    'phone_number': 4568752345,
    'is_prepaid?': False
}
carl= {
    'name': 'Carl',
    'phone_number': 4568752345,
    'is_prepaid?': True
}

alice = {
    'name': 'Alice',
    'phone_number': 4568752345,
    'is_prepaid?': False
}
hotel = {
    '101': ' ',
    '102': ' ',
    '103': ' ',
    '104': ' ',
    '105': ' '

}
# }
# guest_info[''] = ''
# keys = [hotel]

#guest is checking in
hotel['101'] = betty
hotel['102'] = steve
hotel['103'] = alice
hotel['104'] = carl
hotel['105'] = ''

for k in hotel.keys():
    print(f'{k}: {hotel[k]}')
print(hotel)

if hotel[k] == '':
    print(f'{k} is vacant')
else:
    print(f'{k} is occupied by {hotel[k]["name"]}')

#for any one room, you should store:
# occupant name
# phone number
# has prepaid

# hotel['occupant_name'] = 'Alice'




