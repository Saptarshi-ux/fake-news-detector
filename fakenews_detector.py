import streamlit as st
import requests
import re

API_KEY = "AIzaSyAe4zi5KOt4STxm5Cpw1-nZ_sShtx028LU"
CSE_ID = "32a8cd60782c84012"
URL = "https://www.googleapis.com/customsearch/v1"

st.title("Fake News Detector WebApp by Saptarshi")
st.write("Check if a news headline or claim appears on trusted news sites.")
query = st.text_input("Enter a headline or statement:")
def google_search(query):
    params = {"q": query, "key": API_KEY, "cx": CSE_ID, "num": 5}
    r = requests.get(URL, params=params)
    return r.json().get("items", []) if r.status_code == 200 else []

def get_verdict(results):
    trusted = [
    "bbc", "reuters", "apnews", "guardian", "cnn", "nytimes", "snopes", "factcheck.org",
    "factly", "ndtv", "politifact", "indiatoday", "thehindu", "indianexpress", 
    "timesofindia", "hindustantimes", "anandabazar", "eisamay", "bloomberg", 
    "forbes", "economictimes", "thestatesman", "livemint", "telegraphindia",
    "newslaundry", "thequint", "business-standard", "espn", "goal.com",
    "skysports", "espncricinfo", "cricbuzz", "onefootball", "wikipedia"
]

    count = sum(any(t in r["link"].lower() for t in trusted) for r in results)
    if count >= 2:
        return "✅ Likely True (found on multiple trusted sites)"
    elif count == 1:
        return "Not sure whether it is True or False but found on one trusted source"
    else:
        return "Possibly Fake"

if st.button("Check"):
    if not query.strip():
        st.warning("Please enter something first.")
    else:
        with st.spinner("Searching trusted sources..."):
            results = google_search(query)
            if not results:
                st.error("No results found. Might be new or unverified.")
            else:
                verdict = get_verdict(results)
                st.success(verdict)
                st.markdown("### 🔍 Top Search Results:")
                for r in results:
                    st.markdown(f"**[{r['title']}]({r['link']})**")
                    snippet = re.sub(r'\s+', ' ', r.get('snippet', ''))
                    st.caption(snippet)
