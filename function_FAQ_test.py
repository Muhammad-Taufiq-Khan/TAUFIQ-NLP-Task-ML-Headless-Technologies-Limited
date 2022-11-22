# Functions to process single test question

from dependencies import *
from functions import hypernyms, hyponyms, nlp, stpwrd


'''# FUNCTION 06: Function to preprocess test FAQ'''
def preprocessing_single_ques(single_ques_test):
    # ps = PorterStemmer()
    lemma = WordNetLemmatizer()
    question = re.sub('[^a-zA-Z]', ' ', single_ques_test)                           # Cleaning symbols, numbers, punctuations, extra spaces, etc.
    question = question.lower()                                                     # Converting records into lower case.
    question = question.split()
    question = [lemma.lemmatize(word) for word in question if not word in stpwrd]   # Reoving stopwords and applying lemmatizattion
    question = ' '.join(question)
    return question


'''# FUNCTION 07: Attach hypernyms and hyponyms with preprocessed test FAQ text'''
def attach_hyperhypo_single(question):
    question_list = question.split(" ")
    hypo_of_question = hyponyms(question)                       # find hyponyms
    hyper_of_question = hypernyms(question)                     # find hpernyms
    question_list.extend(hypo_of_question)                      # attach hyponyms
    question_list.extend(hyper_of_question)                     # attach hypernms

    question_str = (" ".join (question_list))                   # convert text list into string. Such as ['grand father', 'step mother', 'death season' ] -> "grand father step mother death season"      
    question_list_word_by_word = question_str.split(" ")        #convert text string into list. each list element is single word here. Which reduce redundancy. Such as  "grand father step mother death season " -> ['grand', 'father', 'step', 'mother', 'death', 'season']
    old_Q_list = question.split(" ")                            # old_Q_list will include only base words
    new_Q_list = []                                             # new_Q_list will include unique base words, hyponyms and hypernyms of base words

    for base_q in old_Q_list:
        new_Q_list.append(base_q)
        for hyperhypo_q in question_list_word_by_word: 
            if nlp(base_q).similarity(nlp(hyperhypo_q)) > 0.82: # if hypernyms and hyponyms have more than 82% similarity with the base words then consider.
                new_Q_list.append(hyperhypo_q)

    new_Q_list = Counter(new_Q_list)                            # unique words of a question
    new_Q_str = " ".join(new_Q_list.keys())
    return new_Q_str


''' # FUNCTION 08: Find most similar FAQ of test FAQ and answer it'''
def answer(question_test: str, base_df, base_feature: str ):
    question = preprocessing_single_ques(question_test)
    question = attach_hyperhypo_single(question)
    question_list = question.split(" ")
    question = nlp(question)

    most_similar_FAQ_key = -1
    similarity_dict = {}                                        # will contain similarity score of each FAQ with test/asked question Also contain iteration number (key) of each FAQ in this Dictionary
    similar_FAQ_key = []                                        # will contain key of similar FAQ which has nearly similarity score compared to most similar score key.

    for num, faq in enumerate(base_df[base_feature]):
        faq_list = faq.split(" ")
        for _ in faq_list:
            for __ in question_list:
                if _ == __:                                     # if any word of test FAQ is available in base_features FAQ consider the base_features's FAQ as most similar question
                    most_similar_FAQ_key = num
        similarity_dict[num] = question.similarity(nlp(faq))    # contain similarity score of test FAQ with each base_features's FAQ

    if most_similar_FAQ_key != -1:                              # if any word of test FAQ is available in base_features FAQ
        most_similar_FAQ = base_df['Question'][most_similar_FAQ_key]    
        most_similar_FAQ_Answer = base_df['Answer'][most_similar_FAQ_key]
    else:
        most_similar_FAQ_score = max(similarity_dict.values())  
        most_similar_FAQ_key = max(similarity_dict, key = similarity_dict.get)
        
        # Near to most similar FAQ
        for key, value in similarity_dict.items():
            if value >= (most_similar_FAQ_score - 0.1):         # threshold = 0.1: which FAQ's similarity score is not less than (<) most similarity score - 0.1, consider these as almost similar FAQ
                similar_FAQ_key.append(key)
        similar_FAQ_key.remove(most_similar_FAQ_key)

        most_similar_FAQ = base_df['Question'][most_similar_FAQ_key]     
        most_similar_FAQ_Answer = base_df['Answer'][most_similar_FAQ_key]     
        # print(similarity_dict)
        # print(most_similar_FAQ_score)

    # print(most_similar_FAQ_key)
    print(f"Asked Question: {question_test}")
    # print(f"Similar FAQ: {most_similar_FAQ}")
    print(f"Answer: {most_similar_FAQ_Answer}", end = ' ')
    # For almost similar
    if similar_FAQ_key:
        for key in similar_FAQ_key:
            print(base_df['Answer'][key], end = ' ')    
    print()
    return most_similar_FAQ_Answer
