def read():
    file = open("equipment.txt", "r")
    lines = file.read().splitlines()

    dictionary = {}

    for x in range(len(lines)):
        word = lines[x].split(",")
        name = word[0]
        brand = word[1]
        price = float(word[2].replace('$', ''))
        quantity = int(word[3])
        dictionary[x + 1] = {
            'Name': name,
            'Brand': brand,
            'Price': price,
            'Quantity': quantity
        }

    header_row = "|{:<4} |{:<40} |{:<30} |{:<10} | {:<5}".format("ID", "Name", "Brand", "Price", "Quantity")
    formatted_rows = []

    for item_id, item_data in dictionary.items():
        formatted_row = "|{:<4} | {:<40} |{:<30} |${:<20.3f} |{:<9}|".format(
            item_id, item_data['Name'], item_data['Brand'], item_data['Price'], item_data['Quantity'])
        formatted_rows.append(formatted_row)

    print(header_row)
    print('-' * len(header_row))
    print('\n'.join(formatted_rows))
    print('-' * len(header_row))

    file.close()
    return dictionary




