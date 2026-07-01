from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="MoodBot", page_icon="🎭", layout="centered")

# ── Mood definitions ───────────────────────────────────────────────────────────
MODES = {
    "Angry": {
        "system":  "You are an angry ai agent",
        "emoji":   "😡",
        "accent":  "#e63946",
        "glow":    "rgba(230,57,70,0.35)",
        "bg":      "#110404",
        "bubble_bot": "#1e0808",
        "bubble_border": "#3a1010",
        "tag":     "RAGE MODE",
    },
    "Funny": {
        "system":  "You are a funny ai agent",
        "emoji":   "😂",
        "accent":  "#f4a522",
        "glow":    "rgba(244,165,34,0.35)",
        "bg":      "#110e04",
        "bubble_bot": "#1e1808",
        "bubble_border": "#3a2e10",
        "tag":     "COMEDY MODE",
    },
    "Sad": {
        "system":  "You are a sad ai agent",
        "emoji":   "😢",
        "accent":  "#4ea8de",
        "glow":    "rgba(78,168,222,0.35)",
        "bg":      "#04080f",
        "bubble_bot": "#080f1a",
        "bubble_border": "#101e30",
        "tag":     "MELANCHOLY MODE",
    },
}

# ── Session state ──────────────────────────────────────────────────────────────
if "mode" not in st.session_state:
    st.session_state.mode = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Model ──────────────────────────────────────────────────────────────────────
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2506", temperature=0.9)

model = get_model()

# ── Dynamic CSS ────────────────────────────────────────────────────────────────
def inject_css(mode_key=None):
    m = MODES[mode_key] if mode_key else {
        "accent": "#555", "glow": "rgba(100,100,100,0.15)",
        "bg": "#0a0a0a", "bubble_bot": "#141414",
        "bubble_border": "#222",
    }
    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

:root {{
    --accent:  {m['accent']};
    --glow:    {m['glow']};
    --bg:      {m['bg']};
    --bot-bg:  {m['bubble_bot']};
    --bot-bdr: {m['bubble_border']};
}}

html, body, [class*="css"] {{
    background-color: var(--bg) !important;
    color: #e8e8e8;
    font-family: 'DM Sans', sans-serif;
}}
#MainMenu, footer, header {{ visibility: hidden; }}
.block-container {{ max-width: 760px; padding: 1.5rem 1.5rem 7rem; }}

/* Top bar */
.topbar-title {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    letter-spacing: 3px;
    color: var(--accent);
    text-shadow: 0 0 28px var(--glow);
    line-height: 1;
}}
.topbar-tag {{
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 3px;
    color: var(--accent);
    border: 1px solid var(--accent);
    padding: 3px 10px;
    border-radius: 3px;
    opacity: 0.75;
    display: inline-block;
}}

/* Bubbles */
.msg-row {{
    display: flex;
    align-items: flex-end;
    gap: 0.5rem;
    margin-bottom: 1rem;
    animation: fadeUp 0.28s ease both;
}}
@keyframes fadeUp {{
    from {{ opacity:0; transform: translateY(6px); }}
    to   {{ opacity:1; transform: translateY(0); }}
}}
.msg-row.user {{ flex-direction: row-reverse; }}
.avatar {{
    width: 34px; height: 34px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
    background: #111; border: 1.5px solid #1e1e1e;
}}
.avatar.user {{ border-color: var(--accent); }}
.bubble {{
    max-width: 70%; padding: 0.8rem 1.1rem;
    font-size: 0.875rem; line-height: 1.65; border-radius: 16px;
}}
.bubble.bot {{
    background: var(--bot-bg); border: 1px solid var(--bot-bdr);
    border-bottom-left-radius: 4px; color: #d8d8d8;
}}
.bubble.user {{
    background: var(--accent); border-bottom-right-radius: 4px;
    color: #000; font-weight: 500; text-align: right;
}}

/* Empty */
.empty-state {{
    text-align: center; padding: 3.5rem 0; color: #222;
    font-family: 'DM Mono', monospace; font-size: 0.72rem;
    letter-spacing: 2px; text-transform: uppercase;
}}

