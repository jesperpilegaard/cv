import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Sæt sidekonfiguration
st.set_page_config(page_title="Uddannelse", page_icon="🎓", layout="wide")

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

st.title("Uddannelse")
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.info("""På denne side kan I se lidt statistik over karakterer samt hvor meget hvert fag har vægtet
        på de to uddannelser. Jeg har opdelt det, så min seneste uddannelse, kandidat i Data Science er til venstre,
        mens min bachelor i journalistik står til højre. Alle karakterer, der er "Bestået" eller "Ikke Bestået" 
        er fjernet i barplots og boxplots.
        """)
st.write("""Fra sommer 2017 til vinter 2021 tog jeg min bachelor i journalistik. Derefter har jeg
         arbejdet lidt som journalist, inden jeg i 2022 valgte at tage en kandidat i Data Science for
         at blive klogere på, hvordan data bliver brugt på både godt og ondt i verden, samt hvordan vi
         bedst muligt kan udnytte al den data, vi sidder inde med. Dette færdiggjorde jeg i juni 2024""")

# Kolonner
col1, col2 = st.columns([1, 1])

ds_data = {
    "Fag": [
        "Introduktion til Humanistisk Informatik", "Programmering for Data Science", "Lineær Algebra for Data Science",
        "Datamining og Maskinlæring", "Multivariat Statistisk Analyse", "Databasesystemer", "Anvendt Maskinlæring",
        "IT-sikkerhed, IT-etik og Privathed", "Visualisering", "Statistik for Data Science", "Datadrevne Applikationer",
        "AI Ethics By Design", "News and Market Sentiment Analytics", "Webudvikling", "Speciale i Data Science"
    ],
    "Karakterer": [12, 7, 7, 10, 7, 4, 10, "B", 10, 10, "B", "B", 10, "B", 4],
    "ECTS": [10, 10, 5, 10, 5, 5, 10, 5, 5, 5, 5, 5, 5, 5, 30]
}

jour_data = {
    "Fag": [
        "Journalistisk Håndværk 1", "Mediesprog 1", "Journalistiske Værktøjer: Journalistisk Innovation", "Vidensfag: Sociologi",
        "Refleksionsfag: Journalistikkens Historie, Værdigrundlag og Etik", "Journalistisk Håndværk 2 - Radio",
        "Mediesprog 2", "Journalistiske Værktøjer: Researchtilgange, -Metoder og -Teknikker 1", "Vidensfag: Politik og Forvaltning",
        "Refleksionsfag: Journalistik og Samfund 1", "Journalistisk Håndværk 3 - TV", "Mediesprog 3",
        "Journalistiske Værktøjer: Researchtilgange, -Metoder og -Teknikker 2", "Vidensfag: Økonomi", "Refleksionsfag: Journalistik og Samfund 2",
        "Journalistisk Håndværk 4", "Mediesprog 4", "Journalistiske Værktøjer: Mediejura for Journalister",
        "Vidensfag: International Politik og Organisation", "Refleksionsfag: Kommunikation og Public Relations",
        "Praktik", "Aktuelle Samfundsmæssige Problemer", "Bachelorprojekt"
    ],
    "Karakterer": [7, 10, "B", 10, 12, 7, 10, 7, 7, 7, 4, 7, 12, 4, 7, 2, 2, 4, 7, 4, "B", 7, 10],
    "ECTS": [10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 10, 5, 5, 5, 5, 60, 10, 20]
}

ds_df = pd.DataFrame(ds_data)
jour_df = pd.DataFrame(jour_data)

ds_df2 = ds_df[pd.to_numeric(ds_df["Karakterer"], errors="coerce").notna()]
jour_df2 = jour_df[pd.to_numeric(jour_df["Karakterer"], errors="coerce").notna()]

