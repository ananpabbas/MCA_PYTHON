class Utility:
    def occurrence(self, sentence):
        words = sentence.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count

    def frequency(self, word):
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    def factors(self, num):
        factors_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors_list.append(i)
        return factors_list

def main():
    utility = Utility()

    while True:
        print("\n1. Occurrence of word")
        print("2. Character frequency")
        print("3. Factors")
        print("4. Exit")

        choice = int(input("Please Enter a choice from the menu: "))

        if choice == 1:
            sentence = input("Enter a sentence: ")
            result = utility.occurrence(sentence)
            print("\nWord Occurrences:")
            for word, count in result.items():
                print(f"{word}: {count}")
        
        elif choice == 2:
            word = input("Enter a word: ")
            result = utility.frequency(word)
            print("\nCharacter Frequency:")
            for char, count in result.items():
                print(f"{char}: {count}")
        
        elif choice == 3:
            num = int(input("Enter a number: "))
            result = utility.factors(num)
            print("\nFactors of", num, "are:")
            print(result)
        
        elif choice == 4:
        
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
