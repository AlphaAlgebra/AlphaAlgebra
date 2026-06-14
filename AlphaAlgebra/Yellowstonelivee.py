import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ---------------------------------------------------------
# INITIALIZE COGNITIVE MISSION PREFERENCE MATRIX
# ---------------------------------------------------------
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Dark (Hacker)"
if "math_color_profile" not in st.session_state:
    st.session_state.math_color_profile = "Hyper Pink"

# ---------------------------------------------------------
# STYLISTIC DOM OVERRIDES: ALIEN QUANTUM INTERFACE FONT
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://googleapis.com');

    @keyframes alien-glow {
        0% { text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 40px #00FFCC; color: #39FF14; }
        50% { text-shadow: 0 0 25px #00FFCC, 0 0 50px #FF00FF, 0 0 70px #39FF14; color: #00FFCC; }
        100% { text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14, 0 0 40px #00FFCC; color: #39FF14; }
    }
    @keyframes metrics-pulse {
        0% { text-shadow: 0 0 8px #FFFF00, 0 0 15px #FFFF00; }
        100% { text-shadow: 0 0 15px #FFFF00, 0 0 30px #FFFF00; }
    }
    
    .stApp {
        background-color: #000000 !important;
        color: #39FF14 !important;
        font-family: 'Orbitron', sans-serif !important;
    }
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 3px solid #39FF14;
    }
    /* Bind all interface typography to structural Alien Font matrix */
    h2, h3, p, span, label, .stSelectbox label, .stSlider label {
        color: #FFFF00 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 2px;
        animation: metrics-pulse 2s infinite alternate;
    }
    .alien-title {
        font-family: 'Orbitron', sans-serif !important;
        font-size: 4rem !important;
        font-weight: 900 !important;
        letter-spacing: 16px;
        text-align: center;
        animation: alien-glow 3s infinite ease-in-out;
        margin-bottom: -10px;
    }
    .neon-subtitle {
        color: #FFFF00 !important;
        font-size: 1.5rem !important;
        text-shadow: 0 0 12px #FFFF00;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 8px;
        text-align: center;
        margin-bottom: 30px;
    }
    .intel-card {
        background-color: #030303 !important;
        border: 2px solid #39FF14;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(57, 255, 20, 0.2);
    }
    div[data-baseweb="slider"] {
        background-color: #050505 !important;
        border: 2px solid #FFFF00;
        padding: 12px;
    }
    .stMarkdown p, .katex {
        color: #39FF14 !important;
        text-shadow: 0 0 8px #39FF14;
        font-family: 'Orbitron', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# COMMAND CONTROL SIDEBAR CONFIGURATION
# ---------------------------------------------------------
st.sidebar.markdown("### 🎛️ COGNITIVE QUANTUM CONTROLS")
selected_theme = st.sidebar.selectbox("SYSTEM THEME VIEW", ["Dark (Hacker)", "Light (Laboratory)"])
selected_math_color = st.sidebar.selectbox("MATH CORE MATRIX COLOR", ["Hyper Pink", "Plasma Cyan", "Radioactive Orange"])

st.session_state.theme_mode = selected_theme
st.session_state.math_color_profile = selected_math_color

input_m0 = st.sidebar.slider("REST MASS CONFIG (m_0) [kg]", min_value=0.1, max_value=25.0, value=1.6, step=0.1)
beta_val = st.sidebar.slider("VELOCITY RATIO (v/c) [beta]", min_value=0.01, max_value=0.999, value=0.120, step=0.001)
schrod_n = st.sidebar.slider("QUANTUM PRINCIPAL NUMBER (n)", min_value=1, max_value=8, value=1, step=1)
metric_tensor = st.sidebar.selectbox("SPACETIME METRIC RESOLUTION", ["Minkowski (Flat)", "Schwarzschild (Curved)"], index=1)
angle_driver = st.sidebar.slider("MANUAL CAMERA ANGLE OFFSET", min_value=0, max_value=360, value=120, step=5)

math_hex_map = {"Hyper Pink": "#FF1493", "Plasma Cyan": "#00FFCC", "Radioactive Orange": "#FF4500"}
target_math_color = math_hex_map[st.session_state.math_color_profile]

st.markdown('<p class="alien-title">ALPHA ALGEBRA</p>', unsafe_allow_html=True)
st.markdown('<p class="neon-subtitle">// EXTRATERRESTRIAL COMPUTATION HUD // v5.45</p>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MATHEMATICAL PHYSICAL CONSTANTS & CALCULATION ENGINES
# ---------------------------------------------------------
c = 3.0 * (10**8)
hbar = 1.054 * (10**-34)
v = beta_val * c
gamma = 1.0 / np.sqrt(1.0 - beta_val**2)

E_rest = input_m0 * (c**2)
E_total = gamma * E_rest
p_momentum = gamma * input_m0 * v
relativistic_mass = input_m0 * gamma
de_broglie_wavelen = hbar / (p_momentum + 1e-45)

variance_factor = gamma / 1.5
momentum_trend = (((p_momentum * 1.02) - p_momentum) / p_momentum) * 100
wavelength_trend = (((de_broglie_wavelen * 0.95) - de_broglie_wavelen) / de_broglie_wavelen) * 100

# ---------------------------------------------------------
# HUD COLUMN LAYOUT: TRENDING INTELLIGENCE MATRICES
# ---------------------------------------------------------
st.markdown("### 📊 STRATEGIC INVARIANT TELEMETRY & VECTOR TRENDS")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="intel-card">', unsafe_allow_html=True)
    st.markdown("**Lorentz Scaling Velocity**")
    st.latex(r"\gamma = \frac{1}{\sqrt{1-\beta^2}}")
    st.metric(label="LORENTZ COVARIANCE FACTOR", value=f"{gamma:.4f}", delta=f"+{variance_factor:.2f} Delta Peak")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="intel-card">', unsafe_allow_html=True)
    st.markdown("**Total Momentum Yield**")
    st.latex(r"p = \gamma m_0 v")
    st.metric(label="MOMENTUM SCALAR VECTOR", value=f"{p_momentum:.4E} Ns", delta=f"{momentum_trend:+.2f}% Acceleration")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="intel-card">', unsafe_allow_html=True)
    st.markdown("**De Broglie Compression**")
    st.latex(r"\lambda = \frac{h}{p}")
    st.metric(label="WAVE INTERFERENCE SPECTRUM", value=f"{de_broglie_wavelen:.4E} m", delta=f"{wavelength_trend:.2f}% Wave Compression", delta_color="inverse")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ULTRA-HIGH DENSITY INTERACTIVE 3D COMPUTATIONAL CANVAS
# ---------------------------------------------------------
st.markdown("### 🌌 SPACE-TIME GEODESIC ULTRA-HD RESOLUTION CANVAS")

# Triple the data point frequency density array index to generate pristine vector line profiles
n_points = 3500
theta = np.linspace(0, schrod_n * 12 * np.pi, n_points)
radius_matrix = np.linspace(0.1, input_m0 * gamma, n_points)

if metric_tensor == "Schwarzschild (Curved)":
    radius_matrix += np.sin(theta * 6) * (radius_matrix * 0.30)

x = np.sin(theta) * radius_matrix
y = np.cos(theta) * radius_matrix
z = np.log10(radius_matrix * (c**2)) * (np.sin(schrod_n * theta / 4) ** 2)

rad_angle = np.radians(angle_driver)
cam_x = 1.5 * np.cos(rad_angle)
cam_y = 1.5 * np.sin(rad_angle)

fig = go.Figure(data=[
    # 1. High-Fidelity Extruded Structural Tube/Line Track
    go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(
            color=target_math_color,
            width=8, # Maximum line trace projection
            colorscale=[[0, '#39FF14'], [0.5, '#FFFFFF'], [1, target_math_color]],
        ),
        name="Vector Trajectory"
    ),
    # 2. White-Hot Quantum Interstellar Singularity Nodes
    go.Scatter3d(
        x=x[::2], y=y[::2], z=z[::2],
        mode='markers',
        marker=dict(
            size=5,
            color=z[::2],
            colorscale=[[0, '#FFFFFF'], [0.5, target_math_color], [1, '#00FFFF']],
            opacity=0.98,
            line=dict(color='#000000', width=1.5)
        ),
        name="Quantum Field Singularity"
    )
])

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False,
    scene=dict(
        camera=dict(
            eye=dict(x=cam_x, y=cam_y, z=1.1),
            up=dict(x=0, y=0, z=1)
        ),
        xaxis=dict(gridcolor="#333333", zerolinecolor="#39FF14", showgrid=True, showbackground=False, tickfont=dict(color="#39FF14", family="Orbitron")),
        yaxis=dict(gridcolor="#333333", zerolinecolor="#39FF14", showgrid=True, showbackground=False, tickfont=dict(color="#39FF14", family="Orbitron")),
        zaxis=dict(gridcolor="#333333", zerolinecolor="#39FF14", showgrid=True, showbackground=False, tickfont=dict(color="#39FF14", family="Orbitron"))
    )
)

st.plotly_chart(fig, width='stretch')

st.markdown(
    f'<div style="color: #FFFF00; font-weight: bold; border: 2px dashed #39FF14; padding: 15px; text-align: center; background-color: #050500; font-family: \'Orbitron\', sans-serif;">'
    f'🛡️ TELEMETRY LINK LOCKED // ARCHITECTURE ALIGNMENT RECONFIGURED TO HIGH-DEFINITION ALIEN MATRIX</div>',
    unsafe_allow_html=True
)
