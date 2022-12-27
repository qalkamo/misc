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


if __name__ == "__main__":
    print(get_list_of_text("test.txt"))
    print(count_words("test.txt", "stop"))
    print(list_all_line_with_word("test.txt", "stop"))
