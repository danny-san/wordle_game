def sort_words(file_to_read, file_to_write):
    with open(file_to_read, 'r', encoding="utf-8") as f:
        words = f.readlines()
        words.sort()

    with open(file_to_write, 'w', encoding="utf-8") as new:
        new.writelines(words)


if __name__ == "__main__":
    sort_words('words_5.txt', 'words_5_sort.txt')
