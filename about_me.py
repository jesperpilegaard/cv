import streamlit as st

# Sæt sidekonfiguration
st.set_page_config(page_title="Om mig", page_icon="🙋‍♂️", layout="wide")

# Sidebar med kontaktinformationer
st.sidebar.title("📬 Kontakt")
st.sidebar.markdown("""
**📧 Email:** 
<br> jpkristensen93@gmail.com 

**📱 Telefon:** 
<br> +45 42 91 36 90  

**<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" style="width:16px; height:16px; vertical-align:middle; margin-right:5px;"> LinkedIn:** 
<br> [Klik her](https://www.linkedin.com/in/jesper-pilegaard-kristensen-7a3912138/)
""", unsafe_allow_html=True)

# Titel
st.title("Hvem er jeg?")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

# Layout med kolonner
col1, col2 = st.columns([2, 1])  # Fordeler bredden 2:1 mellem venstre og højre kolonne

# Venstre kolonne (tekst)
with col1:
    st.write("""
    Mit navn er Jesper Pilegaard Kristensen, og i juni 2024 afsluttede jeg min uddannelse som Data Scientist, 
    hvilket har givet mig værdifuld viden inden for områder som machine learning, natural language processing, 
    dataanalyse, visualisering, dataetik samt meget mere. 
    Dette gør mig til en stærk kandidat til at bidrage som kollega hos de fleste virksomheder,
    som brænder inde med rå data, enten til analyse, machine learning, AI, visialisering mm.

    Før jeg begyndte på min kandidatuddannelse i Data Science, tog jeg en bachelor i Journalistik på SDU, 
    hvilket jeg mener gør mig særligt velegnet til at formidle komplekse dataindsigter til personer uden samme 
    tekniske baggrund. 
    Derudover viser min overgang fra journalistik til data science min evne til hurtigt at tilegne mig ny viden, 
    og jeg brænder for at bruge min viden til nytte for samfundet, hvorfor jeg mener, at jeg er et godt match hos 
    de fleste virksomheder.

    Som kollega vil I opleve mig som en udadvendt person, der værdsætter sociale relationer på arbejdspladsen, 
    men som også kan fokusere dybt, når opgaver kræver fuld opmærksomhed. 
    Jeg bringer en positiv energi til arbejdspladsen og har en god sans for humor 
    (eller det synes jeg i hvert fald selv).
             
    Her på siden kan I se mere til min arbejdserfaring, uddannelse samt projekter jeg har udført. Klik rundt og få et glimt af mig!
    """)

# Højre kolonne (billede)
with col2:
    st.image("images/migfarve2.jpeg", caption="Jesper Pilegaard Kristensen", use_container_width=True)

    # Faktaboks
    st.markdown("""
    <div style="background-color: #EADBC8; padding: 15px; border-radius: 10px; margin-top: 20px;">
        <h5>📬 Kontaktinformationer</h5>
        <p><strong>Email:</strong> jpkristensen93@gmail.com</p>
        <p><strong>Telefon:</strong> +45 42 91 36 90</p>
        <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/jesper-pilegaard-kristensen-7a3912138/" target="_blank">Klik her</a></p>
    </div>
    """, unsafe_allow_html=True)
