from collections import defaultdict

COMMON_WORD_WEIGHT = 5
CORRECT_LETTER_INDEX_WEIGHT = 2

words = open("./words_alpha.txt")
word_list = words.readlines()
five_letter_words = filter(lambda word: len(word.strip()) == 5, word_list)
filtered_five_letter_words = filter(lambda word: len(set([char for char in word])) == len([char for char in word]), [word.strip() for word in five_letter_words])

common_words = filter(lambda word: len(word) == 5, [word.strip() for word in open("./common_words.txt").readlines()])
letter_list = [[letter for letter in word] for word in filtered_five_letter_words]
frequency = defaultdict(lambda: defaultdict(lambda: 0))
for word in letter_list:
  letter_score = COMMON_WORD_WEIGHT if "".join(word) in common_words else 1
  for i in range(len(word)):
    frequency[i][word[i]] += letter_score
dict_frequency = dict(frequency)

def sort_dict(d):
  return sorted(d.items(), key=lambda x: x[1], reverse=True)

def score(word):
  score = 0
  for i in range(len(word)):
    letter = word[i]
    score += CORRECT_LETTER_INDEX_WEIGHT * frequency[i][letter]
    for j in range(len(word)):
      if (i != j):
        score += frequency[j][letter]
  return score

scores = {}
for word in filtered_five_letter_words:
  scores[word] = score(word)

sorted_scores = sort_dict(scores)
for i in range(20):
  print sorted_scores[i][0] + ": " + str(sorted_scores[i][1])
