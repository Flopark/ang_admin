# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:54:28 2026

@author: march
"""

import streamlit as st
import base64
import os
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Simulation TikTok - Léo & Florian", layout="wide", initial_sidebar_state="collapsed")

# Nom de votre fichier vidéo unique (à placer dans le même dossier que app.py)
VIDEO_FILE = "1.mp4"

# --- SCÉNARIO DE L'ALGORITHME (À VOUS DE CHANGER LES TIMINGS ET LE TEXTE) ---
# Format : (Seconde précise dans la vidéo, "Trash Talk du terminal")
SCENARIO = [
    # --- Vidéo 1 : L'edit 'Sigma' ---
    (1, "Analyse biométrique lancée... Pupil Tracking actif.<br>L'utilisateur est captivé.<br>Niveau de stress : FAIBLE."),
    (4, "Déduction : Profil 'Loup Solitaire'. Sentiment d'insécurité masculine détecté.<br>🎯 Pub : Formation crypto 'Devenez Millionnaire en 48h'."),
    (6, "Action : L'utilisateur a 'liké' la vidéo.<br>+150 points au profil 'Crédulité'. On verrouille l'attention."),
    
    # --- Vidéo 2 : La Danse (Scroll) ---
    (12, "Scroll détecté.<br>Scan Vidéo 2...<br>Détection de malaise : ÉLEVÉE.<br>Temps de visionnage : 1.2s."),
    (13, "Skip immédiat.<br>Déduction : Intelligence critique présente. Difficile à manipuler.<br>⚠️ Alerte : Injecter 'Shock Value' pour casser les défenses."),
    
    # --- Vidéo 3 : L'IA Epstein (Shock Value) ---
    (18, "Scan Vidéo 3...<br>Sujet sensible. L'utilisateur est figé (3 secondes sans bouger).<br>L'algorithme jubile."),
    (22, "Déduction : Humour noir détecté. Boussole morale défaillante.<br>🎯 Pub : Dropshipping de T-shirts ironiques absurdes."),
    
    # --- Vidéo 4 : La Géopolitique Anime ---
    (28, "Scan Vidéo 4...<br>Contenu anxiogène.<br>Rythme cardiaque déduit (micro-mouvements du cou) : AUGMENTÉ."),
    (32, "Déduction : Éco-anxiété chronique. Romance l'apocalypse.<br>🎯 Pub : Rations de survie luxe (goût bœuf bourguignon) à 150€."),
    
    # --- Conclusion ---
    (40, "🚨 PROFILAGE UTILISATEUR TERMINÉ 🚨<br>Valeur marchande estimée : 0.42 centimes.<br>Prêt pour la vente des données aux annonceurs.")
]

# --- FONCTION HACK TYPEWRITER EFFECT AVEC SYNCHRO VIDÉO ---
def render_typewriter(scenario, video_b64):
    """
    Cette fonction génère tout le HTML et le JavaScript nécessaire pour
    le typewriter effect synchronisé avec le lecteur vidéo HTML5.
    """
    
    # Génération du JS pour chaque entrée du scénario
    js_scenario = ""
    for second, text in scenario:
        # On remplace les sauts de ligne Python par des <br> pour HTML
        text_html = text.replace("\n", "<br>")
        js_scenario += f"    {{ time: {second}, text: '{text_html}' }},\n"

    html_content = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

        /* Style de la page complète (hack pour bypass Streamlit paddings) */
        body {{ background-color: #0e1117; color: #fff; }}
        
        .main-container {{ display: flex; gap: 20px; align-items: start; max-width: 1200px; margin: 0 auto; }}

        /* --- Style du Téléphone (Gauche) --- */
        .phone-container {{ width: 360px; height: 650px; background: #000; border-radius: 30px; border: 12px solid #333; box-shadow: 0 20px 50px rgba(0,0,0,0.8); position: relative; overflow: hidden; }}
        video {{ width: 100%; height: 100%; object-fit: cover; }}

        /* --- Style de la Console Terminal (Droite) --- */
        .terminal-container {{ flex: 1; height: 630px; background-color: #1e1e1e; border: 2px solid #333; border-radius: 10px; font-family: 'Share Tech Mono', monospace; overflow: hidden; position: relative; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; }}
        
        .terminal-header {{ position: absolute; top: 0; left: 0; right: 0; height: 30px; background: #333; color: #aaa; display: flex; align-items: center; justify-content: center; font-size: 12px; }}
        
        .terminal-content {{ margin-top: 30px; flex: 1; overflow-y: auto; display: flex; flex-direction: column-reverse; /* Les nouveaux messages en haut */ }}
        
        .log-entry {{ margin-bottom: 15px; color: #00ff00; line-height: 1.4; border-left: 3px solid transparent; padding-left: 10px; }}
        .log-entry.new {{ border-left-color: red; animation: blink-border 1s steps(2) infinite; }}
        .timestamp {{ color: #888; font-size: 0.8em; margin-right: 10px; }}
        .cursor {{ display: inline-block; width: 8px; height: 15px; background-color: #00ff00; animation: blink 0.7s infinite; vertical-align: middle; }}

        /* --- Animations --- */
        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        @keyframes blink-border {{ 0%, 100% {{ border-left-color: red; }} 50% {{ border-left-color: transparent; }} }}
    </style>

    <div class="main-container">
        <div class="phone-container">
            <video id="master-video" autoplay muted>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
        </div>

        <div class="terminal-container">
            <div class="terminal-header">ALGORITHM LOGS | LEO & FLORIAN TIKTOK presentation</div>
            <div class="terminal-content" id="terminal-content">
                <div id="typewriter-area"><span class="cursor"></span></div>
            </div>
        </div>
    </div>

    <script>
        const video = document.getElementById('master-video');
        const typewriterArea = document.getElementById('typewriter-area');
        const terminalContent = document.getElementById('terminal-content');
        
        // Le scénario précis fourni par Léo & Florian
        const scenario = [
            {js_scenario}
        ];

        let currentIndex = 0;
        let isWriting = false;

        // --- FONCTION TYPEWRITER EFFECT ---
        function typeWriter(text, element, speed = 40) {{
            isWriting = true;
            let i = 0;
            element.innerHTML = '<span class="timestamp">[' + formatTime(video.currentTime) + '] ANALYSE_LOGS:</span>';
            
            function write() {{
                if (i < text.length) {{
                    if (text.substring(i, i+4) === '<br>') {{
                        element.innerHTML += '<br>';
                        i += 4;
                    }} else {{
                        element.innerHTML += text.charAt(i);
                        i++;
                    }}
                    setTimeout(write, speed);
                    terminalContent.scrollTop = 0; // Garder le scroll en bas (reverse order)
                }} else {{
                    element.innerHTML += '<span class="cursor"></span>'; // Ajouter le curseur clignotant
                    isWriting = false;
                }}
            }}
            write();
        }}

        // --- CHECK SYNCHRO VIDÉO ---
        // Se lance toutes les 250ms pour vérifier si c'est le moment d'écrire
        video.ontimeupdate = function() {{
            const currentTime = video.currentTime;
            
            if (currentIndex < scenario.length && !isWriting) {{
                if (currentTime >= scenario[currentIndex].time) {{
                    // Créer une nouvelle entrée dans le terminal
                    const newLog = document.createElement('div');
                    newLog.className = 'log-entry new';
                    
                    // Retirer la classe 'new' (bordure rouge) de l'ancien log
                    const oldLogs = typewriterArea.querySelectorAll('.log-entry');
                    if (oldLogs.length > 0) {{
                        oldLogs[0].classList.remove('new');
                    }}
                    
                    typewriterArea.prepend(newLog); // Insérer le nouveau log en haut (car flex-direction reverse)
                    
                    // Lancer l'effet machine à écrire
                    typeWriter(scenario[currentIndex].text, newLog);
                    
                    currentIndex++;
                }}
            }}
        }};

        // Utilitaire formatage temps
        function formatTime(seconds) {{
            let min = Math.floor(seconds / 60);
            let sec = Math.floor(seconds % 60);
            min = (min < 10) ? '0' + min : min;
            sec = (sec < 10) ? '0' + sec : sec;
            return min + ':' + sec;
        }}
    </script>
    """
    return html_content

# --- CORPS PRINCIPAL DE L'APPLICATION ---
st.title("📱 TikTok : L'économie de votre attention")
st.markdown("*Simulation de la collecte de données en temps réel.*")
st.markdown("---")

# 1. Chargement de la vidéo et encodage Base64
if os.path.exists(VIDEO_FILE):
    with open(VIDEO_FILE, "rb") as f:
        video_bytes = f.read()
    video_b64 = base64.b64encode(video_bytes).decode()
    
    # 2. Injection du HTML/JS
    # On utilise st.components.v1.html pour contrôler parfaitement le timing
    # sans interaction de Streamlit qui créerait de la latence.
    st.components.v1.html(render_typewriter(SCENARIO, video_b64), height=700)
    
    st.info("💡 CONSEIL : Si la vidéo ne démarre pas, rafraîchissez la page. L'algorithme se synchronise au lancement.")

else:
    st.error(f"Fichier vidéo '{VIDEO_FILE}' introuvable. Veuillez placer votre vidéo .mp4 dans le dossier de l'application.")

# Cacher le menu et le footer Streamlit
hide_st_style = """
            <style>
            [data-testid="stHeader"] {display: none;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

