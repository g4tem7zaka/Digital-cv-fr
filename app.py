
from pathlib import Path

import streamlit as st
from PIL import Image

    
# --- PATH SETTINGS ---
current_dir = Path.cwd() / "styles"
css_file = current_dir / "main.css"
resume_file = current_dir.parent / "assets" / "CV.pdf"
profile_pic = current_dir.parent / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digitale | Zakaria TEMOUCH"
PAGE_ICON = ":wave:"
NAME = "ZAKARIA TEMOUCH"
DESCRIPTION = """
Étudiant en Master - Ingénierie des Énergies Renouvelables et Efficacité Énergétique\n
Procédées Thermiques et Valorisation de l'Énergie
"""
EMAIL = "zakariatemouch@gmail.com"
TEL = "+212 696 79 16 27"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/zakariatemouch",
    "CV Digitale - Version Anglais": "https://zakaria-temouch.onrender.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write('\n')
    st.write('\n')
    st.write('\n') 
    st.image(profile_pic, width=260)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger mon C.V",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("☎", TEL)


# --- SOCIAL LINKS ---

cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.write('\n')    
# --- EDUCATION ---


def display_bio():
    st.header("PROFIL")
    st.write('\n')
    st.write("Je poursuis actuellement un master en Ingénierie des Energies Renouvelables et Efficacité Energétique avec une spécialisation en Procédés Thermiques et Valorisation de l'Energie. Mon expérience inclut des stages où j'ai acquis des compétences en dimensionnement, installation de systèmes photovoltaïques et la maintenance des équipements thermiques. Je maîtrise la modélisation énergétique, l'analyse CFD, les audits énergétiques, la gestion de projets en énergies renouvelables, ainsi que la programmation en Python et Java Script. Mes projets académiques ont renforcé ma compréhension des transferts thermiques, le dimensionnement de systèmes énergétiques et les audits énergétiques.")


def display_education():
    st.header("FORMATION ACADEMIQUE")
    st.write('\n')
    st.write('\n')
    st.subheader("Master - Ingénierie des Énergies Renouvelables et Efficacité Énergétique")
    st.write("Octobre 2022 - Présent")
    st.write(
"""
\n
Option: Procédés Thermiques et Valorisation de l'Énergie\n
Faculté Polydisciplinaire - Université Sultan Moulay Slimane - Béni Mellal, Maroc\n
"""
)
    st.write('\n')
    

    st.subheader("Licence Professionnelle - Énergies Renouvelables et Efficacité Énergétique")
    st.write("Octobre 2021 - Juin 2022")
    st.write("ÉCOLE SUPÉRIEURE DE TECHNOLOGIE - Meknès, Maroc")
    st.write('\n')
    st.subheader("Diplôme Universitaire de Technologie - Génie Thermique et Énergie")
    st.write("Septembre 2018 - Juin 2020")
    st.write("ÉCOLE SUPÉRIEURE DE TECHNOLOGIE - Meknès, Maroc")    

def display_work_experience():
    st.header("EXPÉRIENCE PROFESSIONNELLE")
    st.write("\n")
    st.write('\n')
    st.subheader("Stage de Fin d'Études - RANYACHAMS SOLAIRE S.A.R.L - Midelt")
    st.write('\n')
    st.write("Avril 2022 - Juin 2022")
    st.write("\n")
    st.write(
        """
Dimensionnement et Installation des Systèmes Photovoltaïques:\n
• Pompage solaire \n
• Injection au réseau\n
• Sites isolés\n
• Eclairage solaire\n
"""
)
    st.subheader("Stage de Fin d'Année - Agro Juice Processing - VALENCIA, Meknès")
    st.write("Juin 2019 - Aout 2019")
    st.write(
"""

• Maintenance des chaudières et des échangeurs de chaleur \n
• Supervision et régulation des installations de chauffage et de climatisation
"""
)


def display_skills():
    st.header("COMPÉTENCES TECHNIQUES")
    st.write("\n")
    st.write("• Modélisation et dimensionnement des systèmes énergétiques")
    st.write("• Analyse CFD des transferts thermiques")
    st.write("• Diagnostic et bilan thermique des batiments")
    st.write("• Gestion des projets en énergies renouvelables")
    st.write("• Programmation: Python, Java Script, C++")
   

def display_projects():
    st.header("PROJETS ACADEMIQUES")
    st.write("\n")
    st.write("• Etude Analytique et Numérique des Transferts Thermiques dans une Ailette Bi-dimensionnelle")
    st.write("• Analyse CFD de la Convection Forcé sur un Cylindre Verticale")
    st.write("• Dimensionnement d'un Système de Pompage Photovoltaique de Puissance: 12.2 KWc ")
    st.write("• Audit Energétique d'un Batiment Existant à Meknès")
   

def display_softwares():
    st.header("LOGICIELS")
    st.write("\n")
    st.write("• MATLAB")
    st.write("• COMSOL")
    st.write("• ANSYS")
    st.write("• TRNSYS")
    st.write("• SOLIDWORKS")
    st.write("• AUTOCAD")
    st.write("• PVSYST")
    st.write("• RETSCREEN")


def display_languages():
    st.header("Langues")
    st.write("\n")
    st.write("• French: Courant")
    st.write("• English: Courant")
    st.write("• Arabic: Maternelle")        


def display_interests():
    st.header("CENTRES D'INTERET")
    st.write('\n')
    st.write("• Astronomie")
    st.write("• Echecs")
    st.write("• Basketball")    

def main():
    display_bio()
    st.markdown("---")
    display_education()
    st.markdown("---")
    display_work_experience()
    st.markdown("---")
    display_skills()
    st.markdown("---")
    display_projects()
    st.markdown("---")
    display_softwares()
    st.markdown("---")
    display_languages()
    st.markdown("---")
    display_interests()

if __name__ == "__main__":
    main()
