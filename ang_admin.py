# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:54:28 2026
https://github.com/Flopark/ang_admin/blob/f6fcaf1eafdea00b8728e6b7b31dd2d8ffea407d/v.mp4
@author: march
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:54:28 2026

@author: march
"""
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Simulation TikTok - Léo & Florian", layout="wide", initial_sidebar_state="collapsed")

# ==========================================
# VIDÉO DE TEST INFAILLIBLE (Ne la change pas pour le premier test !)
VIDEO_URL = "https://raw.githubusercontent.com/Flopark/ang_admin/main/v.mp4"
# ==========================================

# --- SCÉNARIO DE L'ALGORITHME (Adapté pour votre vidéo de 1 minute) ---
SCENARIO = [
    (2, "Analyse biométrique lancée... Pupil Tracking actif.<br>L'utilisateur est captivé par le début de la vidéo."),
    (12, "Déduction V1 : Profil 'Loup Solitaire'.<br>🎯 Pub : Formation crypto 'Devenez Millionnaire'."),
    (25, "Scroll rapide détecté.<br>Vidéo zappée. Déduction : Intolérance au malaise."),
    (38, "Vidéo 3... Arrêt sur image.<br>Humour noir détecté. Boussole morale en baisse."),
    (55, "🚨 PROFILAGE COMPLET 🚨<br>Valeur marchande : 0.42 centimes. Vente en cours aux annonceurs...")
]

# --- FONCTION HACK TYPEWRITER ---
def render_typewriter(scenario, video_url):
    js_scenario = ""
    for second, text in scenario:
        text_html = text.replace("\n", "<br>").replace("'", "\\'")
        js_scenario += f"    {{ time: {second}, text: '{text_html}' }},\n"

    html_content = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        body {{ background-color: #0e1117; color: #fff; margin: 0; padding: 0; }}
        .main-container {{ display: flex; gap: 20px; align-items: start; max-width: 1200px; margin: 0 auto; }}
        
        .phone-container {{ width: 360px; height: 650px; background: #000; border-radius: 30px; border: 12px solid #333; box-shadow: 0 20px 50px rgba(0,0,0,0.8); position: relative; overflow: hidden; }}
        video {{ width: 100%; height: 100%; object-fit: cover; background-color: #000; }}
        
        .terminal-container {{ flex: 1; height: 630px; background-color: #1e1e1e; border: 2px solid #333; border-radius: 10px; font-family: 'Share Tech Mono', monospace; overflow: hidden; position: relative; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; }}
        .terminal-header {{ position: absolute; top: 0; left: 0; right: 0; height: 30px; background: #333; color: #aaa; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; letter-spacing: 1px; }}
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
            <video id="master-video" playsinline controls>
                <source src="{video_url}" type="video/mp4">
                Votre navigateur ne supporte pas la vidéo.
            </video>
        </div>

        <div class="terminal-container">
            <div class="terminal-header">ALGORITHM LOGS | LÉO & FLORIAN TIKTOK PRESENTATION</div>
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

        function typeWriter(text, element, speed = 15) {{
            isWriting = true;
            let i = 0;
            let textContainer = document.createElement('span');
            element.innerHTML = '<span class="timestamp">[' + formatTime(video.currentTime) + '] ANALYSE_LOGS:</span><br>';
            element.appendChild(textContainer);
            
            let cursor = document.createElement('span');
            cursor.className = 'cursor';
            element.appendChild(cursor);

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

# --- INTERFACE STREAMLIT ---
st.title("📱 TikTok : L'économie de votre attention")
st.markdown("*Simulation de la collecte de données en temps réel.*")
st.markdown("---")

st.components.v1.html(render_typewriter(SCENARIO, VIDEO_URL), height=700)
st.info("💡 **Instructions :** Cliquez sur le bouton 'Play' du téléphone à gauche pour démarrer.")

hide_st_style = """
            <style>
            [data-testid="stHeader"] {display: none;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

