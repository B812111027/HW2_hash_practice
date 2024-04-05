def count_words(file_path):
    word_frequency = {}


    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = ''.join(filter(str.isalpha, word)).lower()
                    if word:
                        word_frequency[word] = word_frequency.get(word, 0) + 1


        return word_frequency
    except FileNotFoundError:
        print("找不到指定的檔案！")
        return None


def main():
    file_path = input("請輸入檔案路徑：")
    word_freque ncy = count_words(file_path)


    if word_frequency:
        print("每一個英文單字出現次數：")
        for word, frequency in word_frequency.items():
            print("%s: %d" % (word, frequency))


if _ _name_ _ == "_ _main_ _":
    main()
