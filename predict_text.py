import re
import random
import get_data


pride_and_prejudice_text = get_data.get()

sentence_starters = {}
word_followers={}
for sentence in re.split('!|\?|\.', pride_and_prejudice_text):
    a=1
    sentence_list = re.split(' ', sentence.strip())

    while len(sentence_list) > 0 and sentence_list[0] == '':
        del sentence_list[0]
    if len(sentence_list) > 0:
        if sentence_list[0] not in sentence_starters:
            sentence_starters[sentence_list[0]]=1
        else:
            sentence_starters[sentence_list[0]]+=1
    for i in range(0,len(sentence_list)):
        word = sentence_list[i]
        if word not in word_followers:
            word_followers[word] = {}
        if i == len(sentence_list)-1:
            next_word = None
        else:
            next_word = sentence_list[i+1]

        if next_word not in word_followers[word]:
            word_followers[word][next_word] = 1
        else:
            word_followers[word][next_word] += 1


def predict_next_word(count_dict):
    """
    :param count_dict: a dict of words and their counts
    :return: a word, selected randomly from the weighted input list
    """
    # translate count_dict into list of words with cumulative count, e.g.
    # count_dict = {'a':1, 'b':4, 'c': 1}
    # -> cumulative_count_list = [('a', 1), ('b', 5), ('c', 6)]
    words_list = []
    cumulative_counts_list = []
    cumulative_count = 0
    for word, count in count_dict.items():
        cumulative_count += count
        words_list.append(word)
        cumulative_counts_list.append(cumulative_count)

    n = random.randint(0, cumulative_count)
    for i in range(0,len(cumulative_counts_list)):
        if n < cumulative_counts_list[i]:
            return words_list[i]
    return words_list[-1]

def generate_a_sentence(sentence_starters, word_followers):
    sentence = [predict_next_word(sentence_starters)]

    while sentence[-1] is not None:
        next_word = predict_next_word(
                word_followers[
                    sentence[-1]
                ]
            )

        sentence.append(
            next_word
        )

    return ' '.join(sentence[:-1])+'.'




print(
    generate_a_sentence(sentence_starters, word_followers)
)
print(
    generate_a_sentence(sentence_starters, word_followers)
)
print(
    generate_a_sentence(sentence_starters, word_followers)
)
print(
    generate_a_sentence(sentence_starters, word_followers)
)
print(
    generate_a_sentence(sentence_starters, word_followers)
)
