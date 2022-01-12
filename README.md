# Wordle Starting Word Analysis
A very quick pass at trying to find the best starting words for wordle. `best_starting_words.py` scans through a list
of words and iterates through all five letter words in the list without any duplicate letters, recording the frequency
of each letter at each index across the dataset. It also more heavily weights letter frequncy if the word the letter
is coming from is in the set of the most common words in the english language. Once the frequencies are established,
iterates through the word list again. Each word is scored by summing the scores of the letters included in the word.
Each letter is scored by a weighted sum of \[frequency of occurence of that letter in its particular index across
all words\] + \[frequency of occurence of that letter in any index across all words\]. With current feature set and
weightings, the highest scoring words are as follows:


```
tares: 28446
lares: 28134
aries: 28026
nares: 27917
cares: 27733
rales: 27588
rates: 27586
dares: 27370
aotes: 27222
saner: 27202
saite: 27080
aures: 27077
teras: 27060
mares: 27059
pares: 27054
tales: 27021
hares: 26987
earns: 26962
lanes: 26942
bares: 26898
```

Run the analysis with `python best_starting_words.py` from the base directory.