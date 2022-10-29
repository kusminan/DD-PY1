
def get_count_char(str_):
    str_ = str_.lower()
    str_ = " ".join(str_.split())
    char_dic = {}
    for char in str_:
        if char.isalpha():
            if char in char_dic:
                char_dic[char] +=1
            else:
                char_dic[char] = 1
    return char_dic




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
