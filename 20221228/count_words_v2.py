import datetime
import os
from typing import List, Union


def get_nowtime() -> str:
    now_time = str(datetime.datetime.now()).split(".")[0]
    now_time = now_time.replace(" ", "_")
    now_time = now_time.replace(":", "_")
    return now_time


def text_all_line_with_word(
    input_file: str,
    output_file,
    word_list: Union[str, List[str]],
    start_line,
    end_line,
) -> List[int]:
    if isinstance(word_list, str):
        word_list = [word_list]
    now_time = get_nowtime()
    os.mkdir(now_time)
    cnt_list = [0] * len(word_list)
    for i, word in enumerate(word_list):
        with open(input_file) as f:
            text_list = f.readlines()
            for _ in range(len(text_list)):
                text_list_line = text_list[_].split(" ")
                text_list_line[-1] = text_list_line[-1].strip()
                if word in text_list_line:
                    cnt_list[i] += 1
                    file_name, extension = output_file.split(".")
                    with open(f"{now_time}/{file_name}_{word}.{extension}", "a") as of:
                        of.writelines(f"{text_list_line}\n")
    return cnt_list


if __name__ == "__main__":
    print("input file name:")
    input_file = str(input())
    print("output file name:")
    output_file = str(input())
    print("list of words you are looking for:")
    word_list = list(map(str, input().split()))
    print(text_all_line_with_word(input_file, output_file, word_list))
