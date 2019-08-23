'''
TODO:
    - 
'''

import csv
import os

filename = '2019-08-22_Report.csv'

fields = []
rows = []
stores = ['Coolstuff', 'Troll and Toad', 'TCG', 'Barter', 'Not included']
largest_num_spaces = 0

def import_csv():
    os.chdir('data/')

    with open (filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for field in csv_reader.next():
            fields.append(field)

        for row in csv_reader:
            rows.append(row)


def export_by_store():
    grand_total = 0

    with open (filename.split('.')[0] + '.txt', 'w') as text_file:
        for i in range(0, len(stores)):
            text_file.write((chr(ord('a') + i)) + ') ' + stores[i] + '\n')
            grand_total = grand_total + populate_listing(text_file, stores[i], None)
            text_file.write('\n')
        text_file.write('Grand Total: $' + str(grand_total))


def export_by_deck():
    # Populate Deck List
    decks = get_list_by('Deck')

    for deck in decks:
        grand_total = 0
        with open (filename.split('_')[0] + '_' + deck + '.txt', 'w') as text_file:
            for i in range(0, len(stores)):
                text_file.write((chr(ord('a') + i)) + ') ' + stores[i] + '\n')
                grand_total = grand_total + populate_listing(text_file, stores[i], deck)
                text_file.write('\n')
            text_file.write('Grand Total: $' + str(grand_total))


def populate_listing(text_file, store, deck):
    subtotal = 0

    for row in rows:
        if (row[fields.index('Store')] == store and (deck == None or row[fields.index('Deck')] == deck)):
            # Count, Card Name
            temp = row[fields.index('Count')] + ' ' + row[fields.index('Card Name')]
            # Card Pack
            temp = temp + ' (' + row[fields.index('Card Pack')] + ')'
            # Make spacing even so prices line up
            num_spaces_required = largest_num_spaces - len(temp)
            temp = temp + (num_spaces_required * ' ')
            # Price
            subtotal = subtotal + float(row[fields.index('Price')].replace('$', ''))
            temp = temp + ('$0.' + row[fields.index('Price')].split('.')[1]
                if len(row[fields.index('Price')].split('.')[0]) == 1 else row[fields.index('Price')]) + '\n'
            text_file.write(temp)

    text_file.write('Subtotal: $' + str(subtotal) + '\n')
    return subtotal


def get_list_by(attribute):
    attribute_list = set()

    for row in rows:
        attribute_list.add(row[fields.index(attribute)])
    attribute_list = list(attribute_list)
    attribute_list.sort()

    return attribute_list


def main():
    import_csv()

    # Create output directory
    if not os.path.exists('../out'):
        os.mkdir('../out')
    os.chdir('../out')

    # Set largest number of spaces
    global largest_num_spaces
    for row in rows:
        temp = len(row[fields.index('Card Name')]) + len(row[fields.index('Card Pack')])
        largest_num_spaces = max(largest_num_spaces, temp)
    # Account for parenthesis, spaces, and the count attribute
    largest_num_spaces = largest_num_spaces + 7
    # Make largest num spaces a multiple of 4 (rounding up)
    largest_num_spaces = largest_num_spaces - (largest_num_spaces % 4) + 4

    export_by_store()
    export_by_deck()


if(__name__ == '__main__'):
    main()