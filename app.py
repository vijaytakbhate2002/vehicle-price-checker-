import joblib 
import streamlit as st
import datetime
import numpy as np
from st_btn_select import st_btn_select 

page_bg_img = """<style>
[data-testid="stAppViewContainer"]{
    background-image:url(C:\\Users\\Vijay Takbhate\\Desktop\\Used vehicle\\Application_UVPP\\galaxy.jpg);
    background-color:rgb(236, 211, 131);
    background-size: cover;
}
</style>"""

st.markdown(page_bg_img,unsafe_allow_html=True)

st.markdown("""
<style>
.heading{
  background-color: rgb(255, 112, 0); 
  font-family: cursive;
  font-size: 40px;
  color: black;
  padding: 10px; 
  width: 600px;
  border-radius: 30px;
  font-weight:bold;
}
.sub_head{
  background-color: rgb(255, 112, 0); 
  font-family: cursive;
  font-size: 25px;
  color: black;
  padding: 10px; 
  width: 250px;
  border-radius: 20px;
  font-weight:bold;
}
.label{
  background-color: rgb(255, 195, 0);
  font-family: cursive;
  font-size: 20px;
  color: rgb(0, 0, 153);
  padding: 20px; 
  width: 300px;
  border-radius: 30px;
  font-weight:bold;
}
.med_label{
  background-color: rgb(255, 195, 0);
  font-family: cursive;
  font-size: 20px;
  color: rgb(0, 0, 153);
  padding: 20px; 
  width: 350px;
  border-radius: 30px;
  font-weight:bold;
}
.large_label{
  background-color: rgb(255, 195, 0);
  font-family: cursive;
  font-size: 20px;
  color: rgb(0, 0, 153);
  padding: 20px; 
  width: 500px;
  border-radius: 30px;
  font-weight:bold;
}
</style>""",unsafe_allow_html=True)

st.markdown("""<p class=heading> Used Vehicle Price Checker </p>""",unsafe_allow_html=True)
st.markdown("""<p class=sub_head> Select Vehicle 👇🏾</p>""",unsafe_allow_html=True)

vcl = st_btn_select(("CAR","BIKE"))

# st.markdown(f"<p class=font_size> {vcl}!! <p/>",unsafe_allow_html=True)

today = int(str(datetime.datetime.now()).split()[0].split("-")[0])
def predictor(lis,model,vehicle_name):
    x = np.array(lis)
    result = model.predict([x])
    if vehicle_name == "CAR":
        st.success(f"{vehicle_name} PRICE {100000*result}")
    else:
        st.success(f"{vehicle_name} PRICE {result}")

def MinMaxScalar(num,max_num,min_num):
    max_n = max_num
    min_n = min_num
    res = (num-min_n)/(max_n-min_n)
    return res

