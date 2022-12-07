import datetime

def input_note_title():
    note_title = input("Enter Note Title: ")
    return note_title

def input_choose_date(file):
    choose_date = input("Would you like to include the date or time in your note? (Enter: Both, No, Date, Time): ")
    choose_date = choose_date.lower()

    if choose_date not in ("both", "no", "date", "time"):
        print('ERROR: Please input one of the following - Both, No, Date, Time ')
        input_choose_date(file)
    elif choose_date == "both":
        date_time_write(file)
    elif choose_date == "date":
        date_write(file)
    elif choose_date == "time":
        time_write(file)
    elif "No":
        return

def date_time_write(file):
    date = datetime.datetime.now()
    file.write(date.strftime('%A %d %B %Y. %H:%M') + '\n')

def date_write(file):
    date = datetime.datetime.now()
    file.write(date.strftime('%A %d %B %Y') + '\n')

def time_write(file):
    time = datetime.datetime.now()
    file.write(time.strftime('%H:%M' + '\n'))

def note_book_main():
    note_title = input_note_title()
    file = open(f'./notes/{note_title}.txt', 'x')
    input_choose_date(file)
    file.write(note_title + '\n')
    file.write(input("Enter Note: "))
    file.close()
    print(f'Note book successfully saved as {note_title}.txt')

note_book_main()
