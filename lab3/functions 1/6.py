def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    reversed_sentence = " ".join(words)
    return reversed_sentence

input = input("enter sentence: ")
print("reversed sentence:", reverse_sentence(input))