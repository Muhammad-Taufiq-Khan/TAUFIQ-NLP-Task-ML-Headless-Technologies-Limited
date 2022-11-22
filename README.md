# TAUFIQ-NLP-Task-ML-Headless-Technologies-Limited

## *Algorithm of the approach*
```
Fetch FAQ dataset

function Preprocess FAQ and FAQ Answers (FAQ dataset):
    Remove punctuations
    Convert texts into lower case
    Lemmatize each words
    return preprocessed FAQ, preprocessed FAQ's Answers
end function

function Find Hyponyms and Hypernyms and Attach with Preprocessed FAQ (preprocessed FAQ):
    find hyponyms and hypernyms of each word of preprocessed FAQ's
    if hypernyms and hyponyms are >= 60% similar with base words:       // base word: word in preprocessed FAQ
        attach hypernyms and hyponyms with processed FAQ
        keep FAQ's words unique
    end if
    return preprocessed FAQ with Hyponyms and Hypernyms
end function

function Create New Hybrid Dataset (preprocessed FAQ, preprocessed FAQ's Answer, preprocessed FAQ with Hyponyms and Hypernyms):
    ''' 
    the hybrid dataset includes 7 (seven) features: 
    1. Question: Given questions in the FAQ dataset.
    2. Answer: Given Answers in the FAQ dataset.
    3. Preprocessed FAQ: Preprocessed Questions.
    4. Preprocessed FAQ Answer:Preprocessed Answers.
    5. Preprocessed FAQ with hyperhypo: Preprocessed questions with their hyponyms and hypernyms.
    6. Corpus: combination of Preprocessed FAQ and Preprocessed FAQ Answer.
    7. Corpus New: Preprocessed FAQ with hyperhypo and Preprocessed FAQ Answer. 
    
    Here feature 3 to 7 are base features.
    '''
    return Hybrid Dataset
end function

function Process FAQ-test data (FAQ-test question):
    preprocess FAQ-test question                                                 //according to previous preprocessing
    find hyponyms and hypernyms and attach with preprocessed FAQ-test question   //according to previous preprocessing
        // here we consider 82% similar hyponyms and hypernyms
    return preprocessed FAQ-test question with hyperhypo
end function

function Validate the Approach (preprocessed FAQ-test question with hyperhypo):
    for feature in base features:
        for question in feature:
            if preprocessed FAQ-test question with hyperhypo and question include any similar word:
                consider that question as most similar question
            end if 
            else:
                check similarity between preprocessed FAQ-test question with hyperhypo and question
                consider question with max similarity score
                if there is any question with similarity >= max similarity score - 10%
                    also consider that question
                end if
            end else
        end for 
    end for
    return best base feature, result
end function

function Test Question Answer (Asked Qestion, Best Base Feature):
    Asked Qestion = Process FAQ-test data (Asked Qestion)
    for question in Best Base Feature: 
        if Asked Qestion and qestion include any similar word:
            consider that question as most similar question
        end if 
        else:
            check similarity between Asked Qestion and question
            consider question with max similarity score
            if there is any question with similarity >= max similarity score - 10%
                also consider that question
            end if
        end else 
    end for 
    return Answer of the considered qestions
end function
```
