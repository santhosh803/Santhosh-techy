''' from gravityai import gravityai as grav '''
import pandas as pd
import pickle

rfc_model = pickle.load(open('rfc_article.pkl', 'rb'))  # Random Forest Classifier
ld = pickle.load(open('label_encoder_article.pkl', 'rb')) # Lable Encoder
vectorizer = pickle.load(open('vectorizer_for_article.pkl', 'rb')) # Vectorizer for 'body' column of an article data set

def process(inPath, outPath):
    df = pd.read_csv(inPath)

    vectorizer_x = vectorizer.transform(df['body'])

    predictions = rfc_model.predict(vectorizer_x)

    df['category'] = ld.inverse_transform(predictions)

    out_df = df[['id', 'category']]
    out_df.to_csv(outPath, index=False)

process('test_set.csv', 'output_for_test_set.csv')

''' grav.wait_for_requests(process) '''