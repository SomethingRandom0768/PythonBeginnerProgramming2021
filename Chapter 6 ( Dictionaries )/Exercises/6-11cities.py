cities = {'Gaborone' : {
                        'Country' : 'Botswana',
                        'Population' : "208,411",
                        'Fact' : "Home to the world's largest concentration of African elephants",
                        },

          'Vilnius' :  {
                        'Country' : 'Lithuania',
                        'Population' : "540,000",
                        'Fact' : "8% of all white storks in the world breed here ",
                        },

          'Caracas' : {
                        'Country' : 'Venezuela',
                        'Population' : "2,946,000",
                        'Fact' : "Home to one of the largest financial districts in South America",
                        }
        }

for name, info_group in cities.items():
    print(f"\nThe city's name is {name} and has the following information:")
    for label, info in info_group.items():
        print(f"{label} : {info}")