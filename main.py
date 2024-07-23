def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"--- Begin report of {book} ---")
        print(f"{len(words)} words found in the document")
        characs = charac_times(file_contents)
        characs = dict(sorted(characs.items(), key=lambda item: -item[1]))
        for charac in characs :
            if charac.isalpha():
                print(f"The {charac} character was found {characs[charac]} times")
        print(f"--- End report ---")

def charac_times(string):
    characs = {}
    for charac in string:
        charac = charac.lower()
        if (charac in characs):
            characs[charac] += 1
        else:
            characs[charac] = 1
    return characs

def sort_on(dict):
    return dict["num"]

main()