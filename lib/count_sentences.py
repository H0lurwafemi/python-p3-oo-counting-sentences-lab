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
    def is_sentence(self):
        return self.value.endswith(".")

class MyString:
    
    def is_question(self):
        return self.value.endswith("?")


class MyString:
  
    def is_exclamation(self):
        return self.value.endswith("!")

class MyString:

    def count_sentences(self):
        sentences = self.value.split(".")  
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  
        return len(sentences)
