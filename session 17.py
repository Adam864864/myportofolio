import streamlit as st

# Page Config
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar
with st.sidebar:
    st.title("adam muhamed")
    st.markdown("📍 Location")
    st.markdown("💼 ")
    st.markdown("🐙 [GitHub](https://github.com/jiraiyam)")
    st.markdown("📧 adamabusalama@gmail.com")

# Header
st.title("👋 Welcome to My Portfolio")
st.write("I'm a student and I am working in python.")

# Skills
st.header("🛠 Skills")
skills = {
    "Programing": ["Python"],
    "Data Science": ["Pandas", "Scikit-learn", "XGBoost"],
    "Visualization": ["Matplotlib", "Seaborn", "Plotly", "Power BI"],
    "Web/Tools": ["Streamlit","Git",'word']
}

cols = st.columns(2)
for i, (skill, items) in enumerate(skills.items()):
    with cols[i % 2]:
        st.subheader(skill)
        st.write(", ".join(items))

# Projects
st.header("📂 Projects")
project_data = [
    {
        "title": "calculator",
        "description": "calculating any numbers , only write your number and the sign you want and you get the answer.",
        "link": "https://projects-vncfhadgmq3zrtktfzovya.streamlit.app/"
    },
    {
        "title": "Covid-19 Data Dashboard",
        "description": "Interactive dashboard with COVID-19 data using Plotly and Streamlit.",
        "link": "https://github.com/yourusername/covid-dashboard"
    },
    {
        "title": "snakeandladder",
        "description": "roll the dice until you win the game.",
        "link": "https://snakeandladder.streamlit.app/"
    },
]

for project in project_data:
    st.subheader(project["title"])
    st.write(project["description"])
    st.markdown(f"[🔗 View Project]({project['link']})")

# Contact Form
st.header("📬 Contact Me")
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        st.success("Thanks for reaching out! I'll get back to you soon.")