import streamlit as st
import time
import random
from datetime import datetime

# ==========================================================
# 1. PESAN HARIAN DARI KAMU UNTUK EGA
# ==========================================================
DAILY_MESSAGES = [
    "Radio check, Ega. Seperti kata Toto ke Kimi Antonelli: 'Focus on your line, the speed is already there.' Apapun rintangan hari ini, kamu punya talenta dan determinasi buat ngelewatinnya! #Cakep #Asik",
    "Box, box, box! Kalau hari ini ban dan mesin kamu rasanya panas, masuk pit lane sebentar. Dinginkan kepala, ganti kompon baru. Besok kita push lagi dari flying lap!",
    "It's Antonelli pace time! Berani ambil racing line sendiri walau kelihatannya sempit dan berliku. Masalah hari ini cuma apex tajam yang bakal bikin instingmu makin tajam.",
    "Data telemetri hari ini menunjukkan progres yang luar biasa, Ga. Gap waktu makin mengecil. Terus konsisten dan jangan terlalu keras sama diri sendiri.",
    "Breathe, Ega. Mobil secepat Silver Arrows pun butuh kontrol setir yang tenang. Kamu hebat sudah menyelesaikan tugas dan cerita hari ini.",
    "Yellow flag di lintasan hari ini bukan berarti gagal. Kadang kita harus melambat sebentar biar terhindar dari benturan. Besok saat green flag berkibar, langsung tancap gas!",
    "P1 on the debrief! Apapun yang terjadi hari ini, kamu tetap pembalap andalan di hati kakak. Istirahat yang cukup, champion!"
]

def get_todays_message():
    day_idx = datetime.now().timetuple().tm_yday % len(DAILY_MESSAGES)
    return DAILY_MESSAGES[day_idx]

