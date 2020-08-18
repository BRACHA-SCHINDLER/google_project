class AutoCompleteData:
    def __init__(self,completed_sentence,source_text):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = -1
        self.score = 0

    def print(self):
        print("sentence: ", self.completed_sentence,"path: ", self.source_text, "| score:", self.score, "| offset: ", self.offset)
        print()

"""
def make_auto_complete_data(completed_sentence,source_text):
    auto = {
        "completed_sentence" : completed_sentence,
        "source_text" : source_text,
        "score" : 0
        "offset": -1
    }"""




