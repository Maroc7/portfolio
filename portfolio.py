import streamlit as st

st.set_page_config(page_title="Mijn Portfolio", page_icon="🧰", layout="centered")

st.title("👋 Welkom op mijn Portfolio")
st.subheader("FTTH Designer | Python Enthousiast | Toekomstig Bouwkundig Tekenaar")

st.write("""
Ik werk momenteel als FTTH Designer met Marlin DT.  
Mijn ambities liggen in de bouwsector én Python development.  
Dit portfolio toont wat ik leer en bouw!
""")

st.header("🔧 Skills")
st.markdown("""
- 📡 FTTH Design (Marlin)
- 🐍 Python scripting
- 📐 Interesse: AutoCAD & Bouwkunde
- 💡 Technisch inzicht, probleemoplossend denken
""")

st.header("📂 Projecten")
st.markdown("""
### 📁 CSV Automatisatie
Tool om automatisch Excel- of CSV-bestanden van kabeldata om te zetten naar juiste structuur.

### ⚙️ Marlin Auto-Schema (In Progress)
Prototype om standaardschema's sneller te genereren voor fiber-projecten.
""")

st.header("📬 Contact")
st.markdown("""
📧 Email: jouw.email@example.com  
💼 LinkedIn: [linkedin.com/in/jouwnaam](https://linkedin.com/in/jouwnaam)  
🐙 GitHub: [github.com/jouwgebruikersnaam](https://github.com/jouwgebruikersnaam)
""")
