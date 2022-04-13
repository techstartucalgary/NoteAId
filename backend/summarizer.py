from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk

lemma = nltk.wordnet.WordNetLemmatizer()


def summarize(text: str, summary_level: str) -> str:
    words = word_tokenize(text)

    word_freq = dict()

    # Words like: I, you, is, was, what, do, have...
    stopWords = stopwords.words("english")
    stopWordsCapital = []

    for word in stopWords:
        stopWordsCapital.append(word.capitalize())

    punctuationList = ['.', ',', '!', ':', '(', ')', '[', ']', '{', '}']

    stopWords.extend(punctuationList)
    stopWords.extend(stopWordsCapital)

    stopWords = set(stopWords)

    # Finds the frequency of each word stem in the text
    for word in words:
        word = lemma.lemmatize(word)
        if word in stopWords:
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # #Test sorted list of words
    # sorted_list = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    # for word in sorted_list:
    #     if sorted_list[word] >= 3:
    #         print(word, sorted_list[word])
    # print(word_freq)

    # Gives a score to each sentence
    def score_sentences(sentences, word_freq) -> dict:
        sentence_scores = dict()

        for sentence in sentences:
            word_count = len(word_tokenize(sentence))
            for wordValue in word_freq:
                if wordValue in sentence.lower():
                    if sentence[:10] in sentence_scores:
                        sentence_scores[sentence[:10]] += word_freq[wordValue]
                    else:
                        sentence_scores[sentence[:10]] = word_freq[wordValue]

            sentence_scores[sentence[:10]
                            ] = sentence_scores[sentence[:10]] // word_count

        return sentence_scores

    # Finds the average of all sentence scores
    def average_score(sentence_scores) -> int:
        sum = 0
        for entry in sentence_scores:
            sum += sentence_scores[entry]

        return int(sum / len(sentence_scores))

    sentences = sent_tokenize(text)

    # Pick the top n scores from this list --> sentence_scores based off user summary level
    sentence_scores = score_sentences(sentences, word_freq)

    sorted_scores = list(sentence_scores.items())
    sorted_scores.sort(key=lambda tup: tup[1], reverse=True)

    if summary_level == 'long':
        # Low summarization of the raw text. Almost nothing
        multiplier = 0.70  # Percentage of original text
    elif summary_level == 'normal':
        multiplier = 0.50
    elif summary_level == 'short':
        multiplier = 0.30

    num_of_sentences = round(multiplier * len(sorted_scores))

    # Slice the list
    sorted_scores = sorted_scores[:num_of_sentences]
    summary_sentences = dict(sorted_scores)

    # Construct the summary:
    sentence_count = 0
    summary = ""
    for sentence in sentences:
        if sentence[:10] in summary_sentences:
            summary += sentence + " "
            sentence_count += 1

    return summary
