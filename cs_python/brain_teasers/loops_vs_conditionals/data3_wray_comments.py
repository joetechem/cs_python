# Pre-req's : loops, conditionals, functions, lists, tuples, and dictionaries
#
# Python 2.7
#
# Objectives: Advanced dictionaries, dictionaries as list indices
# Foundational Objectives: Databases
#

# Remember in the previous lessons, we defined a contact record using the following tuple

contact = ('first_name','last_name','mobile_phone','home_phone','zip_code')

FIRST_NAME = 0 # First name is in the first position of the tuple.
LAST_NAME = 1 # Last name i sin the second position of the tuple...
MOBILE_PHONE = 2
HOME_PHONE = 3
ZIP_CODE = 4

# We built a simple function to help us create contact tuples

def create_contact(first_name,last_name,mobile_phone,home_phone=None,zip_code=None):
    return (first_name,last_name,mobile_phone,home_phone,zip_code)


# Let's create a list for the contacts
contacts = []

# We know we want to create separate dictionaries to help us find by first name or last name.
# But, what if we want to find by phone or zip? Well, let's create more dictionaries.
# And this time, instead of having each dictionary maintain a full contact, our new
# trick will be to simply store the list index in the other dictionaries. Technically, in Python
# this is not all that different from our previous solution (within the program, the variable contact
# references the same tuple for all dictionaries). However, suppose our list of contacts is so large
# that we have to store them in a separate file (like in a real database), we need a solution like below
# in order to maintain an index or id that may reference a record on disk (or on some other system).
# Thus, we will create an 'index' dictionary for each search criterion:

contacts_by_first_name = {}
contacts_by_last_name = {}
contacts_by_phone = {}
contacts_by_zip = {}

# And we can now create a function that populates the list (table) and dictionaries (indexes).
# The 'trick' here is that we simply put the list indexes as the value in the dictionaries

def add_contact(contact):
    
    # We get the index (ID) of the item we are adding to the list (table).
    index = len(contacts)
    # Add it to the list (table).
    contacts.append(contact)

    # First Name - The key is the search term, first_name, and the value is the list indexes
    # get the first_name from the record being added
    first_name = contact[FIRST_NAME]
    # Check if it exists in this dictionary already
    if first_name in contacts_by_first_name.keys():
        # if it already exists, we add it to the list of record indexes that have this first_name
        contacts_by_first_name[first_name].append(index)
    else:
        # if this is the first record with this first_name, we create a list with the one index
        contacts_by_first_name[first_name] = [index]

    # Last Name - Same logic, but with last_name as the key to the list indexes
    last_name = contact[LAST_NAME]
    if last_name in contacts_by_last_name.keys():
        contacts_by_last_name[last_name].append(index)
    else:
        contacts_by_last_name[last_name] = [index]

    # Phone - Ditto, except we are putting both mobile and home phone numbers together.
    mobile = contact[MOBILE_PHONE]
    if mobile in contacts_by_phone.keys():
        contacts_by_phone[mobile].append(index)
    else:
        contacts_by_phone[mobile] = [index]

    home = contact[HOME_PHONE]
    if home in contacts_by_phone.keys():
        contacts_by_phone[home].append(index)
    else:
        contacts_by_phone[home] = [index]

    # Zip - Ditto
    zip = contact[ZIP_CODE]
    if zip in contacts_by_zip.keys():
        contacts_by_zip[zip].append(index)
    else:
        contacts_by_zip[zip] = [index]


# Let's populate our table and indexes with some data      
add_contact(create_contact("Sue","Simmons","804-555-1234"))
add_contact(create_contact("John","Doe","804-555-1235","804-555-1236"))
add_contact(create_contact("Pat","Petri","804-555-1237","804-555-1238","23117"))
add_contact(create_contact("John","Smith","804-555-4321","804-555-4322"))
add_contact(create_contact("Steve","Simmons","804-555-4323","804-555-4323","23117"))

# So, what do these dictionaries look like?

print
print "A dictionary of indexes that stores the list location of the records with the given key."
print "By First Name:"
print contacts_by_first_name
print "By Last Name:"
print contacts_by_last_name
print "By Phone Number:"
print contacts_by_phone
print "By Zip Code:"
print contacts_by_zip
print

print "And the list we are indexing:"
print contacts
print

# So, now, the find by first_name will return a list of indexes, which is exactly what one would expect!

indexes = contacts_by_first_name["Sue"]
contact = contacts[indexes[0]]
print "Contact with first name Sue:"
print contact
print

# A better way to use these dictionaries

print "Results for search by last name Simmons;"
for index in contacts_by_last_name["Simmons"]:
    print contacts[index]

# So, how would you find contacts by phone number?
# By zip?
# Why does the lookup by phone for 804-555-4323 yield two results with the same index?
