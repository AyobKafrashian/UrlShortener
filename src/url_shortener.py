# Create a url shorter with python
import random
import data_management
import webbrowser


def shortener(link):
    random_number = random.randint(1000, 9999)
    with open('setting.txt', 'r') as f:
        content = f.read()
        num = random_number
        url = content.format(num)
        data_management.import_to_jsonFile(link, url)

def search(shortenerLink):
    data = data_management.seach_in_jsonFile(shortenerLink)
    if data != None:
        # open link on browser tab
        webbrowser.open_new_tab(data)
    else:
        print("The shortener of this link was not found!")


def started():
    request = raw_input(
        "Please enter your request (Create or Search) :").lower()
    if request == 'create':
        url_for_shortener = raw_input("Please enter url for shortener: ")
        shortener(url_for_shortener)
        print("Your url has been shortened successfully!")
    elif request == 'search':
        url_for_search = raw_input("Please enter url shortener for search: ")
        search(url_for_search)
    else:
        print("Invalid input, please enter 'Create' or 'Search' only.")
        started()


# run
started()
