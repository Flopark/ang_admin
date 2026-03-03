# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:54:28 2026

@author: march
"""
import streamlit as st
import base64
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Simulation TikTok - Léo & Florian", layout="wide", initial_sidebar_state="collapsed")

# Nom de votre fichier vidéo unique
VIDEO_FILE = "1.mp4"

# --- SCÉNARIO DE L'ALGORITHME ---
SCENARIO = [
    (1, "Analyse biométrique lancée... Pupil Tracking actif.<br>L'utilisateur est captivé.<br>Niveau de stress : FAIBLE."),
    (4, "Déduction : Profil 'Loup Solitaire'. Sentiment d'insécurité masculine détecté.<br>🎯 Pub : Formation crypto 'Devenez Millionnaire en 48h'."),
    (6, "Action : L'utilisateur a 'liké' la vidéo.<br>+150 points au profil 'Crédulité'. On verrouille l'attention."),
    (12, "Scroll détecté.<br>Scan Vidéo 2...<br>Détection de malaise : ÉLEVÉE.<br>Temps de visionnage : 1.2s."),
    (13, "Skip immédiat.<br>Déduction : Intelligence critique présente. Difficile à manipuler.<br>⚠️ Alerte : Injecter 'Shock Value' pour casser les défenses."),
    (18, "Scan Vidéo 3...<br>Sujet sensible. L'utilisateur est figé (3 secondes sans bouger).<br>L'algorithme jubile."),
    (22, "Déduction : Humour noir détecté. Boussole morale défaillante.<br>🎯 Pub : Dropshipping de T-shirts ironiques absurdes."),
    (28, "Scan Vidéo 4...<br>Contenu anxiogène.<br>Rythme cardiaque déduit (micro-mouvements du cou) : AUGMENTÉ."),
    (32, "Déduction : Éco-anxiété chronique. Romance l'apocalypse.<br>🎯 Pub : Rations de survie luxe (goût bœuf bourguignon) à 150€."),
    (40, "🚨 PROFILAGE UTILISATEUR TERMINÉ 🚨<br>Valeur marchande estimée : 0.42 centimes.<br>Prêt pour la vente des données aux annonceurs.")
]

# --- FONCTION HACK TYPEWRITER ---
def render_typewriter(scenario, video_b64):
    js_scenario = ""
    for second, text in scenario:
        # CORRECTION DU BUG : On remplace les apostrophes par des \' pour que le JavaScript ne crashe pas !
        text_html = text.replace("\n", "<br>").replace("'", "\\'")
        js_scenario += f"    {{ time: {second}, text: '{text_html}' }},\n"

    html_content = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        body {{ background-color: #0e1117; color: #fff; margin: 0; padding: 0; }}
        .main-container {{ display: flex; gap: 20px; align-items: start; max-width: 1200px; margin: 0 auto; }}
        
        .phone-container {{ width: 360px; height: 650px; background: #000; border-radius: 30px; border: 12px solid #333; box-shadow: 0 20px 50px rgba(0,0,0,0.8); position: relative; overflow: hidden; }}
        /* CORRECTION : Ajustement de la vidéo pour voir les contrôles */
        video {{ width: 100%; height:


