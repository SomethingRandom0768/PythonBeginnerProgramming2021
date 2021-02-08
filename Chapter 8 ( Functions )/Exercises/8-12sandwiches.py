

def sandwich_items(*items):
    print("The sandwich ordered has:")
    for sandwich_item in items:
        print(f"- {sandwich_item}")


sandwich_items('bread', 'pork', 'lettuce', 'fish')