# ==========================================================
# 2. SETUP & STYLING COMPACT MERCEDES F1
# ==========================================================
st.set_page_config(
    page_title="Mercedes-AMG F1 | Antonelli #12 Ega Paddock",
    page_icon="🏎️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap');

    .stApp {
        background-color: #080a0d;
        background-image: radial-gradient(#151b22 1px, transparent 1px);
        background-size: 18px 18px;
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4 {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 1px;
    }

    .telemetry-code {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        color: #00A19B;
    }

    .pitwall-header {
        border-left: 4px solid #00A19B;
        background: linear-gradient(90deg, rgba(0, 161, 155, 0.12) 0%, transparent 100%);
        padding: 10px 16px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 18px;
    }

    .f1-panel {
        background: #0f1318;
        border: 1px solid #1e2732;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }

    .radio-card {
        background: linear-gradient(135deg, #0e171a 0%, #0a0f13 100%);
        border: 1.5px solid #00A19B;
        border-radius: 10px;
        padding: 18px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 161, 155, 0.25);
    }

    /* COMPACT BUTTONS */
    .stButton > button {
        background: #11161d;
        color: #00A19B !important;
        border: 1px solid #00A19B !important;
        border-radius: 6px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 600;
        font-size: 11px !important;
        letter-spacing: 0.5px;
        padding: 6px 14px !important;
        min-height: 36px !important;
        height: auto !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #00A19B !important;
        color: #080a0d !important;
        box-shadow: 0 0 12px rgba(0, 161, 155, 0.5);
    }

    .stButton > button[kind="primary"] {
        background: #00A19B !important;
        color: #080a0d !important;
        border: none !important;
    }

    /* Compact Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #090c10 !important;
        border: 1px solid #24303e !important;
        color: #f8fafc !important;
        border-radius: 6px;
        font-size: 13px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 3. STATE MANAGEMENT
# ==========================================================
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "sub_mode" not in st.session_state:
    st.session_state.sub_mode = "story"
if "story_submitted" not in st.session_state:
    st.session_state.story_submitted = False
if "todo_submitted" not in st.session_state:
    st.session_state.todo_submitted = False
if "todos" not in st.session_state:
    st.session_state.todos = [
        {"task": "Morning Telemetry & Hydration Check", "done": True},
        {"task": "Apex Speed Focus Session", "done": False}
    ]
if "reaction_state" not in st.session_state:
    st.session_state.reaction_state = "idle"
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "reaction_result" not in st.session_state:
    st.session_state.reaction_result = None

# ==========================================================
# 4. HALAMAN 1: COCKPIT MAIN MENU
# ==========================================================
if st.session_state.current_page == "home":
    st.markdown("""
    <div class="pitwall-header">
        <div class="telemetry-code">MERCEDES-AMG PETRONAS FORMULA ONE TEAM // CAR #12</div>
        <h2 style="margin: 4px 0 0 0; font-size: 22px;">KIMI ANTONELLI'S COCKPIT</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="f1-panel">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-family: 'Orbitron'; font-weight: 800; color: #00A19B; font-size: 18px;">#12</span>
            <span class="telemetry-code">RADIO CHECK ACTIVE</span>
        </div>
        <p style="color: #cbd5e1; font-size: 13.5px; line-height: 1.6; margin: 0;">
            Radio check, di sini kamu pegang kendali atas jadwal harianmu untuk menuliskan ceritamu langsung. 
            Pilih instrumen yang ingin kamu jalankan hari ini:
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📝 STINT LOG", use_container_width=True):
            st.session_state.current_page = "log"
            st.session_state.sub_mode = "story"
            st.session_state.story_submitted = False
            st.rerun()
    with c2:
        if st.button("🎯 TO-DO STRATEGY", use_container_width=True):
            st.session_state.current_page = "log"
            st.session_state.sub_mode = "todo"
            st.session_state.todo_submitted = False
            st.rerun()
    with c3:
        if st.button("🚦 REACTION TEST", use_container_width=True):
            st.session_state.current_page = "game"
            st.rerun()

# ==========================================================
# 5. HALAMAN 2: LOG HARIAN & MULTI TO-DO LIST
# ==========================================================
elif st.session_state.current_page == "log":
    st.markdown("""
    <div class="pitwall-header">
        <div class="telemetry-code">STAGE 02 // TELEMETRY & STRATEGY</div>
        <h2 style="margin: 4px 0 0 0; font-size: 20px;">DEBRIEF ROOM</h2>
    </div>
    """, unsafe_allow_html=True)

    # SUB-MODE A: CERITA
    if st.session_state.sub_mode == "story":
        st.markdown("""
        <div class="f1-panel">
            <h4 style="color: #00A19B; margin: 0 0 6px 0; font-size: 14px;">🎙️ Driver Stint Debrief</h4>
            <p style="color: #94a3b8; font-size: 12px; margin: 0;">
                Tuliskan apa saja yang kamu lalui hari ini. Tulisan ini tersimpan secara lokal dan aman.
            </p>
        </div>
        """, unsafe_allow_html=True)

        log_title = st.text_input("Topik Stint Hari Ini:", placeholder="Contoh: Tikungan berat hari ini...")
        log_content = st.text_area("Debrief Lengkap:", height=170, placeholder="Bagikan ceritamu di sini, Ega...")

        ca, cb = st.columns(2)
        with ca:
            date_str = datetime.now().strftime('%Y-%m-%d %H:%M')
            full_log = f"MERCEDES-AMG F1 #12 // Driver: Ega\nDate: {date_str}\nTopic: {log_title}\n\n{log_content}"
            if st.download_button(
                label="💾 SIMPAN TXT PRIBADI",
                data=full_log,
                file_name=f"Mercedes_Debrief_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            ):
                st.session_state.story_submitted = True

        with cb:
            encoded_body = log_content.replace("\n", "%0D%0A")
            mailto_link = f"mailto:?subject=Mercedes%20Debrief%20#12:%20{log_title}&body={encoded_body}"
            st.markdown(
                f'<a href="{mailto_link}" target="_blank" style="text-decoration:none;">'
                f'<button style="width:100%; height:36px; border-radius:6px; background:#11161d; '
                f'border:1px solid #00A19B; color:#00A19B; font-family:\'Orbitron\'; font-weight:600; font-size:11px; cursor:pointer;">'
                f'✉️ SALIN KE EMAIL SENDIRI</button></a>',
                unsafe_allow_html=True
            )

        st.write("")
        if st.button("🏁 SELESAIKAN & TRANSMISIKAN KE RADIO TIM", type="primary", use_container_width=True):
            st.session_state.story_submitted = True
            st.rerun()

        if st.session_state.story_submitted:
            quote = get_todays_message()
            st.markdown(f"""
            <div class="radio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="color: #00A19B; font-family: 'Orbitron'; font-weight: 700; font-size: 11px;">📻 PIT WALL RADIO // FOR EGA #12</span>
                    <span class="telemetry-code">TRANSMISSION RECEIVED</span>
                </div>
                <p style="color: #f8fafc; font-size: 14.5px; font-style: italic; line-height: 1.6; margin: 8px 0 10px 0;">
                    "{quote}"
                </p>
                <span style="color: #64748b; font-size: 10px; font-family: 'JetBrains Mono';">BROADCASTED FROM YOUR TEAM CHIEF</span>
            </div>
            """, unsafe_allow_html=True)

    # SUB-MODE B: MULTI-ITEM TO-DO LIST
    elif st.session_state.sub_mode == "todo":
        st.markdown("""
        <div class="f1-panel">
            <h4 style="color: #00A19B; margin: 0 0 6px 0; font-size: 14px;">🎯 Race Strategy: Action Items</h4>
            <p style="color: #94a3b8; font-size: 12px; margin: 0;">
                Ketik targetmu satu per satu di bawah, lalu tekan <b>Enter</b> atau tombol <b>+ Tambah</b>. Kamu bisa menambah sebanyak mungkin!
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Form Input Cepat (Tekan Enter langsung nambah)
        with st.form("new_task_form", clear_on_submit=True):
            f_col1, f_col2 = st.columns([4, 1])
            with f_col1:
                task_input = st.text_input("Target Stint", placeholder="Ketik target lalu tekan Enter...", label_visibility="collapsed")
            with f_col2:
                add_btn = st.form_submit_button("➕ Tambah", use_container_width=True)
            
            if add_btn and task_input.strip():
                st.session_state.todos.append({"task": task_input.strip(), "done": False})
                st.session_state.todo_submitted = False
                st.rerun()

        # Telemetri Progress Bar
        total_tasks = len(st.session_state.todos)
        completed_tasks = sum(1 for t in st.session_state.todos if t["done"])
        progress_val = completed_tasks / total_tasks if total_tasks > 0 else 0

        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 12px 0 4px 0;">
            <span style="font-size: 12px; color: #94a3b8;"><b>Lap Telemetry:</b> {completed_tasks}/{total_tasks} Stints Cleared</span>
            <span class="telemetry-code">{int(progress_val * 100)}% COMPLETE</span>
        </div>
        """, unsafe_allow_html=True)
        st.progress(progress_val)

        # Daftar Checklist To-Do
        st.write("")
        for idx, item in enumerate(st.session_state.todos):
            cols_t = st.columns([9, 1])
            with cols_t[0]:
                checked = st.checkbox(item["task"], value=item["done"], key=f"todo_item_{idx}")
                st.session_state.todos[idx]["done"] = checked
            with cols_t[1]:
                # Tombol hapus tugas jika salah ketik
                if st.button("✕", key=f"del_{idx}", help="Hapus item ini"):
                    st.session_state.todos.pop(idx)
                    st.rerun()

        st.write("")
        if st.button("🏁 KONFIRMASI CHECKLIST HARIAN", type="primary", use_container_width=True):
            st.session_state.todo_submitted = True
            st.rerun()

        if st.session_state.todo_submitted:
            quote = get_todays_message()
            st.markdown(f"""
            <div class="radio-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="color: #00A19B; font-family: 'Orbitron'; font-weight: 700; font-size: 11px;">📻 PIT WALL RADIO // STRATEGY CHECKED</span>
                    <span class="telemetry-code">GREEN SECTOR</span>
                </div>
                <p style="color: #f8fafc; font-size: 14.5px; font-style: italic; line-height: 1.6; margin: 8px 0 10px 0;">
                    "{quote}"
                </p>
                <span style="color: #64748b; font-size: 10px; font-family: 'JetBrains Mono';">GREAT EXECUTION TODAY &bull; KEEP UP THE MOMENTUM!</span>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    n1, n2 = st.columns(2)
    with n1:
        if st.button("⬅️ KEMBALI KE COCKPIT", use_container_width=True):
            st.session_state.current_page = "home"
            st.session_state.story_submitted = False
            st.session_state.todo_submitted = False
            st.rerun()
    with n2:
        if st.button("TEST REFLEKS START 🚦", use_container_width=True):
            st.session_state.current_page = "game"
            st.session_state.reaction_state = "idle"
            st.rerun()

# ==========================================================
# 6. HALAMAN 3: MINI GAME REFLEKS
# ==========================================================
elif st.session_state.current_page == "game":
    st.markdown("""
    <div class="pitwall-header">
        <div class="telemetry-code">STAGE 03 // REFLEX CALIBRATION</div>
        <h2 style="margin: 4px 0 0 0; font-size: 20px;">5 RED LIGHTS START</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="f1-panel">
        <h4 style="color: #00A19B; margin: 0 0 4px 0; font-size: 14px;">🚦 Reaction Challenge</h4>
        <p style="color: #cbd5e1; font-size: 12.5px; margin: 0;">
            Tekan <b>START</b>. Tunggu lampu merah menyala lalu padam tiba-tiba. Tekan <b>LAUNCH!</b> secepat mungkin begitu lampu padam.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.reaction_state == "idle":
        if st.button("🔴 START LIGHTS SEQUENCE", type="primary", use_container_width=True):
            st.session_state.reaction_state = "waiting"
            st.rerun()

    elif st.session_state.reaction_state == "waiting":
        st.markdown("<h2 style='text-align: center; color: #E10600; font-size: 38px; letter-spacing: 10px;'>🔴 🔴 🔴 🔴 🔴</h2>", unsafe_allow_html=True)
        st.caption("<p style='text-align:center; color:#94a3b8; font-size:12px;'>STAND BY RPM... TAHAN...</p>", unsafe_allow_html=True)
        
        delay = random.uniform(2.0, 4.0)
        time.sleep(delay)
        st.session_state.start_time = time.time()
        st.session_state.reaction_state = "ready"
        st.rerun()

    elif st.session_state.reaction_state == "ready":
        st.markdown("<h2 style='text-align: center; color: #00A19B; font-size: 38px; letter-spacing: 10px;'>⚪ ⚪ ⚪ ⚪ ⚪</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color: #00A19B; margin: 5px 0;'>LIGHTS OUT! AWAY WE GO!</h4>", unsafe_allow_html=True)
        if st.button("⚡ LAUNCH (RELEASE CLUTCH)!", type="primary", use_container_width=True):
            reaction_ms = int((time.time() - st.session_state.start_time) * 1000)
            st.session_state.reaction_result = reaction_ms
            st.session_state.reaction_state = "finished"
            st.rerun()

    elif st.session_state.reaction_state == "finished":
        res = st.session_state.reaction_result
        st.markdown(f"""
        <div style="background: #090c10; border: 1.5px solid #00A19B; border-radius: 10px; padding: 16px; text-align: center; margin-bottom: 16px;">
            <span class="telemetry-code">REACTION TELEMETRY</span>
            <h1 style="color: #00A19B; font-size: 42px; margin: 4px 0; font-family: 'Orbitron';">{res} ms</h1>
            <p style="color: #cbd5e1; margin: 0; font-size: 13px;">
                {"Refleks gila sekelas pole position Kimi Antonelli!" if res < 250 else "Start solid dan terkontrol, siap menyerang Turn 1!"}
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 RETRY SEQUENCE", use_container_width=True):
            st.session_state.reaction_state = "idle"
            st.rerun()

        quote = get_todays_message()
        st.markdown(f"""
        <div class="radio-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="color: #00A19B; font-family: 'Orbitron'; font-weight: 700; font-size: 11px;">📻 POST-RACE RADIO // FOR EGA #12</span>
                <span class="telemetry-code">CHECKERED FLAG</span>
            </div>
            <p style="color: #f8fafc; font-size: 14.5px; font-style: italic; line-height: 1.6; margin: 8px 0 10px 0;">
                "{quote}"
            </p>
            <span style="color: #64748b; font-size: 10px; font-family: 'JetBrains Mono';">PROUD OF YOU TODAY &bull; REST WELL, CHAMPION!</span>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    if st.button("⬅️ KEMBALI KE COCKPIT", use_container_width=True):
        st.session_state.current_page = "home"
        st.session_state.reaction_state = "idle"
        st.rerun()