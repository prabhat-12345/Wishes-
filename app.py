import streamlit as st
import os
import time

# 1. पेज की पूरी सेटिंग (No Scroll)
st.set_page_config(page_title="Happy Birthday My Love!", page_icon="❤️", layout="wide")

# 2. कस्टमाइज CSS (ओरिजिनल स्टाइल के साथ प्रीमियम पन्ने)
custom_css = """
<style>
    /* ऐप का शानदार डार्क रोमांटिक बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #0f0003 0%, #2a0a07 50%, #4d0011 100%);
        color: #ffffff;
    }
    
    /* मुख्य कंटेनर मोबाइल स्क्रीन के लिए */
    .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 450px !important;
    }
    
    /* मुख्य बनावट सेटिंग */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.4rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 0px;
        margin-bottom: 10px;
        background: linear-gradient(to right, #ff0055, #ffd700, #ff00ab);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite;
    }
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    /* सबसे ऊपर दिखने वाला प्रभात का संदेश */
    .love-sender-box {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 12px;
        line-height: 1.4;
    }
    
    .love-name {
        font-family: 'Georgia', serif;
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #ffd700, #ff00b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(255, 128, 179, 0.6);
        display: inline-block;
    }
    
    .love-receiver-name {
        font-family: 'Georgia', serif;
        font-size: 2.2rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #ff0055, #ff00b3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px #ff0055, 0px 0px 10px #ff00b3;
        display: inline-block;
    }
    
    /* फोटो के ऊपर और नीचे चमकने वाले शानदार रोमांटिक इंग्लिश टैग */
    .romantic-badge {
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin: 10px auto;
        padding: 5px 15px;
        border-radius: 50px;
        background: rgba(255, 0, 85, 0.1);
        border: 1px solid rgba(255, 0, 85, 0.3);
        width: fit-content;
    }
    
    .badge-left { color: #ff0055; text-shadow: 0 0 8px #ff0055; }
    .badge-right { color: #ffd700; text-shadow: 0 0 8px #ffd700; }
    
    /* इमेज का सेटिंग */
    .stImage {
        position: relative;
    }
    
    .stImage img {
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 85, 0.5) !important;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.7) !important;
    }

    /* विश कंटेनर और टेक्स्ट की स्टाइलिंग */
    .wishes-container {
        margin-top: 20px;
        padding: 10px;
    }

    .wish-text {
        font-family: 'Georgia', serif;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(255, 0, 85, 0.1);
        padding-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #ff80b3, #ffccff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 6s linear infinite;
    }

    .wish-text:last-child {
        border-bottom: none;
        margin-bottom: 0;
    }

    .wish-highlight {
        font-weight: bold;
        background: linear-gradient(to right, #ff0077, #ffa500, #ff0077);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 3s linear infinite;
    }

    /* डायरी के पन्नों (Tabs) की कस्टमाइज स्टाइल */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 51, 119, 0.1) !important;
        border: 1px solid rgba(255, 51, 119, 0.3) !important;
        border-radius: 15px !important;
        padding: 6px 12px !important;
        color: #ffb3cc !important;
        font-weight: bold !important;
        font-size: 0.9rem !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(45deg, #ff0055, #ff3377) !important;
        color: white !important;
        border: 1px solid #ffd700 !important;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.5) !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. सीक्रेट पासवर्ड लॉक स्क्रीन
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align:center; font-family:Georgia; color:#ff0055; margin-top:50px;'>🔒 Our Private Space</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ffb3cc;'>यह डायरी सिर्फ तुम्हारे और मेरे लिए लॉक्ड है।</p>", unsafe_allow_html=True)
    
    password = st.text_input("सीक्रेट कोड (Password) दर्ज करें:", type="password")
    if st.button("डायरी खोलें 📖"):
        if password == "1122":  
            st.session_state.authenticated = True
            st.success("अनलॉक हो रहा है... ❤️")
            time.sleep(1)
            st.rerun()
        else:
            st.error("गलत पासवर्ड! सिर्फ मेरी जान को असली कोड पता है। 😉")
    st.stop()

# --- अनलॉक होने के बाद का मुख्य ऐप ---

# बैकग्राउंड म्यूजिक चेंजिंग लॉजिक
if 'active_track' not in st.session_state:
    st.session_state.active_track = "https://chosic.com"

audio_html = f"""
<audio id="birthday-song" loop src="{st.session_state.active_track}"></audio>
<script>
    function playAudio() {{
        var audio = document.getElementById('birthday-song');
        if (audio && audio.paused) {{
            audio.play().catch(e => console.log("Interaction needed"));
        }}
    }}
    document.addEventListener('click', playAudio, {{ once: true }});
    document.addEventListener('touchstart', playAudio, {{ once: true }});
    var audio = document.getElementById('birthday-song');
    if(audio) {{ audio.play(); }}
