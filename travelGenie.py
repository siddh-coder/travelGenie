import streamlit as st
import os
import datetime
import google.generativeai as genai
import csv

def create_top_menu():
    # Using markdown for in-page navigation links
     st.markdown(
        """
        <style>
        .top-menu {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #007BFF; /* Main background color */
            padding: 10px 20px; /* Added padding for a better look */
            border-radius: 8px; /* Rounded corners */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
        }
        .icon {
            display: flex;
            align-items: center;
        }
        .menu-item {
            margin-left: 30px;
            cursor: pointer;
            font-size: 18px;
            color: white; /* Text color */
            text-decoration: none; /* Remove underline */
            padding: 10px; /* Add padding for better click area */
            border-radius: 7px; /* Rounded corners for menu items */
            background-color: white; /* Default background color */
            transition: background-color 0.3s, color 0.3s; /* Smooth transition */
        }
        .menu-item:hover {
            background-color: #007BFF; /* Lighter blue on hover */
            color: #FFD700; /* Gold text on hover */
        }
        .menu-item:active {
            background-color: #003f7f; /* Even darker blue when active */
            color: #FFA500; /* Darker gold on click */
        }
        .logo {
            margin-right: 10px; /* Space between logo and text */
        }
        </style>
        <div class="top-menu">
            <div class="icon">
                <img class="logo" src="https://cdn-icons-png.flaticon.com/512/6213/6213814.png" width="60" height="60">
                <span style="margin-left: 5px; font-size: 32px; color: white;">Welcome to Travel Genie</span>
            </div>
            <div class="menu">
                <a href="#home" class="menu-item">Home</a>
                <a href="#about" class="menu-item">About</a>
                <a href="#contact" class="menu-item">Contact</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(page_title="Travel Genie", layout="wide")
create_top_menu()

st.title('Travel Genie')

key = st.sidebar.text_input('Google Gemini API Key')
st.sidebar.info("You can get your free API key from Google from https://aistudio.google.com/app/u/1/apikey?pli=1")

def generate_response(input_text):
    genai.configure(api_key = key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    st.info(response.text)

with open('worldcities.csv', 'r', encoding='utf-8') as csvfile:
  reader = csv.DictReader(csvfile)  # assumes header row exists
  column_name = 'city'  # replace with the column name you want to read
  predefined_locations = [row[column_name] for row in reader]

with st.form('my_form'):  
	location = st.selectbox("Choose your Starting Location:", predefined_locations)
	destination = st.selectbox("Choose your Destination:", predefined_locations)
	#start_date = st.date_input("Choose your start Date:", value="default_value_today", min_value=datetime.datetime.now(), format="DD/MM/YYYY")
	#end_date = st.date_input("Choose your end Date:", value="default_value_today", min_value=datetime.datetime.now(), format="DD/MM/YYYY")
	start_date = st.date_input("Choose your start Date:", value=datetime.date.today(), min_value=datetime.date.today())
	end_date = st.date_input("Choose your end Date:", value=datetime.date.today(), min_value=start_date)
	haclass = st.selectbox("Choose your Type of Travel:", ['Economy','Business','First Class'])
	
	text = "Give me a Travel Plan to go from " + location + " to " + destination + " between " + str(start_date) + " and " + str(end_date) + " also show the budget in the currency of starting location along with rupees in brackets according to " + haclass
	submitted = st.form_submit_button('Submit')
	if submitted:
		try:
			generate_response(text)	
		except:
			st.error("Enter valid API key!", icon="⚠️")	

# Define sections for navigation
st.write("<div id='home'></div>", unsafe_allow_html=True)  # Home section anchor
st.header("Discover Your Next Adventure with Us!")
st.write("Your journey begins here explore breathtaking destinations, curated travel experiences, and unforgettable memories.")

st.write("<div id='about'></div>", unsafe_allow_html=True)  # About section anchor
st.header("About Section")
st.write("At Wanderwise Journeys, we’re passionate about creating immersive travel experiences that take you beyond the ordinary. Whether you're looking for a serene escape to tropical islands, a thrilling adventure in the mountains, or a cultural exploration in bustling cities, we have the perfect itinerary tailored just for you.")

st.write("<div id='contact'></div>", unsafe_allow_html=True)  # Contact section anchor
st.header("Contact Section")
st.write("Aditya Mittal: Aditya.Mittal@xyz.com")
st.write("Srijan Gupta: Srijan.Gupta@xyz.com")
st.write("Ridwan Umar: Ridwan.Umar@xyz.com")
st.write("Siddharth Tripathi: Siddharth.Tripathi@xyz.com")

