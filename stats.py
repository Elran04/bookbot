def get_num_words(book_text):
        words = book_text.split()
        num_words = len(words)
        return num_words

def get_char_count(book_text):
        char_count = {}
        lowercase_text = book_text.lower()
        
        for char in lowercase_text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        return char_count

def sort_on(dict_item):
        return dict_item["num"]

def chars_dict_to_sorted_list(chars_dict):
        sorted_list = []
        for char in chars_dict:
            if char.isalpha():
                sorted_list.append({"char": char, "num": chars_dict[char]})
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list

def sort_dictionary(unsorted_dict):
        sorted_keys = sorted(unsorted_dict.keys())
        sorted_dict = {}
        
        for key in sorted_keys:
            sorted_dict[key] = unsorted_dict[key]
        
        return sorted_dict