def count_characters(file_path):
    char_frequency = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                for char in line.strip():
                    if char.isalpha():
                        char_lower = char.lower()
                        char_frequency[char_lower] = char_frequency.get(char_lower, 0) + 1

        return char_frequency
    except FileNotFoundError:
        print("找不到指定的檔案！")
        return None

def main():
    file_path = input("請輸入檔案路徑：")
    char_frequency = count_characters(file_path)

    if char_frequency:
        print("每一個英文字出現次數：")
        for char, frequency in char_frequency.items():
            print("%s: %d" % (char, frequency))

if __name__ == "__main__":
    main()
