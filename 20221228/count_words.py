def get_list_of_text(file: str) -> list:
    with open(file) as f:
        text_list = f.readlines()
        for _ in range(len(text_list)):
            text_list[_] = text_list[_].split(" ")
            text_list[_][-1] = text_list[_][-1].strip()
    return text_list


def count_words(file: str, word: str) -> int:
    cnt = 0
    text_list = get_list_of_text(file)
    for l in text_list:
        for w in l:
            if w == word:
                cnt += 1
    return cnt


def list_all_line_with_word(file: str, word: str) -> list:
    text_list = get_list_of_text(file)
    new_matrix = []
    for l in text_list:
        for w in l:
            if w == word:
                new_matrix.append(l)
                break
    return new_matrix


def count_line_with_words(file: str, word: str) -> int:
    return len(list_all_line_with_word(file, word))


if __name__ == "__main__":
    print("Enter file name")
    file = str(input())
    print("word you are looking for")
    word = str(input())
    print(get_list_of_text(file))
    print(count_words(file, word))
    print(list_all_line_with_word(file, word))
    print(count_line_with_words(file, word))
