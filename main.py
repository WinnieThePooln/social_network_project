# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd


fr = open(r'C:\Users\11046\Desktop\yelp_dataset-2\yelp_academic_dataset_tip.json', 'r', encoding='utf-8')
json_info = fr.read()
tips_df = pd.read_json(json_info, lines=True)
tips_df = tips_df[: 200]
tips_df.to_csv('yelp_academic_dataset_tip.csv', index=False, columns=["text", "date", "compliment_count", "business_id", "user_id"])
print(tips_df.shape)
print(tips_df[:5])

fr = open(r'C:\Users\11046\Desktop\yelp_dataset-2\small_review.json', 'r', encoding='utf-8')
json_info = fr.read()
rv_df = pd.read_json(json_info, lines=True)
rv_df = rv_df[: 200]
rv_df.to_csv('yelp_academic_dataset_tip.csv', index=False, columns=["review_id", "user_id", "business_id", "stars",
                                                                 "date", "text", "useful", "funny", "cool"])
rv_df = rv_df[:200]
print(rv_df.shape)
print(rv_df[:5])

fr = open(r'C:\Users\11046\Desktop\yelp_dataset-2\small_user.json', 'r', encoding='utf-8')
json_info = fr.read()
user_df = pd.read_json(json_info, lines=True)
user_df = user_df[: 200]
user_df.to_csv('yelp_academic_dataset_tip.csv', index=False, columns=["user_id", "name", "review_count", "yelping_since", "friends",
                                                                 "useful", "funny", "cool", "fans", "elite", "average_stars"
                                                                 , "compliment_hot", "compliment_more", "compliment_profile",
                                                                 "compliment_cute", "compliment_list", "compliment_note",
                                                                 "compliment_plain", "compliment_cool", "compliment_funny",
                                                                 "compliment_writer", "compliment_photos"])
print(user_df.shape)
print(user_df[:5])




# Press the green button in the gutter to run the script.

