# Create a url shorter with python
import random
import data_management


def shortener(link):
    random_number = random.randint(1000, 9999)
    data_management.import_to_jsonFile(link, random_number)


def search(shortenerLink):
    pass


# run
request = raw_input("Please enter your request (Insert or Search) :").lower()
if request == 'insert':
    url_for_shortener = raw_input("Please enter url for shortener: ")
    shortener(url_for_shortener)
    print("Your url has been shortened successfully!")
elif request == 'search':
    url_for_search = raw_input("Please enter url shortener for search: ")
else:
    print("Invalid input, please enter 'insert' or 'search' only.")
