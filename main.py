def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictChars = lowerandcount(text)
    sorted = converAndSort(dictChars)
    print(f"{sorted} words found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def lowerandcount(text):   
    res = {}
    for val in text :
        if val.isalpha() : 
            lower = val.lower()
            if lower in res :
                res[lower] +=1
            else :
                res[lower] = 1
    return res

def converAndSort(dictio) :
    sorted_list = []
    for ch in dictio:
        sorted_list.append({"char": ch, "num": dictio[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()
