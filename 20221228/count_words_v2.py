import datetime
import os
from typing import List, Union


def get_wordlist(is_newline: bool = False) -> List[str]:
    """
    is_newline == False
        word_list.txt
            "word1 word2 ..."
    is_newline == True
        word_list.txt
            "word1
            word2
            ...
            "
    """
    with open("word_list.txt") as f:
        wordlist = f.readlines()
        if is_newline:
            for i, l in enumerate(wordlist):
                wordlist[i] = wordlist[i].strip()
        else:
            wordlist = wordlist[0].split(" ")
            wordlist[-1] = wordlist[-1].strip()
    return wordlist


def get_nowtime() -> str:
    now_time = str(datetime.datetime.now()).split(".")[0]
    now_time = now_time.replace(" ", "_")
    now_time = now_time.replace(":", "_")
    return now_time


def text_all_line_with_word(
    input_file: str, output_file, word_list: Union[str, List[str]], last_line: int = 5
) -> List[int]:
    if isinstance(word_list, str):
        word_list = [word_list]
    now_time = get_nowtime()
    os.mkdir(now_time)
    cnt_list = [0] * len(word_list)
    output_file_name, extension = output_file.split(".")
    for word_num, word in enumerate(word_list):
        with open(input_file) as f:
            text_list = [line for index, line in enumerate(f) if index <= last_line]
            for line_num in range(len(text_list)):
                text_list_line = text_list[line_num].split(" ")
                text_list_line[-1] = text_list_line[-1].strip()
                columns = []
                for word_col, word_in_line in enumerate(text_list_line):
                    if word_in_line == word:
                        cnt_list[word_num] += 1
                        columns.append(word_col)
                if columns:
                    with open(
                        f"{now_time}/{output_file_name}_{word}.{extension}", "a"
                    ) as of:
                        of.writelines(f"{line_num} {columns} {text_list_line}\n")
    return cnt_list


if __name__ == "__main__":
    print("input file name:")
    input_file = str(input())
    print("output file name:")
    output_file = str(input())
    # print("list of words you are looking for:")
    # word_list = list(map(str, input().split()))
    print(
        text_all_line_with_word(
            input_file, output_file, word_list=get_wordlist(True), last_line=10
        )
    )
    # print(text_all_line_with_word(input_file, output_file, word_list=get_wordlist(False)))
