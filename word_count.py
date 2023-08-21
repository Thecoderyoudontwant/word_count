def main():
    text = input("Enter a sentence or paragraph: ")
    words = text.split()
    word_count = len(words)
    print("Word count:", word_count)

if __name__ == "__main__":
    main()
