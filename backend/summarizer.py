from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def summarize(text: str) -> str:
    # text = "The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The novel virus was first identified in the Chinese city of Wuhan in December 2019; a lockdown in Wuhan and other cities in surrounding Hubei failed to contain the outbreak, and it quickly spread to other parts of mainland China and around the world. The World Health Organization (WHO) declared a Public Health Emergency of International Concern on 30 January 2020, and a pandemic on 11 March 2020. Multiple variants of the virus have emerged and become dominant in many countries since 2021, with the Alpha, Beta, Gamma and Delta variants being the most virulent. As of 18 November 2021, more than 255 million cases and 5.12 million deaths have been confirmed, making the pandemic one of the deadliest in history. COVID-19 symptoms range from none to life-threatening. Severe illness is more likely in elderly patients and those with certain underlying medical conditions. Transmission of COVID-19 occurs when people breathe in air contaminated by droplets and small airborne particles. The risk of breathing these in is highest when people are in close proximity, but the virus can transmit over longer distances, particularly indoors and in poorly ventilated areas. Transmission can also occur, rarely, via contaminated surfaces or fluids. People remain contagious for up to 20 days, and can spread the virus even if they do not develop symptoms. Several vaccines have been approved and distributed in various countries, which have initiated mass vaccination campaigns since December 2020. Other recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, covering one's mouth when sneezing or coughing, hand washing, disinfecting surfaces, and quarantining people who have been exposed or are symptomatic. Treatments focus on addressing symptoms, but work is underway to develop medications that inhibit the virus. Authorities worldwide have responded by implementing travel restrictions, lockdowns, business closures, workplace hazard controls, testing protocols, and systems for tracing contacts of the infected."
    words = word_tokenize(text)

    word_freq = dict()
    stopWords = set(stopwords.words("english")) # Words like: I, you, is, was, what, do, have... 
    stemmer = PorterStemmer()

    # Finds the frequency of each word stem in the text
    for word in words:
        word = stemmer.stem(word)
        if word in stopWords:
            continue
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

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
    threshold = average_score(sentence_scores) * 1.0 # Adjust this number to increase the summary length

    sentence_count = 0
    summary = ""

    for sentence in sentences:
        if sentence[:10] in sentence_scores and sentence_scores[sentence[:10]] > threshold:
            summary += " " + sentence
            sentence_count += 1

    return summary