if vcl == "CAR":
    # loaded data which is used for training model
    cars_names = joblib.load('Car Names')
    cars_brands = joblib.load("Car Brands") 

    cmodel = joblib.load("car_price_model")
    cmax_km_drive,cmin_km_drive = (6500000, 171)
    
    st.markdown("""<p class=label> Select Car Name 👇🏾</p>""",unsafe_allow_html=True)
    names = sorted(cars_names)
    cname = st.selectbox('',names)
    cname_ind = names.index(cname)
    st.write(cname_ind)

    brand = cname.split()[0]
    cbrand = cars_brands.index(brand)

    st.markdown("""<p class=label> Select Location 👇🏾</p>""",unsafe_allow_html=True)
    locations = ('Ahmedabad', 'Bangalore', 'Chennai', 'Coimbatore', 'Delhi', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata', 'Mumbai', 'Pune')
    clocation = st.selectbox("",locations)
    cloc_ind = locations.index(clocation)
    st.write(cloc_ind)

    st.markdown("""<p class=label> Select Fule Type 👇🏾</p>""",unsafe_allow_html=True)
    fuel = ('CNG', 'Diesel', 'LPG','Petrol')
    cfuel = st_btn_select((fuel))
    cfuel_ind = fuel.index(cfuel)
    st.write(cfuel_ind)

    st.markdown("""<p class=med_label> Select Transmission Mode 👇🏾</p>""",unsafe_allow_html=True)
    transmission = ('Automatic','Manual')
    ctransmission = st_btn_select((transmission))
    ctransmission_ind = transmission.index(ctransmission)
    st.write(ctransmission_ind)

    st.markdown("""<p class=label> Select Owner Type 👇🏾</p>""",unsafe_allow_html=True)
    owner_type = ('First', 'Second', 'Fourth & Above', 'Third')
    owner_type = sorted(owner_type)
    cowner_type = st_btn_select((owner_type))
    cowner_type_ind = owner_type.index(cowner_type)
    st.write(cowner_type_ind)

    st.markdown("""<p class=med_label> Select Number Of seats 👇🏾</p>""",unsafe_allow_html=True)
    seats = ( 5., 7., 8., 4., 6., 2., 10., 9.)
    seats = tuple(sorted(seats))
    cseats = st_btn_select((seats))
    st.write(cseats)

    st.markdown("""<p class=label> Enter Year 👇🏾</p>""",unsafe_allow_html=True)
    cyear = st.number_input('',min_value=1900,max_value=today)

    st.markdown("""<p class=label> Enter Mileage 👇🏾</p>""",unsafe_allow_html=True)
    cmileage = st.number_input(" ")

    st.markdown("""<p class=label> Enter Engine in CC 👇🏾</p>""",unsafe_allow_html=True)
    cengine = st.number_input("  ")

    st.markdown("""<p class=label> Enter Engine Power 👇🏾</p>""",unsafe_allow_html=True)
    cpower = st.number_input("    ")

    st.markdown("""<p class=large_label> Enter vehicle kilometer driven (Km/hr) 👇🏾</p>""",unsafe_allow_html=True)
    ckilometers_driven = st.number_input("")
    ckilometers_driven = MinMaxScalar(ckilometers_driven,cmax_km_drive, cmin_km_drive)


    def cpred_support():
        cx = [cname_ind,cloc_ind,cyear,ckilometers_driven,cfuel_ind,ctransmission_ind,cowner_type_ind,cmileage,cengine,cpower,cseats,cbrand]
        row = predictor(cx,cmodel,"CAR")
    st.button("Show Car Price",on_click = cpred_support)
    
else:
    # loaded data which is used for training model
    bike_names = joblib.load("bike names")
    bike_brands = joblib.load("bike brands")
    bike_city = joblib.load("bike city")
    bike_owner = joblib.load("bike owner")

    # model loading
    bmodel = joblib.load("bike_price_model")


    st.markdown("""<p class=label> Select Brand 👇🏾</p>""",unsafe_allow_html=True)
    bbrand = st.selectbox("",bike_brands)
    bbrand_ind = bike_brands.index(bbrand)

    st.markdown("""<p class=label> Select Bike Name 👇🏾</p>""",unsafe_allow_html=True)
    bname = st.selectbox("",bike_names)
    bname_ind = bike_names.index(bname)

    st.markdown("""<p class=label> Select City 👇🏾</p>""",unsafe_allow_html=True)
    bcity = st.selectbox("",bike_city)
    bcity_ind = bike_city.index(bcity)

    st.markdown("""<p class=med_label> Enter Bike Driven (Kilo meter) 👇🏾</p>""",unsafe_allow_html=True)
    bkms_driven = st.number_input("")

    st.markdown("""<p class=label> Select Owner Type 👇🏾</p>""",unsafe_allow_html=True)
    bowner_type = ('First Owner', 'Fourth Owner Or More', 'Second Owner', 'Third Owner')
    bowner = st_btn_select((bowner_type))
    bowner_ind = bike_owner.index(bowner)

    st.markdown("""<p class=label> Enter Bike Age 👇🏾</p>""",unsafe_allow_html=True)
    bage = st.number_input(" ")

    st.markdown("""<p class=label> Enter Power Of Engine 👇🏾</p>""",unsafe_allow_html=True)
    bpower = st.number_input("  ")

    st.markdown("""<p class=label> Enter CC of Engine 👇🏾</p>""",unsafe_allow_html=True)
    bCC = st.number_input("   ")

    bx = [bname_ind,bcity_ind,bkms_driven,bowner_ind,bage,bpower,bbrand_ind,bCC]
    def bpred_support():
        row = predictor(bx,bmodel,"BIKE")
    st.button("Show Bike Price",on_click=bpred_support)
    
