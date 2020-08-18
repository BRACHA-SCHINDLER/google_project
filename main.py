from auto_complete import auto_complete
from buld_trie import create_db, init_tree
from json_func import read_from_json


def get_input_and_search(data, trie):
    while 1:
        sentence_for_search = ""
        while 1:
            sentence_for_search += input(f"enter your search term . # for new search. * for exit: {sentence_for_search}")
            if sentence_for_search:
                if sentence_for_search[-1] == "#":
                    print("---------type a new search---------")
                    break
                if sentence_for_search[-1] == "*":
                    break
            if auto_complete(trie, data, sentence_for_search) == 0:
                print("---------not found :( type a new search---------")
                break
        if sentence_for_search[-1] == "*":
            break


if __name__ == '__main__':
    """offline:
    data = dict()
    trie = create_db()
    init_tree(trie, data)"""

    trie = read_from_json("trie.json")
    data = read_from_json("data.json")
    get_input_and_search(data, trie)




