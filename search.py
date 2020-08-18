def is_sub_without_mistake(trie, sentence):
    for letter in sentence:
        if letter == " ":
            place_in_word = 0
        if letter in trie.keys():
            trie = trie[letter]
        else:
            return []
    if "end" in trie:
        return trie["end"]


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def get_sentence_by_id(id, data):
    return data[f"{id}"]["completed_sentence"]


def swap_minus_score(letter):
    minus = [5, 4, 3, 2]
    return minus[letter] if letter <= 3 else 1


def is_sub(res, sentence):
    mistake = 0
    if len(sentence) > len(res):
        return 0
    for letter in range(len(sentence)):
        if res[letter] != sentence[letter]:
            mistake += 1
    return mistake == 1


def is_sub_with_one_swap(sentence, intersect, data):
    correct = []
    for id in intersect:
        res = get_sentence_by_id(id, data)
        iter = 0
        for letter in range(len(res)):
            while res[iter] != sentence[0]:
                iter += 1
            if is_sub(res[iter+letter:], sentence):
                correct.append(id)
                break
    return correct


def update_swap_score(trie, sentence,data, tmp, letter):
    for item in tmp:
        if data[f"{item}"]["score"] == 0:
            data[f"{item}"]["score"] = -swap_minus_score(letter) + len(sentence)*2
            if data[f"{item}"]["offset"] == -1:
                data[f"{item}"]["offset"] = get_offset(trie, sentence[:letter], data[f"{item}"]["completed_sentence"])


def sub_with_swap(trie, sentence, data):
    res = []
    for letter in range( len(sentence) - 1):
        prefix = is_sub_without_mistake(trie, sentence[:letter])
        suffix = is_sub_without_mistake(trie, sentence[letter + 1:])
        intersect = intersection(prefix, suffix)
        if intersect != []:
            tmp = is_sub_with_one_swap(sentence, intersect, data)
            if tmp != []:
                update_swap_score(trie, sentence, data, tmp, letter)
                res += tmp
    if len(sentence) > 1:
        tmp = is_sub_without_mistake(trie, sentence[:len(sentence) - 1])
        update_swap_score(trie, sentence, data, tmp, len(sentence) -1)
        res += tmp

        tmp = is_sub_without_mistake(trie, sentence[1:])
        update_swap_score(trie, sentence, data, tmp, 0)
        res += tmp
    return res


def delete_insert_minus_score(char):
    minus = [10, 8, 6, 4]
    if char <= 3:
        return minus[char]
    else:
        return 2


def update_delete_insert_score_(trie, data, sentence, arr, char):
    for item in arr:
        if data[item]["score"] == 0:
            data[item]["score"] = -delete_insert_minus_score(char) + len(sentence) * 2
            if data[item]["offset"] == -1:
                data[item]["offset"] = get_offset(trie, sentence[:char], data[item]["completed_sentence"])


def do_update_delete_insert_score_(trie,data, sentence, arr, letter):
    update_delete_insert_score_(trie, data, sentence, arr, letter)
    return arr


def sub_with_delete(trie, sentence,data):
    res = []
    for letter in range(1, len(sentence) - 1):
        prefix = is_sub_without_mistake(trie, sentence[:letter])
        suffix = is_sub_without_mistake(trie, sentence[letter:])
        intersect = intersection(prefix, suffix)
        if intersect:
            arr = is_sub_with_one_swap(sentence[:letter] + ' ' + sentence[letter:], intersect, data)
            res += do_update_delete_insert_score_(trie,data, sentence, arr, letter)
    arr = is_sub_without_mistake(trie, sentence[:len(sentence) - 1])
    res += do_update_delete_insert_score_(trie, data, sentence, arr, len(sentence) - 1)
    arr = is_sub_without_mistake(trie, sentence[1:])
    res += do_update_delete_insert_score_(trie, data, sentence, arr, 0)
    return res


def sub_with_insert(data,trie, sentence):
    res = []
    for char in range(len(sentence)):
        arr = is_sub_without_mistake(trie, sentence[:char] + sentence[char + 1:])
        res += do_update_delete_insert_score_(trie, data, sentence, arr, char)
    return res


def get_offset(trie, word, sentence):
    return sentence.find(word)


def update_high_score(trie, founded, data, sentence):
    for found in founded:
        data[f"{found}"]["score"] += len(sentence)*2
        if data[f"{found}"]["offset"] == -1:
            data[f"{found}"]["offset"] = get_offset(trie, sentence, data[f"{found}"]["completed_sentence"])


def search_in_tree(trie, sentence, data):
    founded = []
    if len(sentence) > 0:
        founded += is_sub_without_mistake(trie, sentence)
        update_high_score(trie, founded, data, sentence)
    if len(sentence) > 1:
        if len(founded) < 5:
            founded += sub_with_swap(trie, sentence, data)
            if len(founded) < 5:
                founded += sub_with_delete(trie, sentence, data)
                if len(founded) < 5:
                    founded += sub_with_insert(data, trie, sentence)
    return set(founded)







