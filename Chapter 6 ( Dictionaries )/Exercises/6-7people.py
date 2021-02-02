first_person = {'First Name': 'monkey',
          'Last Name' : 'bannan',
          'Age'       :  300,            # He is a wise old monkey
          'City'      : 'monkeyland'
          }

second_person = {'First Name': 'Janice', # I have no clue if this is an actual person, I just made up this name.
                 'Last Name' : 'Walters',
                 'Age'       :  51514,
                 'City'      : 'PHDLand'
                 } # Okay nvm, I looked her up and apparently she's a really disliked PHD

third_person = {'First Name'   : 'chicken', # A good friend of monkey bannan
                'Last Name'    : 'man',
                'Age'          : 250,
                'City'         : 'barnland'
                }

list_of_people = [ first_person, second_person, third_person ]

for person in list_of_people:
   for type, info in person.items():
       print(f"{type.title()} : {info}")
