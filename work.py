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
        i Odense og Aakirkeby. Klik på punkterne for at læse lidt mere om det arbejde, jeg har udført. 🟢 Betyder jobs
        relateret til Data Science, 🔴 er jobs relateret til journalistik, mens 🟡 er andre jobs.
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
            "Som postbud har jeg stået for post- og pakkelevering, altid med et smil på læben for at sørge for den bedst mulige kundeoplevelse.",
            "Jeg arbejdede med dataanalyse og visualisering af intern data i Microsoft Power BI med formålet at kunne tage databaserede beslutinger. Jobbet gav mig solid erfaring med Power BI samt værdifuld viden inden for, hvordan man internt kan skabe værdi af sine rå data.",
            "Her har jeg stået for alt fra tilrettelæggelse, fotografering, interviews til klipning af endelige programmer. Alt, hvad man kan forestille sig inden for journalistik og videoproduktion. Jeg har lært at arbejde meget selvstændigt med større projekter og og tænkt kreativt i forhold til, hvordan vi bedst muligt kan producere indhold til unge mennesker lokalt.",
            "Christian Firtal er en øl-bar i Odense, der specialiserer sig i specialøl og spiritus. Her har jeg fået god erfaring inden for kundepleje/service samt meget viden inden for øl og spiritus."
        ],
        "category": ["Data Science",
                     "Andet",
                     "Data Science",
                     "Journalistik",
                     "Andet"],
        "skills": [
            "Python, Streamlit, Programmering, Dataudtræk, Dataanalyse, Visualisering",
            "Kundeservice, Gode kørefærdigheder, Selvstændigt arbejde",
            "Power BI, Python, DAX, Dataudtræk, Dataanalyse, Visualisering",
            "Videoredigering, Adobe Premiere Pro, Interviews, Tilrettelæggelse, Fotografering",
            "Kundeservice, Øl- og spiritus-aficionado, Ansvarlighed"
        ],
        "image": [
            None,
            None,
            None,
            ["images/lokaltv.jpg", "images/lokaltv2.jpeg", "images/lokaltv3.jpg", "images/lokaltv4.jpg"],
            "images/c41.jpg"
        ],
        "video": [
            None,
            None,
            None,
            "videos/magiske.mov",
            None
        ],
        "video_description": [
            None,
            None,
            None,
            "En lille teaser til et program om Magiske Dage i Odense. Jeg skulle egentlig have været bag kameraet, men en af værterne havde ikke mulighed for at være foran kamera, så jeg måtte hurtigt omstille mig på at skulle være vært i stedet for fotograf.",
            None
        ]
    })

    category_colors = {
        "Data Science": [0, 255, 0, 160],
        "Journalistik": [255, 0, 0, 160],
        "Andet": [255, 255, 0, 160]
    }

    odense_coords["color"] = odense_coords["category"].map(category_colors)

    # Define our Scatterplot layer
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=odense_coords,
        id="Odense",
        get_position=["lon", "lat"],
        get_fill_color="color",
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
        map_style="mapbox://styles/mapbox/outdoors-v12"
    )

    event_odense = st.pydeck_chart(r, on_select='rerun', selection_mode="single-object")

# Andet kort (Aakirkeby)
with col2:
    # Data for steder i Aakirkeby
    aakirkeby_coords = pd.DataFrame({
        "lat": [55.07614584190186],
        "lon": [14.914868472018988],
        "info": ["TV 2/Bornholm"],
        "description": ["Jeg arbejdede som videojournalist, reporter, live reporter, vært samt webjournalist. Jeg blev særligt god til at producere mine egne indslag og arbejde på egen hånd. Derudover har jeg fået en god stemmeføring til at speake, samt jeg er god til at bygge en historie op."],
        "category": ["Journalistik"],
        "skills": ["Videoredigering, Fotografering, Interviews, Speaks, Kreativ skrivning, Analyse, Lokalpolitik"],
        "video": [["videos/soem.mp4", "videos/kontrol.mp4"]],
        "video_description": [["En kort teaser til et sommerprogram på TV 2/Bornholm. Her blev jeg også bare kastet ud i værtsrollen uden at vide, hvad jeg skulle. Det endte med, at jeg skulle lære at stikke et søm i næsen, og det viser bl.a., hvor omstillingsparat jeg er",
                              "Et indslag om de danske grænselukninger; lokalt på Bornholm. Her viser jeg mine evner i at speake og bygge en historie op, mens jeg også er ude i at interviewe på både dansk, engelsk og tysk."]]
    })

    aakirkeby_coords["color"] = aakirkeby_coords["category"].map(category_colors)

    # Define our Scatterplot layer
    aakirkeby_layer = pdk.Layer(
        "ScatterplotLayer",
        data=aakirkeby_coords,
        id="Aakirkeby",
        get_position=["lon", "lat"],
        get_fill_color="color",
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
        map_style="mapbox://styles/mapbox/outdoors-v12"
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
            "description": selected_event["description"],
            "skills": selected_event["skills"],
            "video": selected_event["video"],
            "image": selected_event["image"],
            "video_description": selected_event["video_description"]
        }

# Kontroller for Aakirkeby kort
if event_aakirkeby.selection is not None and hasattr(event_aakirkeby.selection, "objects"):
    if "Aakirkeby" in event_aakirkeby.selection.objects:
        selected_event = event_aakirkeby.selection.objects["Aakirkeby"][0]
        st.session_state["selected_job"] = {
            "info": selected_event["info"],
            "lat": selected_event["lat"],
            "lon": selected_event["lon"],
            "description": selected_event["description"],
            "skills": selected_event["skills"],
            "video": selected_event["video"],
            "video_description": selected_event["video_description"]
        }

if "selected_job" in st.session_state:
    selected_job = st.session_state["selected_job"]
    
    st.write(f"**Valgt job**: {selected_job['info']}")
    st.write(f"**Beskrivelse**: {selected_job['description']}")
    st.write(f"**Kompetencer**: {selected_job['skills']}")

    # Indlejring af LinkedIn-indlæg baseret på job
    if selected_job['info'] == "Scape Technologies A/S":
        st.write(f"**Anbefaling**:")
        linkedin_embed_code = """
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7288568232259522560" 
                height="963" width="504" frameborder="0" allowfullscreen="" title="Indlejret indlæg">
        </iframe>
        """
        st.markdown(linkedin_embed_code, unsafe_allow_html=True)

    if "image" in selected_job and selected_job["image"]:
        if isinstance(selected_job["image"], list):  # Hvis video er en liste
            cols = st.columns(len(selected_job["image"]))  # Opretter kolonner
            for col, image in zip(cols, selected_job["image"]):
                with col:
                    st.image(image)
        else:  # Hvis video er en enkelt string
            st.image(selected_job["image"])

    # Vis videoer, hvis det findes
    if "video" in selected_job and selected_job["video"]:
        if isinstance(selected_job["video"], list):  # Hvis video er en liste
            cols = st.columns(len(selected_job["video"]))  # Opretter kolonner
            for col, video in zip(cols, selected_job["video"]):
                with col:
                    st.video(video)
        else:  # Hvis video er en enkelt string
            st.video(selected_job["video"])

    # Vis videobeskrivelse, hvis det findes
    if "video_description" in selected_job and selected_job["video_description"]:
        if isinstance(selected_job["video_description"], list):  # Hvis video er en liste
            cols = st.columns(len(selected_job["video_description"]))  # Opretter kolonner
            for col, video_description in zip(cols, selected_job["video_description"]):
                with col:
                    st.write(video_description)
        else:  # Hvis video er en enkelt string
            st.write(selected_job["video_description"])
