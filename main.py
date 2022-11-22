from functions import *

""" FETCH DATA """
FAQs_link = "https://raw.githubusercontent.com/Muhammad-Taufiq-Khan/TAUFIQ-NLP-Task-ML-Headless-Technologies-Limited/main/FAQs.csv"
df = pd.read_csv(FAQs_link)                                                     ;print("Fetched data - FAQ")


""" PREPROCESSING """
df_len = len(df)
preprocessed_FAQ = preprocessing(df_len, df['Question'])                        ;print("Preprocessing done - FAQ")
preprocessed_FAQ_Ans = preprocessing(df_len, df['Answer'])                      ;print("Preprocessing done - FAQ Ans")


""" ATTACHING HYPONYMS AND HYPERNYMS WITH PREPROCESSED TEXTS """
threshold = 0.6 # hyperhypo similarity threshold
FAQ_with_hyperhypo = attach_hyperhypo(preprocessed_FAQ, threshold)             ;print('Attaching hyper-hypo done - FAQ')
FAQ_Ans_with_hyperhypo = attach_hyperhypo(preprocessed_FAQ_Ans, threshold)     ;print('Attaching hyper-hypo done - FAQ Ans')


""" CREATING HYBRID DATASET """
create_modified_dataset(df, 'hybrid_dataset.csv', preprocessed_FAQ, preprocessed_FAQ_Ans, FAQ_with_hyperhypo, FAQ_Ans_with_hyperhypo)
