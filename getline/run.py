def getlines(file):
    with open(file=file) as f:
        line_list = f.readlines()
        data = []
        for line in line_list:
            line = line.split("\t")
            data.append([])
            for word in line:
                # print(word)
                data_word = word.replace('\n', '')
                data[-1].append(data_word)
    return data


if __name__ == "__main__":
    print(getlines("test.txt"))