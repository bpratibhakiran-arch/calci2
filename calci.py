import streamlit as st

st.title("Calculator")

num1 = st.number_input("Enter first no. : ")
num2 = st.number_input("Enter second no. : ")

col1, col2, col3, = st.columns(3)

with col1:
    add = st.button("Add")
    div = st.button("Divide")

with col2:
    sub = st.button("Subtract")
    pow = st.button("Power")

with col3:
    mul = st.button("Multiply")
    per = st.button("Percentage")

if add:
    result = (num1 + num2)
    st.markdown(f"""Answer = {result}""")

elif sub:
    result = (num1 - num2)
    st.markdown(f"""Answer = {result}""")
    
elif mul:
    result = (num1 * num2)
    st.markdown(f"""Answer = {result}""")

elif div:
    result = (num1 / num2)
    st.markdown(f"""Answer = {result}""")

elif pow:
    result = (num1 ** num2)
    st.markdown(f"""Answer = {result}""")

elif per:
    result = ((num1 / 100) * num2)
    st.markdown(f"""Answer = {result}""")

elif per:
    result = ((num1 / 100) * num2)
    st.markdown(f"""Answer = {result}""")

elif per:
    result = ((num1 / 100) * num2)
    st.markdown(f"""Answer = {result}""")
    
elif per:
    result = ((num1 / 100) * num2)
    st.markdown(f"""Answer = {result}""")