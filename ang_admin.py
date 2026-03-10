# -*- coding: utf-8 -*-
import streamlit as st
import base64
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Simulation TikTok - Léo & Florian", layout="wide", initial_sidebar_state="collapsed")

# Nom de votre fichier vidéo unique
VIDEO_FILE = "1.mp4"

# --- SCÉNARIO DE L'ALGORITHME ---
# --- ALGORITHM SCENARIO (9 Logs - Ultimate Dark Roast Edition) ---
# Format : (Seconde précise, "Texte du log en anglais")
SCENARIO = [
    (4, "Analyse_Logs: User liked 'Sigma Male' content.<br>Scan: Delusional main-character syndrome detected. Severe lack of female contact confirmed.<br>🎯 Target: Overpriced crypto courses and 'Alpha' podcasts."),
    
    (10, "Analyse_Logs: Cringe tolerance tested (Awkward dance transition).<br>Scan: User watched without flinching. Brain activity flatlining. Intelligence quotient dropping.<br>🎯 Target: Mind-numbing mobile game ads."),
    
    (18, "Analyse_Logs: WW3 Anime intro engaged. User liked the geopolitical disaster.<br>Scan: Eco-anxiety high, empathy zero. Romanticizes global conflict.<br>🎯 Target: Doomsday survival kits and tactical flashlights."),
    
    (24, "Analyse_Logs: Thirst trap detected. Pupil dilation confirmed.<br>Scan: Profound superficiality and crippling self-esteem issues. User is easily manipulated by visual stimuli.<br>🎯 Target: Hair loss treatments and fake luxury watches."),
    
    (31, "Analyse_Logs: Deepfake of convicted criminal singing. User liked the video.<br>Scan: Extreme dark humor processed. Moral compass: Non-existent. Psychopathy markers +45%.<br>🎯 Target: Obscure conspiracy documentaries."),
    
    (37, "Analyse_Logs: 'Minecraft IRL' watched.<br>Scan: Arrested development confirmed. User is legally an adult but mentally 12. Lives with parents.<br>🎯 Target: Toxic energy drinks and cheap LED room lights."),
    
    (43, "Analyse_Logs: Real-world explosion footage. User liked it.<br>Scan: Morbid dopamine spike registered. Consumes tragedy for entertainment. Emotionally dead.<br>🎯 Target: Antidepressants and fast food delivery."),
    
    (50, "Analyse_Logs: Raging man in car. Heart rate synchronized.<br>Scan: User resonates with pure, toxic anger. Deep frustration with own miserable life detected.<br>🎯 Target: Anger management apps and dashcams."),
    
    (64, "🚨 PROFILING COMPLETE: SOUL HARVESTED 🚨<br>Summary: Isolated, doomscrolling, emotionally stunted man-child.<br>Estimated Market Value: $0.003.<br>Action: Packaging mental illness data. Selling to the highest bidder...")
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
        video {{ width: 100%; height: 100%; object-fit: cover; }}
        
        .terminal-container {{ flex: 1; height: 630px; background-color: #1e1e1e; border: 2px solid #333; border-radius: 10px; font-family: 'Share Tech Mono', monospace; overflow: hidden; position: relative; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; }}
        .terminal-header {{ position: absolute; top: 0; left: 0; right: 0; height: 30px; background: #333; color: #aaa; display: flex; align-items: center; justify-content: center; font-size: 12px; }}
        .terminal-content {{ margin-top: 30px; flex: 1; overflow-y: auto; display: flex; flex-direction: column-reverse; }}
        
        .log-entry {{ margin-bottom: 15px; color: #00ff00; line-height: 1.4; border-left: 3px solid transparent; padding-left: 10px; }}
        .log-entry.new {{ border-left-color: red; animation: blink-border 1s steps(2) infinite; }}
        .timestamp {{ color: #888; font-size: 0.8em; margin-right: 10px; }}
        .cursor {{ display: inline-block; width: 8px; height: 15px; background-color: #00ff00; animation: blink 0.7s infinite; vertical-align: middle; }}

        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        @keyframes blink-border {{ 0%, 100% {{ border-left-color: red; }} 50% {{ border-left-color: transparent; }} }}
    </style>

    <div class="main-container">
        <div class="phone-container">
            <video id="master-video" autoplay muted playsinline controls>
                <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            </video>
        </div>

        <div class="terminal-container">
            <div class="terminal-header">ALGORITHM LOGS | LEO & FLORIAN TIKTOK presentation</div>
            <div class="terminal-content" id="terminal-content">
                <div id="typewriter-area"></div>
            </div>
        </div>
    </div>

    <script>
        const video = document.getElementById('master-video');
        const typewriterArea = document.getElementById('typewriter-area');
        const terminalContent = document.getElementById('terminal-content');
        
        const scenario = [
            {js_scenario}
        ];

        let currentIndex = 0;
        let isWriting = false;

        function typeWriter(text, element, speed = 12) {{
            isWriting = true;
            let i = 0;
            // On prépare le conteneur du texte pour pouvoir le remplir lettre par lettre
            let textContainer = document.createElement('span');
            element.innerHTML = '<span class="timestamp">[' + formatTime(video.currentTime) + '] ANALYSE_LOGS:</span><br>';
            element.appendChild(textContainer);
            
            // Le curseur qui clignote
            let cursor = document.createElement('span');
            cursor.className = 'cursor';
            element.appendChild(cursor);

            // Pour gérer l'insertion de balises HTML comme <br>
            let tempHTML = "";

            function write() {{
                if (i < text.length) {{
                    if (text.substring(i, i+4) === '<br>') {{
                        tempHTML += '<br>';
                        i += 4;
                    }} else {{
                        tempHTML += text.charAt(i);
                        i++;
                    }}
                    textContainer.innerHTML = tempHTML;
                    terminalContent.scrollTop = 0;
                    setTimeout(write, speed);
                }} else {{
                    isWriting = false;
                }}
            }}
            write();
        }}

        video.ontimeupdate = function() {{
            const currentTime = video.currentTime;
            
            if (currentIndex < scenario.length && !isWriting) {{
                if (currentTime >= scenario[currentIndex].time) {{
                    const newLog = document.createElement('div');
                    newLog.className = 'log-entry new';
                    
                    const oldLogs = typewriterArea.querySelectorAll('.log-entry');
                    if (oldLogs.length > 0) {{
                        oldLogs[0].classList.remove('new');
                    }}
                    
                    typewriterArea.prepend(newLog);
                    typeWriter(scenario[currentIndex].text, newLog);
                    currentIndex++;
                }}
            }}
        }};

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

# --- CORPS PRINCIPAL ---
st.title("📱 TikTok : L'économie de votre attention")
st.markdown("*Simulation de la collecte de données en temps réel.*")
st.markdown("---")

if os.path.exists(VIDEO_FILE):
    with open(VIDEO_FILE, "rb") as f:
        video_bytes = f.read()
    video_b64 = base64.b64encode(video_bytes).decode()
    
    st.components.v1.html(render_typewriter(SCENARIO, video_b64), height=700)
    
    # Message d'aide si la vidéo ne démarre pas
    st.warning("⚠️ Si la vidéo ne se lance pas toute seule, cliquez sur le bouton 'Play' directement sur le téléphone à gauche !")
else:
    st.error(f"Fichier vidéo '{VIDEO_FILE}' introuvable. Placez la vidéo dans le même dossier que ce code.")

hide_st_style = """
            <style>
            [data-testid="stHeader"] {display: none;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


