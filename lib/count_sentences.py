#!/usr/bin/env python3

# class MyString:
#   pass

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The value must be a string")


class MyString:
    # ... (constructor)

    def is_sentence(self):
        return self.value.endswith(".")

class MyString:
    # ... (constructor)
    
    def is_question(self):
        return self.value.endswith("?")


class MyString:
    # ... (constructor)

    def is_exclamation(self):
        return self.value.endswith("!")

class MyString:
    # ... (constructor)

    def count_sentences(self):
        sentences = self.value.split(".")  # Split sentences by period
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty sentences
        return len(sentences)