with col1:

    st.markdown("#### Data Science")

    # Dropdown til valg af diagramtype
    plot_type = st.selectbox("Vælg diagramtype:", ["Bar", "Boxplot"], key="ds_plot_type")

    if plot_type == "Bar":
        st.markdown("#### Karakterfordeling for Data Science")
        # Opretter et bar plot ved hjælp af value_counts
        value_counts = ds_df2["Karakterer"].value_counts().reset_index()
        value_counts.columns = ["Karakter", "Antal fag"]  # Omdøber kolonnerne
        fig = px.bar(value_counts, x="Karakter", y="Antal fag", 
                    labels={"Karakter": "Karakter", "Antal fag": "Antal fag"},
                    title="Karakterfordeling", text_auto=True)
        fig.update_layout(bargap=0)  # Fjerner interval mellem søjlerne

        # Opdater x-aksen til kun at vise de eksisterende karakterer
        fig.update_layout(
            xaxis=dict(
                tickvals=value_counts["Karakter"],  # Brug de faktiske karakterer som tick values
                ticktext=value_counts["Karakter"].astype(str)  # Sørg for at vise karaktererne som tekst
            )
        )

    elif plot_type == "Boxplot":
        st.markdown("#### Karakterfordeling for Data Science")
        fig = px.box(ds_df2, x="Karakterer", title="Boxplot af karakterer")

    # Vis figuren
    st.plotly_chart(fig, use_container_width=True, key="ds_karakterfordeling")

    # Tree Diagram (Treemap) med fag og ECTS
    st.markdown("#### Fag og ECTS for Data Science")

    # Opretter en ny dataframe til treemap-diagrammet
    tree_data = ds_df[["Fag", "ECTS"]].copy()
    tree_data["Kategori"] = "Data Science"  # Kategoriserer alle fag under Data Science

    # Opretter treemap diagram
    tree_fig = px.treemap(tree_data, path=["Kategori", "Fag"], values="ECTS")

    # Vis treemap diagrammet
    st.plotly_chart(tree_fig, use_container_width=True, key="ds_treemap")

with col2:

    st.markdown("#### Journalistik")

    # Dropdown til valg af diagramtype
    plot_type2 = st.selectbox("Vælg diagramtype:", ["Bar", "Boxplot"], key="jour_plot_type")

    if plot_type2 == "Bar":
        st.markdown("#### Karakterfordeling for Journalistik")
        # Opretter et bar plot ved hjælp af value_counts
        value_counts2 = jour_df2["Karakterer"].value_counts().reset_index()
        value_counts2.columns = ["Karakter", "Antal fag"]  # Omdøber kolonnerne
        fig2 = px.bar(value_counts2, x="Karakter", y="Antal fag", 
                    labels={"Karakter": "Karakter", "Antal fag": "Antal fag"},
                    title="Karakterfordeling", text_auto=True)
        fig2.update_layout(bargap=0)  # Fjerner interval mellem søjlerne

        # Opdater x-aksen til kun at vise de eksisterende karakterer
        fig2.update_layout(
            xaxis=dict(
                tickvals=value_counts2["Karakter"],  # Brug de faktiske karakterer som tick values
                ticktext=value_counts2["Karakter"].astype(str)  # Sørg for at vise karaktererne som tekst
            )
        )

    elif plot_type2 == "Boxplot":
        st.markdown("#### Karakterfordeling for Journalistik")
        fig2 = px.box(jour_df2, x="Karakterer", title="Boxplot af karakterer")

    # Vis figuren
    st.plotly_chart(fig2, use_container_width=True, key="jour_karakterfordeling")

    # Tree Diagram (Treemap) med fag og ECTS
    st.markdown("#### Fag og ECTS for Journalistik")

    # Opretter en ny dataframe til treemap-diagrammet
    tree_data2 = jour_df[["Fag", "ECTS"]].copy()
    tree_data2["Kategori"] = "Journalistik"  # Kategoriserer alle fag under Data Science

    # Opretter treemap diagram
    tree_fig2 = px.treemap(tree_data2, path=["Kategori", "Fag"], values="ECTS")

    # Vis treemap diagrammet
    st.plotly_chart(tree_fig2, use_container_width=True, key="jour_treemap")