</script>
"""
st.markdown(audio_html, unsafe_allow_html=True)

# ऑटोमैटिक फोटो ढूंढने का सिस्टम (बिना नाम बदले काम करेगा)
all_files = os.listdir(".")
all_images = [f for f in all_files if f.lower().endswith((".jpeg", ".jpg", ".png", ".webp"))]

# मुख्य पन्ने के लिए पहली फोटो चुनी जाएगी
main_photo = all_images[0] if len(all_images) > 0 else None

# अगर गिटहब में ज्यादा फोटो होंगी तो वो एल्बम में स्लाइडर बन जाएंगी
album_photos = all_images if len(all_images) > 0 else [
    "https://unsplash.com",
    "https://unsplash.com"
]

# 4. डायरी के अलग-अलग पन्ने (Tabs System)
panna1, panna2, panna3 = st.tabs(["🏠 मुख्य पन्ना", "🎵 म्यूजिक रूम", "📸 फोटो एल्बम"])

# ----------------- पन्ना 1: होम और ओरिजिनल कोट्स -----------------
with panna1:
    # प्रभात और लक्ष्मी का हेडर
    st.markdown('<div class="love-sender-box"><span class="love-name">🎉 PRABHAT 🎉</span><br><span style="color:#ffb3cc; font-size:0.9rem; font-weight:bold;">Wishes Happy Birthday To His Lifeline</span><br><span class="love-receiver-name">💖 LAXMI 💖</span></div>', unsafe_allow_html=True)

    # मुख्य टाइटल
    st.markdown('<h1 class="main-title">Happy Birthday<br>My Love 🎂</h1>', unsafe_allow_html=True)

    # पहला बैच
    st.markdown('<div class="romantic-badge badge-left">❤️ YOU ARE MY LIFE 🌹</div>', unsafe_allow_html=True)

    # इमेज और गोल चक्र वाला साइड टेक्स्ट
    col1, col2 = st.columns(2)

    with col1:
        if main_photo:
            st.image(main_photo, use_container_width=True)
        else:
            st.image("https://unsplash.com", use_container_width=True)

    with col2:
        circle_html = """
        <div style="
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            border: 2px solid #ff0055; 
            border-radius: 50%; 
            width: 140px; 
            height: 140px; 
            margin: 30px auto 0 auto; 
            background: rgba(255,0,85,0.1);
            box-shadow: 0 0 20px #ff0055;
            font-family: 'Georgia', serif;
            font-size: 0.8rem;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            line-height: 1.4;
            transform: rotate(-15deg);
        ">
            11 💖 YRS<br>OF 🌹 LOVE<br>MY 💍 WIFE<br>MY BABU<br>MY 💞 JAAN<br>MY 🚼 LIFE
        </div>
        """
        st.markdown(circle_html, unsafe_allow_html=True)

    # नीचे का दूसरा बैच
    st.markdown('<div class="romantic-badge badge-right">💝 YOU ARE MY EVERYTHING 🧸</div>', unsafe_allow_html=True)

    # सारे लव और रोमांटिक कोट्स
    quotes_html = """
    <div class="wishes-container">
        <p class="wish-text"><span class="wish-highlight">✨ 1. 11 Years of Togetherness:</span> हमारा यह 11 साल का सफर सिर्फ एक रिश्ता नहीं, मेरी पूरी जिंदगी की सबसे खूबसूरत सच्चाई है। 🌹</p>
        <p class="wish-text"><span class="wish-highlight">❤️ 2. Forever Mine:</span> चेहरे पर आपके रहे हमेशा नूर, खुदा कभी न करे हमसे आपको दूर... Happy Birthday Jaan! 🧎</p>
        <p class="wish-text"><span class="wish-highlight">💘 3. To My Soulmate:</span> "You are the beat of my heart, the smile on my face, and the spark in my life. I love you endlessly." 🏹</p>
