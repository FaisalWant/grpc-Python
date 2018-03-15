#! /usr/bin/python
import addressbook_pb2
import sys

# This function fills in a Person message
def ListPeople(address_book):
  for person in address_book.people:
     print ("PersonID:", person.id)
     print("Name", person.name)
     if person.HasField('email'):
        print("E-mail address", person.email)

     for phone_number in person.phones:
        if phone_number.type== addressbook_pb2.Person.MOBILE:
	   print("Mobile Phone")

	elif phone_number.type==addressbook_pb2.Person.HOME:
	   print("HOME PHONE")

	elif phone_number.type==addressbook_pb2.Person.WORK:
	   print("Work Phone")

	print (phone_number.number)


# Main procedure: Reads the entire address book the information inside
if len(sys.argv) !=2:
   print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE", sys.exit(-1)
address_book= addressbook_pb2.AddressBook()



# Read the exixting address book
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()
ListPeople(address_book)
