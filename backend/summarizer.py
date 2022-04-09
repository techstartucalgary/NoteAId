from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk

lemma = nltk.wordnet.WordNetLemmatizer()

def summarize(text: str) -> str:
    words = word_tokenize(text)

    word_freq = dict()
    stopWords = stopwords.words("english") # Words like: I, you, is, was, what, do, have... 
    stopWordsCapital = []
    

    for word in stopWords:
        stopWordsCapital.append(word.capitalize())
        
    punctuationList = ['!', ',', '(', ')', '[', ']', '{', '}', '.', ':']

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

            sentence_scores[sentence[:10]] = sentence_scores[sentence[:10]] // word_count

        return sentence_scores

    # Finds the average of all sentence scores
    def average_score(sentence_scores) -> int:
        sum = 0
        for entry in sentence_scores:
            sum += sentence_scores[entry]
        
        return int(sum / len(sentence_scores))

    sentences = sent_tokenize(text)
    sentence_scores = score_sentences(sentences, word_freq)
    threshold = average_score(sentence_scores) * 0.8 # Adjust this number to increase the summary length

    sentence_count = 0
    summary = ""

    for sentence in sentences:
        if sentence[:10] in sentence_scores and sentence_scores[sentence[:10]] > threshold:
            summary += " " + sentence
            sentence_count += 1

    return summary


