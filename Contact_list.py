#A sample contact list using python with fun features
import sqlite3
conn = sqlite3.connect('Python_final_assignment.db')
my_cursor = conn.cursor()

#1. Query for Creating a new contact list
query_new_list = 'create table {}(first_name text, last_name text, phone_number int, address text,\
secondary_number int,email text)'
#2. Query for removing an existing contact list
query_del_list = 'drop table {}'
#3. Query for Adding a new contact to a contact list
query_new_con = "insert into {} (first_name, last_name, phone_number, address, secondary_number, email)\
 values ('{}', '{}', {}, '{}', {}, '{}')"
#4. Query for deleting an existing contact
query_del_con = "delete from {} where first_name = '{}' and last_name = '{}'"

if input('Do you want to create a new contact list? (Y/N)\n') == 'Y':
    table_name = input('Choose a name for your contact list:\n')
    my_cursor.execute(query_new_list.format(table_name))
elif input('Do you want to remove an existing contact list? (Y/N)\n') == 'Y':
    table_name = input('Which contact list:\n')
    my_cursor.execute(query_del_list.format(table_name))
else:
    #here you can do some changes or search some data from your chosen list
    table_name = input('Which contact list you want to EDIT?\n')
    my_cursor.execute('select * from {}'.format(table_name))
    print('below are the contacts in {}:'.format(table_name))
    contact_list = my_cursor.fetchall()
    for cons in contact_list:
        print(cons)
    print("\nBelow actions are supported for editing your chosen contact lists\n",
    '1.Add new contact (enter: contact_new)\n',
    '2.delete new contact (enter: contact_del)\n',
    '3.Show specific number (enter: contact_num)\n',
    '4.Details of a nymber (enter: contact_det)\n')
    Action = input('choose an action from list above:\n')

    if Action == 'contact_new':
        print('Please enter below information:\n')
        first_name = input("What is your contact's First name?\n")
        last_name = input("What is your contact's Last name?\n")
        phone_number = input("What is your contact's Phone number?\n")
        address = input("What is your contact's address? (less than 20 charactors)\n")
        secondary_number = input("What is your contact's Secondary number? (inter 0 if no secondary number)\n")
        email = input("What is your contact's Email?\n")
        my_cursor.execute(query_new_con.format(table_name, first_name, last_name, phone_number, address, secondary_number, email))
        print(my_cursor.fetchone())
    elif Action == 'contact_del':
        first_name = input("Please enter contact's first name which you want to delete:\n")
        last_name = input("Please enter contact's last name which you want to delete:\n")
        my_cursor.execute(query_del_con.format(table_name, first_name, last_name))
        print(my_cursor.fetchone())
    elif Action == 'contact_num':
        first_name = input('Please enter contact\'s first name which you want to see its number:\n')
        my_cursor.execute("select phone_number from {} where first_name = '{}'".format(table_name, first_name))
        print(my_cursor.fetchone())
    elif Action == 'contact_det':
        phone_number = input("Please enter the phone number which you want to see its detail:\n")
        my_cursor.execute("select * from {} where Phone_number = {}".format(table_name, phone_number))
        print(my_cursor.fetchone())

conn.commit()
