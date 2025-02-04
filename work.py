import streamlit as st
import pandas as pd
import pydeck as pdk

# Sæt sidekonfiguration
st.set_page_config(page_title="Erhvervserfaring", page_icon="💼", layout="wide")

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

st.title("Erhvervserfaring")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.info("""På denne side kan I læse lidt mere om, hvor jeg har arbejdet. Kortene viser hhv. arbejdssteder 
        i Odense og Aakirkeby. Klik på punkterne for at læse lidt mere om det arbejde, jeg har udført.
        """)


# Kolonner til kortlayout
col1, col2 = st.columns([1, 1])  # Lige store kolonner

# Første kort (Odense)
with col1:
    # Data for steder i Odense, hvor du har arbejdet
    odense_coords = pd.DataFrame({
        "lat": [
            55.40194060523473,  # Scape Technologies A/S
            55.37084079471569,  # PostNord
            55.3625250364327,   # Leica Geosystems
            55.399236892963465, # Lokal TV Fyn
            55.396025043891825  # Christian Firtal
        ],
        "lon": [
            10.40382455431049,  # Scape Technologies A/S
            10.477183164185433, # PostNord
            10.46023092362125,  # Leica Geosystems
            10.3796225418837,   # Lokal TV Fyn
            10.38363165530275   # Christian Firtal
        ],
        "info": [
            "Scape Technologies A/S",
            "PostNord",
            "Leica Geosystems",
            "Lokal TV Fyn",
            "Christian Firtal"
        ],
        "description": [
            "Jeg stod for udtræk, analyse og visualisering af tekstdata fra en af deres robotter, hvilket skal hjælpe med at optimere robottens processer. Formålet er at se, hvilke cyklusser og processer, der tager lang tid for robotten samt finde ud af hvorfor. Jeg har blandt andet udviklet et interaktivt dashboard gennem streamlit, så man lettere kan få indsigter i robottens opgaver. Hele projektet har jeg arbejdet med meget selvstændigt og selv udtænkt, hvordan vi nemmest og bedst muligt kan få dybe indsigter i robottens data. Jeg har arbejdet med Streamlit i Python. Klik på fanen \"Dashboard Scape\" for at se, hvad jeg har lavet.",
            "Som postbud har jeg stået for post- og pakkelevering, altid med et smil på læben for at sørge for den bedst mulilge kundeoplevelse.",
            "Jeg arbejdede med dataanalyse og visualisering af intern data i Microsoft Power BI med formålet at kunne tage databaserede beslutinger. Jobbet gav mig solid erfaring med Power BI samt værdifuld viden inden for, hvordan man internt kan skabe værdi af sine rå data.",
            "Her har jeg stået for alt fra tilrettelæggelse, fotografering, interviews til klipning af endelige programmer. Alt, hvad man kan forestille sig inden for journalistik og videoproduktion. Jeg har lært at arbejde meget selvstændigt med større projekter og og tænkt kreativt i forhold til, hvordan vi bedst muligt kan producere indhold til unge mennesker lokalt.",
            "Christian Firtal er en øl-bar i Odense, der specialiserer sig i specialøl og spiritus. Her har jeg fået god erfaring inden for kundepleje/service samt meget viden inden for øl og spiritus."
        ]
    })

    # Define our Scatterplot layer
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=odense_coords,
        id="Odense",
        get_position=["lon", "lat"],
        get_fill_color=[0, 140, 255, 160],
        get_line_color=[0, 0, 0, 255],
        pickable=True,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=6,
        radius_max_pixels=20,
        line_width_min_pixels=1
    )

    odense_view_state = pdk.ViewState(
        latitude=55.4038,
        longitude=10.4424,
        zoom=10.5,
        bearing=0,
        pitch=0,
    )

    r = pdk.Deck(
        layers=layer,
        initial_view_state=odense_view_state,
        tooltip={"text": "{info}"},
        map_style="mapbox://styles/mapbox/streets-v11"
    )

    event_odense = st.pydeck_chart(r, on_select='rerun', selection_mode="single-object")

# Andet kort (Aakirkeby)
with col2:
    # Data for steder i Aakirkeby
    aakirkeby_coords = pd.DataFrame({
        "lat": [55.07614584190186],
        "lon": [14.914868472018988],
        "info": ["TV 2/Bornholm"],
        "description": ["Jeg arbejdede som videojournalist, reporter, live reporter, vært samt webjournalist. Jeg blev særligt god til at producere mine egne indslag og arbejde på egen hånd. Derudover har jeg fået en god stemmeføring til at speake, samt jeg er god til at bygge en historie op."]
    })

    # Define our Scatterplot layer
    aakirkeby_layer = pdk.Layer(
        "ScatterplotLayer",
        data=aakirkeby_coords,
        id="Aakirkeby",
        get_position=["lon", "lat"],
        get_fill_color=[0, 140, 255, 160],
        get_line_color=[0, 0, 0, 255],
        pickable=True,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=6,
        radius_max_pixels=20,
        line_width_min_pixels=1
    )

    aakirkeby_view_state = pdk.ViewState(
        latitude=55.1461,
        longitude=14.9143,
        zoom=8.9,
        bearing=0,
        pitch=0,
    )

    r2 = pdk.Deck(
        layers=aakirkeby_layer,
        initial_view_state=aakirkeby_view_state,
        tooltip={"text": "{info}"},
        map_style="mapbox://styles/mapbox/streets-v11"
    )

    event_aakirkeby = st.pydeck_chart(r2, on_select='rerun', selection_mode="single-object")

# Infoboks under kortene
st.info("""
    Klik på et punkt på et af kortene for at få information om, hvad jeg har lavet på den valgte arbejdsplads. 
    Hvis du har valgt punktet på Bornholm og vil tilbage til Odense, skal du lige klikke en ekstra gang på punktet, 
    før du kan vælge et punkt i Odense.
""")

# Samlet session-opdatering
selected_event = None

# Kontroller for Odense kort
if event_odense.selection is not None and hasattr(event_odense.selection, "objects"):
    if "Odense" in event_odense.selection.objects:
        selected_event = event_odense.selection.objects["Odense"][0]
        st.session_state["selected_job"] = {
            "info": selected_event["info"],
            "lat": selected_event["lat"],
            "lon": selected_event["lon"],
            "description": selected_event["description"]
        }

# Kontroller for Aakirkeby kort
if event_aakirkeby.selection is not None and hasattr(event_aakirkeby.selection, "objects"):
    if "Aakirkeby" in event_aakirkeby.selection.objects:
        selected_event = event_aakirkeby.selection.objects["Aakirkeby"][0]
        st.session_state["selected_job"] = {
            "info": selected_event["info"],
            "lat": selected_event["lat"],
            "lon": selected_event["lon"],
            "description": selected_event["description"]
        }

# Display selected job if any job is selected
if "selected_job" in st.session_state:
    selected_job = st.session_state["selected_job"]
    st.write(f"**Valgt job**: {selected_job['info']}")
    st.write(f"**Beskrivelse**: {selected_job['description']}")
