import streamlit as st
import joblib

model = joblib.load("d:\MACHINE LEARNING PROJECTS\obessity classification\obesity_classification.pkl")

st.header("Are you Obese?  Lets Use Machine Learning to Predict")
st.write()
#st.write("Are you obesse?")
st.write()
st.write("Lets get to work.")

col1,col2 = st.columns(2)
with col1:
    p1 = st.number_input("Enter your Age",1,120)
with col2:
    s1 = st.selectbox("Enter your Gender",('Male','Female'))
    if s1 == 'Male':
        p2=0
    elif s1 == 'Female':
        p2=1
with col1:
    s2 = st.number_input("Enter your height in feets",1.0,10.0)
    p3 = s2*30.48
with col2:
    p4 = st.number_input("Enter your weight(kg)",1,200)

bmi = st.write("Your Body Mass Index is: ",round(p4/(p3/100)**2,2))
p5 = st.number_input("Read your BMI here :point_up_2: and input it here :point_down: ",0.0,50.0)

if st.button("Click to Predict"):
    prediction = model.predict([[p1,p2,p3,p4,p5]])
    if prediction == 0:
        st.success("Your are normal weight")
    elif prediction == 1:
        st.success("You are overweight")
    elif prediction == 2:
        st.success("You are underweight")
    else:
        st.success("Your are obese")

