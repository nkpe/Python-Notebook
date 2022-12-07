import datetime

def input_note_title():
    note_title = input("Enter Note Title: ")
    return note_title

def date_input():
    date = datetime.datetime.now()
    return date.strftime('%A %d %B %Y. %H:%M')

def note_book_functionality():
    note_title = input_note_title()
    file = open(f'./notes/{note_title}.txt', 'x')
    file.write(date_input() + '\n')
    file.write(note_title + '\n')
    file.write(input("Enter Note: "))
    file.close()
    print(f'Note book successfully saved as {note_title}.txt')

note_book_functionality()
