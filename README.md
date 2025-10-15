# Fake news detector
This project is a simple yet effective Fake News Detection Tool built using Python and Streamlit. It helps users verify whether a given news headline or claim appears on trusted news sources using the Google Custom Search API.

### Features
1. Accepts any news headline or statement as input
2. Searches the web through the Google Custom Search Engine (CSE)
3. Checks whether the claim appears on trusted and verified media websites
4. Displays top relevant search results with snippets and source links

### Provides a verdict:

 Likely True (found on multiple trusted sites)

Possibly True (found on one trusted site)

Possibly Fake (no trusted matches found)

### How It Works

User inputs a headline or claim.

The app calls the Google Custom Search API with the query.

The returned search results are scanned against a predefined list of trusted domains (e.g., BBC, Reuters, The Hindu, NDTV, etc.).

Based on the number of trusted matches, the app provides a simple, interpretable verdict.

Results are displayed with article titles, links, and summaries.

### The Tech Stack

Python 3.x
Streamlit (for the web interface)
Requests (for interacting with Google’s API)

### Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/fake-news-detector.git
cd fake-news-detector

2. Install Dependencies
pip install -r requirements.txt

3. Configure API Credentials

Create a Google Custom Search Engine (CSE) and enable the Custom Search JSON API.
Then, open the Python script and replace:

API_KEY = your own api
CSE_ID = your own cx key

4. Run the Application
streamlit run app.py

Project Structure
├── app.py               Main Streamlit app script
├── requirements.txt     the Dependencies
└── README.md            the Project documentation

#### Some Illustrations:
<img width="1550" height="637" alt="image" src="https://github.com/user-attachments/assets/f9970388-24b6-408d-ac12-42fcbfa9b066" />

<img width="1590" height="774" alt="image" src="https://github.com/user-attachments/assets/3456e35f-f4f6-415e-9d77-29fa420ed40c" />


##### Author

Saptarshi Bandyopadhyay(@saptarshi-ux)
Data & Analytics Professional | Economics & Technology Enthusiast
