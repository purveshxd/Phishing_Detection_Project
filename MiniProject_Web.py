
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score, f1_score

loaded_model = pickle.load(open('phishing.pkl','rb'))

st.title('Phishing Detection')

st.header('Mini Project')

predict_input = st.text_input("Enter link below","") 
predict_input_raw = [predict_input]

# predict_bad = ['yeniik.com.tr/wp-admin/js/login.alibaba.com/login.jsp.php']
# predict_good = ['youtube.com/']
result = loaded_model.predict(predict_input_raw)



print(result)
print("*"*30)
if st.button("check"):
    if result==['bad']:
        st.header('Phishing')
    if result==['good']:
        st.header('Not Phishing')
