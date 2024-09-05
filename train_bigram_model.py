import nltk
nltk.download('gutenberg')
import nltk
print(nltk.__version__)


from nltk.corpus import gutenberg
print(gutenberg.fileids()) 


alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")

print(alice[:1000])

words = nltk.word_tokenize(alice)
print(words[:1000])


num_tokens = 26 # size of vacabulary
bigram_counts = [[0 for _ in range(num_tokens)] for _ in range(num_tokens)]
    
print(bigram_counts)

for word in words:
    for char_idx in range(len(word)-1):
        first_char_id = ord(word[char_idx]) -97
        second_char_id = ord(word[char_idx+1]) - 97
        if(
            first_char_id < 0
            or first_char_id > 25
            or second_char_id < 0 
            or second_char_id > 25
        ):
            continue
    bigram_counts[first_char_id][second_char_id] += 1



for row in bigram_counts:
    N = sum(row)
    for idx in range(len(row)):
        row[idx] /= N

sum(bigram_counts)

print(bigram_counts)

# # import matplotlib.pyplot as plt

# # fig = plt.figure(figsize=(8,8), dpi=80)
# # plt.imshow()
