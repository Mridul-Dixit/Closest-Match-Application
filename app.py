import streamlit as st
from fuzzywuzzy import process

items = ['US', 'UK', 'Canada', 'France', 'Germany', 'Italy', 'Japan']

def find_closest_match(user_input, items):
    closest_match, score = process.extractOne(user_input, items)
    return closest_match, score

def main():
    st.title("Closest Match Finder")

    user_input = st.text_input("Type a country:", "")

    if user_input:
        closest_match, score = find_closest_match(user_input, items)
        st.write(f"Closest match: {closest_match} (Score: {score})")

if __name__ == "__main__":
    main()
