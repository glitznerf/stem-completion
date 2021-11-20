from nltk.stem.porter import *
from stemmer import Porter

stemmer = Porter()
nltk_stemmer = PorterStemmer()

words = "He didn t say any more but we ve always been unusually communicative in a reserved way and I understood that he meant a great deal more than that In consequence I m inclined to reserve all judgements a habit that has opened up many curious natures to me and also made me the victim of not a few veteran bores The abnormal mind is quick to detect and attach itself to this quality when it appears in a normal person and so it came about that in college I was unjustly accused of being a politician because I was privy to the secret griefs of wild unknown men Most of the confidences were unsought frequently I have feigned sleep  preoccupation or a hostile levity when I realized by some unmistakable sign that an intimate revelation was quivering on the horizon for the intimate revelations of young men or at least the terms in which they express them are usually plagiaristic and marred by obvious suppressions Reserving judgements is a matter of infinite hope I am still a little afraid of missing something if I forget that as my father snobbishly suggested and I snobbishly repeat a sense of the fundamental decencies is parcelled out unequally at birth".lower().split(" ")

false = 0
for word in words:
    stemmed = stemmer.stem(word)
    true_stem = nltk_stemmer.stem(word)
    if stemmed != true_stem:
        false += 1
        print(f"Word: {word}, generated: {stemmed}, true: {true_stem}!")

print(f"{false} wrong out of {len(words)}")