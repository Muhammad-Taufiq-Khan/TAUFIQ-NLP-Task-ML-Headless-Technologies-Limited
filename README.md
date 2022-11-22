# TAUFIQ-NLP-Task-ML-Headless-Technologies-Limited
The reposity contains the assignment for the position of AI/NLP Engineer at Headless Technologies Limited. 

- There the Google Colab file [TAUFIQ_ML_NLP_Task.ipynb](https://github.com/Muhammad-Taufiq-Khan/TAUFIQ-NLP-Task-ML-Headless-Technologies-Limited/blob/main/TAUFIQ_ML_NLP_Task.ipynb) contains the solution.

- Also the directory "Taufiq_ML_NLP task_VScode" contains the solution for vs code usage. The files in the directory is described below.
```
    1. dependency.py        : contains code snippet to setup dependency.
    2. function_FAQ_test.py : User defined function to process the questions of FAQ-test dataset or new input question.
    3. functions_FAQ.py     : User defined function to process the FAQ dataset.
    5. hybrid_dataset.csv   : A new hybrid dataset generated after processing FAQ dataset.
    6. process_FAQ.py       : Scripts to process FAQ dataset and generate the new hybrid dataset.
    7. process_FAQ_test.py  : Scripts to process FAQ-test dataset and new input question.
    8. requirements.txt     : Required libraries to setup dependencies.
```

*[Any of the above (either Google Colab or VS code) can be used to execute the solution. I'll recommand the google colab file as it requires only 2 minutes to execute including installing dependencies.]*

For better understanding I've written a pseudocode of the solution below.

## **Pseudocode of the solution**
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
