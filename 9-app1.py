import streamlit as st


# title
st.title("BMI Calculator")

# height
height=st.number_input("Your height in cm",value=1.5)

# weight
weight=st.number_input("Your weight in kg",value=40)

# calculate bmi
BMI=(weight/height**2)
st.write("Here is your BMI",BMI)

# message alert
# follow classifation below
# http://www.myhealth.gov.my/indeks-jisim-tubuh-ijt/
if BMI<18.5:
    st.warning("You are underweght.")
elif BMI<24.9:
    st.success("You have ideal weight.")
elif BMI<30:
    st.warning("You are overweight.")
else:
    st.error("you are obese.")





# caption
st.caption("Developed by JiaWen")
