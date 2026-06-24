import streamlit as st
st.title("METRO + CAB BOOKING")
#Metro Stations List
stations=[
    "SELECT",
    "JNTUH",
    "MYP",
    "Ameerpet",
    "LBNagar"
]
from_station=st.selectbox("From Satation",stations)
to_station=st.selectbox("To Station",stations)
tickets=st.number_input("Number of Tickets",min_value=1,value=1)
need_cab=st.radio("Do You need a cab ?",
                  ["Yes","No"],index=None)
cab_destination=""
cab_fare=0
if need_cab=="Yes":
    cab_destination=st.text_input("Destination")
    cab_fare=130
if st.button("BOOK"):
    if from_station==to_station:
        st.error("Both Stations are same!")
    else:
        bill=40*tickets
        metro_fare=30 * tickets
        total=metro_fare+cab_fare+bill
        st.success("Booking Done!")
        st.subheader("***Bill Details***")
        st.write(f"From Station: {from_station}")
        st.write(f"To Station :{to_station}")
        st.write(f"Tickets : {tickets}")
        st.write(f"metro :{metro_fare}")
        st.write(f"bill is :{bill}")
        if need_cab=="Yes":
            st.write(f"Cab From:{to_station}")
            st.write(f"to : {cab_destination}")
            st.write(f"cab bill:{cab_fare}")
            st.write(f"---Total----{total}")
