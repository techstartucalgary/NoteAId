from cgitb import text
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import spacy
import pytextrank

lemma = nltk.wordnet.WordNetLemmatizer()

#textVariable = "The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The novel virus was first identified in the Chinese city of Wuhan in December 2019; a lockdown in Wuhan and other cities in surrounding Hubei failed to contain the outbreak, and it quickly spread to other parts of mainland China and around the world. The World Health Organization (WHO) declared a Public Health Emergency of International Concern on 30 January 2020, and a pandemic on 11 March 2020. Multiple variants of the virus have emerged and become dominant in many countries since 2021, with the Alpha, Beta, Gamma and Delta variants being the most virulent. As of 18 November 2021, more than 255 million cases and 5.12 million deaths have been confirmed, making the pandemic one of the deadliest in history. COVID-19 symptoms range from none to life-threatening. Severe illness is more likely in elderly patients and those with certain underlying medical conditions. Transmission of COVID-19 occurs when people breathe in air contaminated by droplets and small airborne particles. The risk of breathing these in is highest when people are in close proximity, but the virus can transmit over longer distances, particularly indoors and in poorly ventilated areas. Transmission can also occur, rarely, via contaminated surfaces or fluids. People remain contagious for up to 20 days, and can spread the virus even if they do not develop symptoms. Several vaccines have been approved and distributed in various countries, which have initiated mass vaccination campaigns since December 2020. Other recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, covering one's mouth when sneezing or coughing, hand washing, disinfecting surfaces, and quarantining people who have been exposed or are symptomatic. Treatments focus on addressing symptoms, but work is underway to develop medications that inhibit the virus. Authorities worldwide have responded by implementing travel restrictions, lockdowns, business closures, workplace hazard controls, testing protocols, and systems for tracing contacts of the infected."
textVariable2 = """The Flames were the result of the NHL's first pre-emptive strike against the upstart World Hockey Association (WHA).[3] In December 1971, the NHL hastily granted a team to Long Island — the New York Islanders — in an attempt to keep the WHA's New York Raiders out of the recently completed Nassau Veterans Memorial Coliseum. Needing another team to balance the schedule, the NHL awarded a team to the Atlanta-based group that owned the National Basketball Association's Atlanta Hawks, headed by prominent local real estate developer Tom Cousins.[4] Cousins named the team the Flames after the fire resulting from the March to the Sea in the American Civil War by General William Tecumseh Sherman, in which Atlanta was nearly destroyed. They played home games in the Omni Coliseum in downtown Atlanta.[5]  The Flames were relatively successful early on. Under head coaches Bernie Boom Boom Geoffrion, Fred Creighton and Al MacNeil, the Flames made the playoffs in six of eight seasons in Atlanta.[6] In marked contrast, their expansion cousins, the Islanders, won only 31 games during their first two years in the league combined.[7] However, this success did not carry over to the playoffs, as the Flames won only two postseason games during their time in Atlanta.[8]  Despite the on-ice success, the Atlanta ownership was never on sound financial footing. Longtime general manager Cliff Fletcher said years later that Cousins' initial financial projections for an NHL team did not account for the WHA entering the picture.[9] The Flames were also a poor draw, and never signed a major television contract.[5]  In 1980, Cousins was in considerable financial difficulty and was forced to sell the Flames to stave off bankruptcy. With few serious offers from local groups, he was very receptive to an offer from Canadian entrepreneur (and former Oilers owner) Nelson Skalbania. He was fronting a group of Calgary businessmen that included oil magnates Harley Hotchkiss, Ralph T. Scurfield, Norman Green, Doc and Byron Seaman, and former Calgary Stampeders great Norman Kwong.[5] A last-ditch effort to keep the team in Atlanta fell short, and Cousins sold the team to Skalbania for US$16 million, a record sale price for an NHL team at the time.[9] On May 21, 1980, Skalbania announced that the team would move to Calgary.[10] He chose to retain the Flames name, feeling it would be a good fit for an oil town like Calgary, while the flaming "A" logo was replaced by a flaming "C".[11] Skalbania sold his interest in 1981, and the Flames have been locally owned since.[12] Early years in Calgary (1980–1985)  Unlike the WHA's Calgary Cowboys, who folded three years earlier, the Flames were immediately embraced by the city of Calgary. While the Cowboys could manage to sell only 2,000 season tickets in their final campaign of 1976–77, the Flames sold 10,000 full- and half-season ticket packages in the 7,000 seat Stampede Corral.[13] Brad Marsh with the Flames during the 1980–81 season. The team found greater playoff success, qualifying for the Stanley Cup playoffs for their first five years after moving to Calgary.  Led by Kent Nilsson's 49-goal, 131-point season, the Flames qualified for the playoffs in their first season in Calgary with a 39–27–14 record, good for third in the Patrick Division.[14] The team found much greater playoff success in Calgary than it did in Atlanta, winning their first two playoff series over the Chicago Black Hawks and Philadelphia Flyers before bowing out to the Minnesota North Stars in the semi-finals.[15] This early success was not soon repeated. After a losing record in 1981–82, Fletcher jettisoned several holdovers from the Atlanta days who could not adjust to the higher-pressure hockey environment and rebuilt the roster.[9][16] Over the next three seasons, he put together a core of players that remained together through the early 1990s.  Fletcher's efforts to match the Oilers led him to draw talent from areas previously neglected by the NHL. The Flames were among the earliest teams to sign large numbers of U.S. college players, including Joel Otto, Gary Suter and Colin Patterson.[17] Fletcher also stepped up the search for European hockey talent, acquiring Hakan Loob and other key players. He was among the first to draft players from the Soviet Union, including CSKA Moscow star Sergei Makarov in 1983, but Soviet players were not released to Western teams until 1989.[18] Still, the team was sufficiently improved to challenge the Oilers, who required the maximum seven games to defeat the Flames en route to their 1984 Stanley Cup Championship.[19]  In 1983, the Flames moved into their new home, the Olympic Saddledome (now known as the Scotiabank Saddledome). Located on the grounds of the Calgary Exhibition and Stampede, the Saddledome was built as a venue for the 1988 Winter Olympics. In three seasons in the Corral, the Flames lost only 32 home games.[10] The Saddledome hosted the NHL All-Star Game in 1985, a 6–4 victory by the Wales Conference.[20] Presidents' Trophies and Stanley Cup Finals (1985–1990)  The players acquired by Fletcher matured into one of the strongest teams in the NHL during the mid-1980s and early 1990s. From 1984–85 to 1990–91, the Flames tallied 90 points in every season but one.[21] However, they were usually unable to transform that success into a deep playoff run, largely because they could not get the better of their provincial rivals, the powerhouse Edmonton Oilers. The Oilers and Flames usually finished at or near the top of the Campbell Conference and were usually among the best teams in the entire league during this time. However, the NHL's playoff structure of the time made it very likely the Flames would meet the Oilers in either the first or second round, rather than in the Campbell Conference finals.[9] That same structure made it very likely that the other two playoff qualifiers in the Smythe Division would have to get past the Flames or Oilers (or both) in order to make it to the conference finals.[22] From 1983 until 1990, either the Oilers or the Flames represented the Campbell Conference in the Stanley Cup Finals.[23] By 1986, the Flames landed forwards Doug Risebrough, Lanny McDonald and Dan Quinn, defenceman Al MacInnis and goaltender Mike Vernon. Finishing second in the Smythe with a 40–31–9 record (the only season from 1984 to 1991 in which they did not finish with 90 or more points),[14] the Flames swept the Winnipeg Jets in the first round of the playoffs,[19] setting up a showdown with the Oilers. Edmonton finished 30 points ahead of Calgary during the season, and was heavily favoured to win a third Cup in a row. However, the Flames upset the Oilers in seven games, the only time the Flames defeated the Oilers in a playoff series in the decade. The series-winning goal came when an errant clearing attempt by Steve Smith ricocheted off goaltender Grant Fuhr's leg and into his own net.[24] The goal remains one of the most legendary blunders in hockey history.[25][26][27]  From there, the Flames went on to the Campbell Conference Finals, where they defeated the St. Louis Blues in another seven-game series. This time, Calgary had to survive a scare of its own, shaking off the Monday Night Miracle at the St. Louis Arena. Trailing by a score of 5–2 with ten minutes to play in the third period of Game 6, the Blues mounted a furious comeback to send the contest into overtime, where Doug Wickenheiser scored to force a deciding seventh game.[28] Calgary won Game 7 at home, 2–1, advancing into the Stanley Cup Finals for the first time.[19] The Flames proved to be no match for the Montreal Canadiens, losing the championship series in five games. Montreal rookie goaltender Patrick Roy was nearly unbeatable in the last two games, allowing only four goals en route to winning the Conn Smythe Trophy. """


nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("textrank")

doc = nlp(textVariable2)

nlp.pipe_names
nlp.analyze_pipes(pretty=True)

# examine the top-ranked phrases in the document
""" for phrase in doc._.phrases:
    print(phrase.text)
    print(phrase.rank, phrase.count)
    print(phrase.chunks) """

def summarize(text: str) -> str:
    #text = "The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The novel virus was first identified in the Chinese city of Wuhan in December 2019; a lockdown in Wuhan and other cities in surrounding Hubei failed to contain the outbreak, and it quickly spread to other parts of mainland China and around the world. The World Health Organization (WHO) declared a Public Health Emergency of International Concern on 30 January 2020, and a pandemic on 11 March 2020. Multiple variants of the virus have emerged and become dominant in many countries since 2021, with the Alpha, Beta, Gamma and Delta variants being the most virulent. As of 18 November 2021, more than 255 million cases and 5.12 million deaths have been confirmed, making the pandemic one of the deadliest in history. COVID-19 symptoms range from none to life-threatening. Severe illness is more likely in elderly patients and those with certain underlying medical conditions. Transmission of COVID-19 occurs when people breathe in air contaminated by droplets and small airborne particles. The risk of breathing these in is highest when people are in close proximity, but the virus can transmit over longer distances, particularly indoors and in poorly ventilated areas. Transmission can also occur, rarely, via contaminated surfaces or fluids. People remain contagious for up to 20 days, and can spread the virus even if they do not develop symptoms. Several vaccines have been approved and distributed in various countries, which have initiated mass vaccination campaigns since December 2020. Other recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, covering one's mouth when sneezing or coughing, hand washing, disinfecting surfaces, and quarantining people who have been exposed or are symptomatic. Treatments focus on addressing symptoms, but work is underway to develop medications that inhibit the virus. Authorities worldwide have responded by implementing travel restrictions, lockdowns, business closures, workplace hazard controls, testing protocols, and systems for tracing contacts of the infected."
    words = word_tokenize(text)

    word_freq = dict()
    stopWords = stopwords.words("english") # Words like: I, you, is, was, what, do, have... 
    stopWordsCapital = stopwords.words("english")

    for word in stopWordsCapital:
        word.capitalize()
    punctuationList = ['!', ',', '(', ')', '[', ']', '{', '}', '.', ':', 'The' ]
    stemmer = PorterStemmer()

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

    
    
    sorted_list = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

    for word in sorted_list:
        if sorted_list[word] >= 3:
            print(word, sorted_list[word])
            

        
    print(word_freq)

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

summarize(textVariable2)