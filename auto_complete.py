from Auto_complet_data import AutoCompleteData
from buld_trie import normal_form
from search import search_in_tree

def print_auto_complete_data(auto):
    print("sentence: ", auto["completed_sentence"],"path: ", auto["source_text"], "| score:", auto["score"], "| offset: ",auto["offset"])
    print()


def print_auto_complete(res):
    for item in res:
        print_auto_complete_data(item)


def sort_by_score(res):
    res.sort(key=lambda x: x["completed_sentence"])
    res.sort(key=lambda x: x["score"], reverse=True)
    return res


def get_object_by_id(data,res):
    return [data[f"{i}"] for i in res]


def restart_score_offset(res):
    for item in res:
        item["score"] = 0
        item["offset"] = -1


def auto_complete(trie, data, sentence_for_search):

    res = search_in_tree(trie, normal_form(sentence_for_search), data)
    if res == set():
        return 0
    res = sort_by_score(get_object_by_id(data, res))
    print_auto_complete(res[:5])
    restart_score_offset(res)



