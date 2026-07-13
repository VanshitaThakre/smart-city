import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="AI Command Center")

# --- UNIQUE DATA FOR EACH CITY ---
data_store = {
    "Nagpur": {
        "Traffic": {"Areas": ["Sadar", "Sitabuldi", "Ramdaspeth", "Civil Lines"], "Score": [85, 92, 45, 30], "Type": "bar"},
        "Water": {"Areas": ["North", "South", "East", "West"], "Score": [70, 85, 60, 95], "Type": "pie"},
        "Safety": {"Areas": ["Zone A", "Zone B", "Zone C", "Zone D"], "Score": [90, 88, 75, 95], "Type": "line"},
        "Healthcare": {"Areas": ["Hosp A", "Hosp B", "Hosp C"], "Score": [95, 80, 85], "Type": "bar"},
        "Pollution": {"Areas": ["Ind-Area", "Resi", "Comm"], "Score": [60, 30, 45], "Type": "pie"},
        "EV": {"Areas": ["St-1", "St-2", "St-3", "St-4"], "Score": [40, 70, 85, 60], "Type": "bar"}
    },
    "Mumbai": {
        "Traffic": {"Areas": ["Andheri", "Dadar", "Colaba", "Bandra"], "Score": [95, 88, 60, 92], "Type": "bar"},
        "Water": {"Areas": ["South Mumbai", "Suburbs", "Navi Mumbai", "Thane"], "Score": [60, 75, 80, 50], "Type": "pie"},
        "Safety": {"Areas": ["Juhu", "Worli", "Borivali", "Goregaon"], "Score": [70, 80, 85, 65], "Type": "line"},
        "Healthcare": {"Areas": ["Lilavati", "Kokilaben", "Sion Hosp"], "Score": [90, 95, 88], "Type": "bar"},
        "Pollution": {"Areas": ["BKC", "Chembur", "Dharavi"], "Score": [70, 85, 50], "Type": "pie"},
        "EV": {"Areas": ["Vile Parle", "BKC", "Lower Parel"], "Score": [50, 90, 75], "Type": "bar"}
    },
    "Pune": {
        "Traffic": {"Areas": ["Hinjewadi", "Baner", "Kothrud", "Viman Nagar"], "Score": [98, 75, 65, 80], "Type": "bar"},
        "Water": {"Areas": ["Kothrud", "Hadapsar", "Wakad", "Pimpri"], "Score": [50, 90, 70, 85], "Type": "pie"},
        "Safety": {"Areas": ["Shivajinagar", "Camp", "Aundh", "Katraj"], "Score": [80, 85, 90, 75], "Type": "line"},
        "Healthcare": {"Areas": ["Ruby Hall", "Jehangir", "Sahyadri"], "Score": [92, 88, 84], "Type": "bar"},
        "Pollution": {"Areas": ["Chakan", "Hadapsar", "Kharadi"], "Score": [55, 40, 35], "Type": "pie"},
        "EV": {"Areas": ["Magarpatta", "Wakad", "Baner"], "Score": [80, 65, 90], "Type": "bar"}
    },
    "Delhi": {
        "Traffic": {"Areas": ["Connaught", "Saket", "Dwarka", "Rohini"], "Score": [90, 85, 70, 95], "Type": "bar"},
        "Water": {"Areas": ["North", "South", "Central", "East"], "Score": [40, 60, 80, 50], "Type": "pie"},
        "Safety": {"Areas": ["Vasant Kunj", "Lajpat Nagar", "Karol Bagh", "Dwarka"], "Score": [65, 90, 85, 70], "Type": "line"},
        "Healthcare": {"Areas": ["AIIMS", "Safdarjung", "Max"], "Score": [98, 92, 88], "Type": "bar"},
        "Pollution": {"Areas": ["Okhla", "Narela", "Punjabi Bagh"], "Score": [95, 88, 75], "Type": "pie"},
        "EV": {"Areas": ["ITO", "Rajouri", "Saket"], "Score": [60, 75, 85], "Type": "bar"}
    }
}

st.markdown("<h1 style='text-align: center; color: #38bdf8;'>AI COMMAND CENTER</h1>", unsafe_allow_html=True)
city = st.selectbox("Select Core Node:", list(data_store.keys()))
tabs = st.tabs(["Traffic", "Water", "Safety", "Healthcare", "Pollution", "EV Charging"])

def render_tab(category):
    data = data_store[city][category]
    df = pd.DataFrame({'Area': data['Areas'], 'Score': data['Score']})
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if data['Type'] == 'bar': fig = px.bar(df, x='Area', y='Score', color='Score', color_continuous_scale='Bluered')
        elif data['Type'] == 'pie': fig = px.pie(df, names='Area', values='Score', hole=0.4)
        else: fig = px.line(df, x='Area', y='Score', markers=True)
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color='white')
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        best_area = df.loc[df['Score'].idxmin() if category in ["Traffic", "Pollution"] else df['Score'].idxmax(), 'Area']
        st.metric(f"{category} Index", f"{int(df['Score'].mean())}%")
        st.success(f"Best Node: **{best_area}**")

for i, tab_name in enumerate(["Traffic", "Water", "Safety", "Healthcare", "Pollution", "EV"]):
    with tabs[i]: render_tab(tab_name)