from dependencies import *

# LOAD english stopwords [stpwrd]
stpwrd = nltk.corpus.stopwords.words('english') 
new_stopwords = ['albert', 'einstein', 'date', 'name'] # after self R&D I've found the necessity to consider these words as stopwords
stpwrd.extend(new_stopwords) 
#LOAD spacy package [nlp]
nlp = spacy.load("en_core_web_lg") 


''' # FUNCTION 01: Preprocessing function'''
def preprocessing(length_of_df, feature_to_preprocess):
    # ps = PorterStemmer()
    lemma = WordNetLemmatizer()
    preprocessed_text_list = []
    for row_i in range(length_of_df):
        text = re.sub('[^a-zA-Z]', ' ', str(feature_to_preprocess[row_i]))       # Cleaning symbols, numbers, punctuations, extra spaces, etc.
        text = text.lower()                                                      # Converting records into lower case.
        text = text.split()
        text = [lemma.lemmatize(word) for word in text if not word in stpwrd]    # Reoving stopwords and applying lemmatizattion.
        text = ' '.join(text)
        preprocessed_text_list.append(text)
    return preprocessed_text_list


'''# FUNCTION 02: Find hyponyms (specific words such as Hyponyms of Parent are father, mother) of each words in a question'''
def hyponyms(word): 
    hyponyms = []
    unnecessary_charecters_front = 8 #there are 8 unnecessary charecters (S y n s e t ( ') before actal hponyms "Synset('passing.n.02')"
    unnecessary_charecters_last = -7  #there are 6 unnecessary charecters (. n . 0 2 ' ) after actual hponyms "Synset('passing.n.02')"
    WORD = word.split(' ')
    for w in WORD:
        synonyms = wn.synsets(w)
        if synonyms:
            for i in synonyms[0].hyponyms(): # synonyms[0].hyponyms(): hyponyms of only 1st class synonyms have been considered.
                i = re.sub('[^a-zA-Z]', ' ', str(i)[unnecessary_charecters_front: unnecessary_charecters_last])
                # i initially include Synset('passing.n.02') but actual hypernym/hyponym word is only 'passing'. To get the actual word the above code is written.
                # print(i)
                hyponyms.append(i)
    return hyponyms


'''# FUNCTION 03: Find hypernym (generalized or abstract such as hypernym of father can be parent) of each words in a question'''
def hypernyms(word):
    hypernym = []
    unnecessary_charecters_front = 8 #there are 8 unnecessary charecters (S y n s e t ( ') before actal hponyms "Synset('passing.n.02')"
    unnecessary_charecters_last = -7 #there are 6 unnecessary charecters (. n . 0 2 ' ) after actual hponyms "Synset('passing.n.02')"
    WORD = word.split(' ')
    for w in WORD:
        synonyms = wn.synsets(w)
        if synonyms:
            for i in synonyms[0].hypernyms(): # synonyms[0].hypernyms(): hypernyms of only 1st class synonyms have been considered.
                i = re.sub('[^a-zA-Z]', ' ', str(i)[unnecessary_charecters_front: unnecessary_charecters_last])
                # i initially include Synset('passing.n.02') but actual hypernym/hyponym word is only 'passing'. To get the actual word the above code is written.
                hypernym.append(i)
    return hypernym


''' # FUNCTION 04: Attach hyponyms and hypernyms with qestion/answer'''
def attach_hyperhypo(preprocessed_texts: list, hyperhypo_similarity_threshold: float):
    text_with_hyperhypo_list = []
    for text in preprocessed_texts:
        text_list = text.split(" ")
        hypo = hyponyms(text)                           # find hyponyms
        hyper = hypernyms(text)                         # find hypernyms
        text_list.extend(hypo)                          # attach hyponyms
        text_list.extend(hyper)                         # arrach hypernyms

        text_str = (" ".join (text_list))               # convert text list into string. Such as ['grand father', 'step mother', 'death season' ] -> "grand father step mother death season"
        text_list_word_by_word = text_str.split(" ")    #convert text string into list. each list element is single word here. Which reduce redundancy. Such as  "grand father step mother death season " -> ['grand', 'father', 'step', 'mother', 'death', 'season']
        old_text_list = text.split(" ")                 # old_text_list will include only base words
        new_text_list = []                              # new_text_list will include unique base words, hyponyms and hypernyms of base words
        
        for base_word in old_text_list:
            new_text_list.append(base_word)
            for hyperhypo_word in text_list_word_by_word:
                if nlp(base_word).similarity(nlp(hyperhypo_word)) > hyperhypo_similarity_threshold:     # if hypernyms and hyponyms have more than 60% similarity with the base words then consider.
                    new_text_list.append(hyperhypo_word)

        new_text_list = Counter(new_text_list)          # unique words 
        new_text_str = " ".join(new_text_list.keys())
        text_with_hyperhypo_list.append(new_text_str)
    return text_with_hyperhypo_list


''' # FUNCTION 05: Create Modified Dataset'''
def create_modified_dataset(base_df, new_df_name: str, preprocessed_FAQ: list, preprocessed_FAQ_Ans: list, FAQ_with_hyperhypo: list):  
    df_new = base_df.copy()
    len_of_base_df = len(base_df)
    df_new['preprocessed_FAQ'], df_new['preprocessed_FAQ_Ans'], df_new['FAQ_with_hyperhypo'] = [preprocessed_FAQ, preprocessed_FAQ_Ans, FAQ_with_hyperhypo]
    Corpus = list(zip(preprocessed_FAQ, preprocessed_FAQ_Ans))                      # combination of preprocessed FAQs and preprocessed Answers
    Corpus = preprocessing(len_of_base_df, Corpus)
    Corpus_new = list(zip(FAQ_with_hyperhypo, preprocessed_FAQ_Ans))                # combination of preprocessed FAQs with hypernyms-hyponyms and preprocessed Answers
    Corpus_new = preprocessing(len_of_base_df, Corpus_new)
    # Corpus_with_hyperhypo = list(zip(FAQ_with_hyperhypo,FAQ_Ans_with_hyperhypo )) # FAQ_Ans_with_hyperhypo: list; combination of preprocessed FAQs with hypernyms-hyponyms and preprocessed Answers with hypernyms-hyponyms
    # Corpus_with_hyperhypo = preprocessing(len_of_base_df, Corpus_with_hyperhypo)
    df_new['Corpus'] = Corpus
    df_new['Corpus_new'] = Corpus_new
    # df_new['Corpus_with_hyperhypo'] =  Corpus_with_hyperhypo
    df_new.to_csv('Taufiq_ML_NLP task_VScode/'+new_df_name); print('Hybrid dataset creation done')
