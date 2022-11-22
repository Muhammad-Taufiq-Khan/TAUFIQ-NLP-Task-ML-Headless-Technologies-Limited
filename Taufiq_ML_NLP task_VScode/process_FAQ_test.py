from function_FAQ_test import *
modified_df_path = '/home/taufiq/Desktop/NLP_Assignment/Taufiq_ML_NLP task_VScode/hybrid_dataset.csv'
modified_df = pd.read_csv(modified_df_path)
FAQs_test_link = "https://raw.githubusercontent.com/Muhammad-Taufiq-Khan/TAUFIQ-NLP-Task-ML-Headless-Technologies-Limited/main/FAQs_test.csv"
df_test = pd.read_csv(FAQs_test_link)


# Test All FAQ test with multiple base features
# base_feature_names = ['preprocessed_FAQ', 'FAQ_with_hyperhypo', 'Corpus', 'Corpus_new']
# for i, base_feature in enumerate(base_feature_names):
#     print(f"\n #{i+1}. Base Feature: {base_feature}")
#     for question in df_test['Question']:
#         Ans = answer(question, modified_df, base_feature); print()


# Test all FAQ-test based on best base-feature
for question in df_test['Question']:
        Ans = answer(question, modified_df, 'FAQ_with_hyperhypo'); print()


# # Test single FAQ-test based on best base-feature
# question = "At what institutions did he study?"
# Ans = answer(question, modified_df, 'FAQ_with_hyperhypo') #;print(f"\nAnswer: {Ans}")

