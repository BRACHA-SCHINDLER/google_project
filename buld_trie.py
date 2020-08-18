from os import listdir
from json_func import write_to_json


def create_db():
    return dict()


def normal_form(s):
    return ' '.join(((s.replace("\n", "")).replace(",", "")).split())


def insert_prefix(trie, sentence, start, i):
    for letter in sentence[start:]:
        if letter not in trie.keys():
            trie[letter] = dict()
            trie[letter]["end"] = list()
        if i not in trie[letter]["end"]:
            trie[letter]["end"].append(i)
        trie = trie[letter]


def insert_sofix(data, trie, sentence, i):
    for j in range(len(sentence)):
        insert_prefix(trie, sentence, j, i)


def insert_to_trie(data, trie, sentence, i):
    #insert_prefix(trie,sentence, 0, i)
    insert_sofix(data, trie, sentence, i)
    trie["end"] = sentence


def auto_complete_data(completed_sentence, source_text):
    auto = {
        "completed_sentence": completed_sentence,
        "source_text": source_text,
        "score": 0,
        "offset": -1
    }
    return auto


def init_tree(trie, data):
    print("preparing your sources, please wait...")
    for f in listdir('technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/c-api')[:1]:
        path = f"technology_texts/python-3.8.4-docs-text/python-3.8.4-docs-text/c-api/{f}"
        my_file = open(path, "r", encoding="utf8")
        index = 1
        for line, sentence in enumerate(my_file):
            if sentence != " ":
                data[index] = auto_complete_data(sentence, f"{path}/{line}")
                insert_to_trie(data, trie, normal_form(sentence), index)
                index += 1
    write_to_json("trie.json", trie)
    write_to_json("data.json", data)