/* Chat scroll */
.chat-area {{ max-height: 58vh; overflow-y: auto; padding-right: 4px; }}
.chat-area::-webkit-scrollbar {{ width: 3px; }}
.chat-area::-webkit-scrollbar-track {{ background: transparent; }}
.chat-area::-webkit-scrollbar-thumb {{ background: #1e1e1e; border-radius: 3px; }}

/* Input */
.stChatInputContainer, [data-testid="stChatInput"] {{
    background: #0f0f0f !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 12px !important;
}}
.stChatInputContainer textarea {{
    color: #e8e8e8 !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.85rem !important;
}}
.stChatInputContainer button svg {{ stroke: var(--accent) !important; }}

/* Streamlit buttons */
div[data-testid="stButton"] button {{
    font-family: 'Bebas Neue', sans-serif !important;
    letter-spacing: 2px; font-size: 1rem !important;
    border-radius: 10px; border: 1.5px solid #222;
    background: transparent; color: #555;
    transition: all 0.2s; width: 100%; padding: 0.6rem !important;
}}
div[data-testid="stButton"] button:hover {{
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    box-shadow: 0 0 18px var(--glow);
    background: transparent !important;
}}

/* Divider */
.divider {{ border-bottom: 1px solid #181818; margin-bottom: 1.5rem; }}

/* Spinner */
.stSpinner > div {{ border-top-color: var(--accent) !important; }}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  MODE SELECTION SCREEN
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.mode is None:
    inject_css(None)

    st.markdown("""
<div style="text-align:center; padding: 2.5rem 0 0.5rem;">
    <div style="font-family:'Bebas Neue',sans-serif; font-size:4rem;
                letter-spacing:6px; color:#e0e0e0; line-height:1;">
        MOOD<span style="color:#444;">BOT</span>
    </div>
    <div style="font-family:'DM Mono',monospace; font-size:0.68rem;
                letter-spacing:3px; color:#2e2e2e; text-transform:uppercase;
                margin-top:0.5rem;">
        Choose your AI personality
    </div>
</div>
<br>
""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    picks = [("Angry","😡"), ("Funny","😂"), ("Sad","😢")]
    for col, (name, emoji) in zip([col1, col2, col3], picks):
        with col:
            st.markdown(f"<div style='text-align:center;font-size:2.8rem;margin-bottom:0.4rem'>{emoji}</div>",
                        unsafe_allow_html=True)
            if st.button(f"{name.upper()} MODE", key=f"btn_{name}"):
                st.session_state.mode = name
                st.session_state.messages = [SystemMessage(content=MODES[name]["system"])]
                st.rerun()

    st.markdown("""
<div style="text-align:center; margin-top:3.5rem; color:#191919;
            font-family:'DM Mono',monospace; font-size:0.62rem; letter-spacing:2px;">
    MISTRAL-SMALL-2506 · LANGCHAIN
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  CHAT SCREEN
# ══════════════════════════════════════════════════════════════════════════════
else:
    mode_key = st.session_state.mode
    m = MODES[mode_key]
    inject_css(mode_key)

    # ── Header row ──
    c1, c2, c3 = st.columns([3, 2, 1])
    with c1:
        st.markdown(f"<div class='topbar-title'>{m['emoji']} MOODBOT</div>", unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"<div style='display:flex;align-items:center;height:100%;'>"
            f"<span class='topbar-tag'>{m['tag']}</span></div>",
            unsafe_allow_html=True)
    with c3:
        if st.button("↩ BACK"):
            st.session_state.mode = None
            st.session_state.messages = []
            st.rerun()

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # ── Messages ──
    visible = [msg for msg in st.session_state.messages if not isinstance(msg, SystemMessage)]

    html = '<div class="chat-area">'
    if not visible:
        html += f'<div class="empty-state">{m["emoji"]} &nbsp; Say something…</div>'
    else:
        for msg in visible:
            if isinstance(msg, HumanMessage):
                html += (f'<div class="msg-row user">'
                         f'<div class="avatar user">🧑</div>'
                         f'<div class="bubble user">{msg.content}</div></div>')
            elif isinstance(msg, AIMessage):
                safe = msg.content.replace("<","&lt;").replace(">","&gt;")
                html += (f'<div class="msg-row bot">'
                         f'<div class="avatar bot">{m["emoji"]}</div>'
                         f'<div class="bubble bot">{safe}</div></div>')
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

    # ── Input ──
    user_input = st.chat_input(f"Talk to your {mode_key.lower()} bot…")
    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner(""):
            response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        st.rerun()