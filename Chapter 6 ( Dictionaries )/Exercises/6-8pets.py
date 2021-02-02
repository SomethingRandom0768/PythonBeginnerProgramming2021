first_pet = {'Mabel' :
                 {'Type': 'Dog',
                "Owner's Name" : 'Monkey'}
             }
second_pet = {'Flopsie':
                  {'Type' : 'Goat Gorilla',
                   "Owner's Name" : 'King Bumi'
                   }
              }

pets = [first_pet, second_pet]

for pet in pets:
    for name, info in pet.items():
        print(f"\nPet's Name : { name.title() } " ) # This is a messed up format but psh, it does something.
        for info_label, information in info.items():
            print(f"{info_label} : {information}")