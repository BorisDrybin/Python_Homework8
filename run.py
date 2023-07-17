from user import choose_mode
from fill_dictionary import filling
from search import search_person

def running():
    person, mode = choose_mode()
    if mode == 'запись':
        filling(person)
    else:
        search_person()