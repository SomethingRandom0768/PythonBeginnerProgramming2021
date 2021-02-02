
rivers = {'nile': 'egypt',
          'amazon': 'colombia',
          'yangtze': 'china'
          }

for k, v in rivers.items():
    print(f"The { k.title() } goes through { v.title() }")