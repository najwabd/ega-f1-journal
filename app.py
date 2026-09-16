import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# ==========================================================
# 1. PESAN HARIAN DARI KAMU UNTUK EGA
# ==========================================================
DAILY_MESSAGES = [
    "Radio check, Ega. Seperti kata Toto ke Kimi Antonelli: 'Focus on your line, the speed is already there.' Apapun rintangan hari ini, kamu punya talenta dan determinasi buat ngelewatinnya!",
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
        background-color: #080a0d !important;
        background-image: radial-gradient(#151b22 1px, transparent 1px);
        background-size: 18px 18px;
        color: #f1f5f9 !important;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, label p {
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 1px;
        color: #f1f5f9 !important;
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
        background: #11161d !important;
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

    /* Target input container Streamlit BaseWeb */
    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    div[data-baseweb="textarea"] {
        background-color: #0f1318 !important;
        border: 1.5px solid #24303e !important;
        border-radius: 6px !important;
    }

    input[type="text"], textarea {
        background-color: transparent !important;
        color: #f8fafc !important;
        border: none !important;
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
        if st.button("🏎️ 3D TRACK SIM", use_container_width=True):
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

    elif st.session_state.sub_mode == "todo":
        st.markdown("""
        <div class="f1-panel">
            <h4 style="color: #00A19B; margin: 0 0 6px 0; font-size: 14px;">🎯 Race Strategy: Action Items</h4>
            <p style="color: #94a3b8; font-size: 12px; margin: 0;">
                Ketik targetmu satu per satu di bawah, lalu tekan <b>Enter</b> atau tombol <b>+ Tambah</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)

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

        st.write("")
        for idx, item in enumerate(st.session_state.todos):
            cols_t = st.columns([9, 1])
            with cols_t[0]:
                checked = st.checkbox(item["task"], value=item["done"], key=f"todo_item_{idx}")
                st.session_state.todos[idx]["done"] = checked
            with cols_t[1]:
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
        if st.button("MAIN 3D SIMULATOR 🏎️", use_container_width=True):
            st.session_state.current_page = "game"
            st.rerun()

# ==========================================================
# 6. HALAMAN 3: MINI GAME 3D RACING SIMULATOR
# ==========================================================
elif st.session_state.current_page == "game":
    st.markdown("""
    <div class="pitwall-header">
        <div class="telemetry-code">STAGE 03 // 3D RACING LINE SIMULATOR</div>
        <h2 style="margin: 4px 0 0 0; font-size: 20px;">MERCEDES #12 ON-TRACK</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="f1-panel">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-family: 'Orbitron'; color: #00A19B; font-size: 14px;">🎮 Kimi Antonelli Track Simulator</span>
            <span class="telemetry-code">CAR: W16 // DRIVER: EGA</span>
        </div>
        <p style="color: #94a3b8; font-size: 12px; margin: 6px 0 0 0;">
            Arahkan mobil tetap di aspal sirkuit dan ambil titik Apex hijau toska! 
            Gunakan <b>Tombol Panah Kiri/Kanan</b> atau <b>A / D</b> di keyboard (atau sentuh sisi kiri/kanan di HP).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 3D THREE.JS CANVAS GAME (Embed Full Canvas)
    game_3d_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body { margin: 0; overflow: hidden; background: #080a0d; font-family: sans-serif; }
        #canvas-container { width: 100%; height: 420px; position: relative; border-radius: 10px; overflow: hidden; border: 1.5px solid #1e2732; }
        #hud {
            position: absolute; top: 12px; left: 16px; color: #f8fafc; z-index: 10;
            background: rgba(15, 19, 24, 0.85); padding: 8px 14px; border-radius: 6px;
            border: 1px solid #00A19B; font-size: 12px; font-weight: bold;
        }
        #hud span { color: #00A19B; font-size: 16px; }
        #touch-controls {
            position: absolute; bottom: 0; left: 0; width: 100%; height: 100%; display: flex; z-index: 5;
        }
        .touch-zone { flex: 1; height: 100%; }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="canvas-container">
            <div id="hud">SPEED: <span id="speed-val">285</span> KM/H &bull; APEX SCORE: <span id="score-val">0</span></div>
            <div id="touch-controls">
                <div class="touch-zone" id="touch-left"></div>
                <div class="touch-zone" id="touch-right"></div>
            </div>
        </div>

        <script>
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x080a0d, 0.015);

            const camera = new THREE.PerspectiveCamera(65, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(0, 3.2, 7);
            camera.lookAt(0, 1.2, -10);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            // Lighting
            const ambient = new THREE.AmbientLight(0xffffff, 0.7);
            scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0x00A19B, 0.9);
            dirLight.position.set(5, 12, 10);
            scene.add(dirLight);

            // Ground & Asphalt Track
            const trackGeo = new THREE.PlaneGeometry(12, 400, 10, 80);
            const trackMat = new THREE.MeshBasicMaterial({ color: 0x15191e, wireframe: false });
            const track = new THREE.Mesh(trackGeo, trackMat);
            track.rotation.x = -Math.PI / 2;
            scene.add(track);

            // Red/White Curbs (Batas Sirkuit F1)
            const curbGeo = new THREE.PlaneGeometry(0.8, 400);
            const curbMat = new THREE.MeshBasicMaterial({ color: 0xe10600 });
            const leftCurb = new THREE.Mesh(curbGeo, curbMat);
            leftCurb.rotation.x = -Math.PI / 2;
            leftCurb.position.x = -6.4;
            scene.add(leftCurb);

            const rightCurb = new THREE.Mesh(curbGeo, curbMat);
            rightCurb.rotation.x = -Math.PI / 2;
            rightCurb.position.x = 6.4;
            scene.add(rightCurb);

            // Mercedes W16 3D Car Model (Stylized Low-poly Chassis)
            const carGroup = new THREE.Group();

            // Main Body (Silver/Dark)
            const bodyGeo = new THREE.BoxGeometry(1.2, 0.45, 3.4);
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0x11161d, roughness: 0.3 });
            const carBody = new THREE.Mesh(bodyGeo, bodyMat);
            carBody.position.y = 0.4;
            carGroup.add(carBody);

            // Front Nose Cone & Wing
            const noseGeo = new THREE.BoxGeometry(0.6, 0.25, 1.6);
            const noseMat = new THREE.MeshStandardMaterial({ color: 0x00A19B });
            const carNose = new THREE.Mesh(noseGeo, noseMat);
            carNose.position.set(0, 0.3, -2.0);
            carGroup.add(carNose);

            const frontWing = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.1, 0.6), new THREE.MeshStandardMaterial({ color: 0x080a0d }));
            frontWing.position.set(0, 0.2, -2.6);
            carGroup.add(frontWing);

            // Rear Wing with Petronas Cyan accent
            const rearWing = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.5, 0.3), new THREE.MeshStandardMaterial({ color: 0x00A19B }));
            rearWing.position.set(0, 0.9, 1.6);
            carGroup.add(rearWing);

            // 4 F1 Wheels
            const wheelGeo = new THREE.CylinderGeometry(0.4, 0.4, 0.35, 16);
            const wheelMat = new THREE.MeshBasicMaterial({ color: 0x020406 });
            const wheels = [];
            const wheelPos = [
                [-1.1, 0.4, -1.2], [1.1, 0.4, -1.2],
                [-1.2, 0.45, 1.2], [1.2, 0.45, 1.2]
            ];
            wheelPos.forEach(pos => {
                const w = new THREE.Mesh(wheelGeo, wheelMat);
                w.rotation.z = Math.PI / 2;
                w.position.set(...pos);
                wheels.push(w);
                carGroup.add(w);
            });

            scene.add(carGroup);

            // Collectible Apex Targets (Green Petronas Orbs)
            const apexes = [];
            const apexGeo = new THREE.OctahedronGeometry(0.4);
            const apexMat = new THREE.MeshBasicMaterial({ color: 0x00A19B, wireframe: true });
            for (let i = 0; i < 8; i++) {
                const apex = new THREE.Mesh(apexGeo, apexMat);
                apex.position.set((Math.random() - 0.5) * 8, 0.6, -20 - i * 35);
                scene.add(apex);
                apexes.push(apex);
            }

            // Controls & Physics
            let carX = 0;
            let targetX = 0;
            let score = 0;
            let speed = 285;
            const keys = { left: false, right: false };

            window.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') keys.left = true;
                if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') keys.right = true;
            });
            window.addEventListener('keyup', (e) => {
                if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') keys.left = false;
                if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') keys.right = false;
            });

            // Touch Screen Support for Phones
            document.getElementById('touch-left').addEventListener('touchstart', (e) => { e.preventDefault(); keys.left = true; });
            document.getElementById('touch-left').addEventListener('touchend', () => { keys.left = false; });
            document.getElementById('touch-right').addEventListener('touchstart', (e) => { e.preventDefault(); keys.right = true; });
            document.getElementById('touch-right').addEventListener('touchend', () => { keys.right = false; });

            // Animation Loop
            function animate() {
                requestAnimationFrame(animate);

                // Movement physics
                if (keys.left && targetX > -4.8) targetX -= 0.16;
                if (keys.right && targetX < 4.8) targetX += 0.16;

                carX += (targetX - carX) * 0.12;
                carGroup.position.x = carX;
                carGroup.rotation.y = (carX - targetX) * 0.4; // Body tilt
                carGroup.rotation.z = (carX - targetX) * 0.2;

                // Wheel spin
                wheels.forEach(w => w.rotation.x += 0.3);

                // Move Track & Apex Objects towards car
                apexes.forEach(apex => {
                    apex.position.z += 0.9;
                    apex.rotation.y += 0.05;

                    // Collision check
                    if (Math.abs(apex.position.z - carGroup.position.z) < 1.5 && Math.abs(apex.position.x - carGroup.position.x) < 1.2) {
                        score += 10;
                        document.getElementById('score-val').innerText = score;
                        apex.position.z = -220;
                        apex.position.x = (Math.random() - 0.5) * 8;
                    }

                    if (apex.position.z > 8) {
                        apex.position.z = -220;
                        apex.position.x = (Math.random() - 0.5) * 8;
                    }
                });

                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            });
        </script>
    </body>
    </html>
    """

    components.html(game_3d_html, height=440)

    # RADIO KATA-KATA PENUTUP DARI KAKAK
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
        st.rerun()