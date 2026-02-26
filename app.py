import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Setup
st.title("Physics Utility: Relativistic Kinetic Energy")
st.write("Calculate the energy of a particle as it approaches $c$.")

# 2. User Inputs (The "Clickable" part)
mass = st.number_input("Mass of particle (kg)", value=1.0, step=0.1)
velocity_pct = st.slider("Velocity as % of speed of light", 0, 99, 50)

# 3. Physics Logic
c = 3e8
v = (velocity_pct / 100) * c
gamma = 1 / np.sqrt(1 - (v**2 / c**2))
ke_relativistic = (gamma - 1) * mass * c**2
ke_classical = 0.5 * mass * v**2

# 4. Display Results
st.metric("Relativistic KE (Joules)", f"{ke_relativistic:.2e}")
st.write(f"At {velocity_pct}% of $c$, the Lorentz factor ($\gamma$) is {gamma:.4f}")

# 5. Visualizations (Keeps people on the page longer)
v_range = np.linspace(0, 0.99 * c, 100)
gamma_range = 1 / np.sqrt(1 - (v_range**2 / c**2))
ke_range = (gamma_range - 1) * mass * c**2

fig, ax = plt.subplots()
ax.plot(v_range/c, ke_range, label="Relativistic")
ax.plot(v_range/c, 0.5 * mass * v_range**2, '--', label="Classical")
ax.set_xlabel("v/c")
ax.set_ylabel("Energy (J)")
ax.legend()
st.pyplot(fig)
