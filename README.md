# Travel Genie

Travel Genie is a user-friendly travel planning application that helps users generate curated travel plans based on their starting location, destination, and travel preferences. With this app, you can create a personalized itinerary, estimate your travel budget, and explore exciting destinations effortlessly.

---

## Features

- **Interactive UI**: Navigate through a sleek and intuitive interface.
- **Dynamic Date Input**: Select start and end dates for your journey.
- **Travel Class Options**: Choose between Economy, Business, or First-Class travel preferences.
- **Google Gemini API Integration**: Generate travel plans using AI-powered recommendations.
- **Currency Conversion**: Get budgets displayed in your starting location's currency and INR for comparison.
- **CSV Integration**: Predefined locations are read from a `worldcities.csv` file for user convenience.
- **Responsive Design**: Mobile-friendly and adaptable to different screen sizes.

---

## Getting Started

### Prerequisites

1. **Python 3.10+** is required to run the app.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Streamlit** is used for the web interface:
   ```bash
   pip install streamlit
   ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/travel-genie.git
   cd travel-genie
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/u/1/apikey?pli=1).

4. Place your `worldcities.csv` file in the same directory as the app.

---

## Running the App

1. Run the app using Streamlit:
   ```bash
   streamlit run travelGenie.py
   ```

2. Open your browser and navigate to `http://localhost:8501` to use the app.

---

## Usage

1. Enter your **Google Gemini API Key** in the sidebar.
2. Select your **Starting Location** and **Destination** from the dropdown.
3. Choose your **Start Date** and **End Date** for the trip.
4. Select your **Travel Class** (Economy, Business, First-Class).
5. Click **Submit** to generate a travel plan with budget estimates.

---

## File Structure

```
travel-genie/
│
├── travelGenie.py         # Main application file
├── worldcities.csv        # CSV file containing location data
├── requirements.txt       # Python dependencies
├── README.md              # Documentation file
└── env/                   # Virtual environment (optional)
```

---

## Technologies Used

- **Streamlit**: For building the web interface.
- **Python**: Core programming language for the backend.
- **Google Gemini API**: To generate AI-based travel recommendations.
- **CSV**: For managing and reading predefined locations.

---

## Contributors

- **Aditya Mittal**
- **Srijan Gupta**
- **Ridwan Umar**
- **Siddharth Tripathi**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Screenshots

### Homepage
![Homepage](https://cdn-icons-png.flaticon.com/512/6213/6213814.png)

---

## Feedback

We value your feedback! Feel free to open an issue or contribute to the project.
