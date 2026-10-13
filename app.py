import streamlit as st
import plotly.express as px
from src.data import generate_employees
from src.nine_box import plot_data, nine_box_label, grid_position

st.title("⭐ Performance Review — 9-Box Grid")
df = generate_employees(80)
data = plot_data(df.to_dict("records"))

fig = px.scatter(
    data, x="performance", y="potential", color="label", text="name",
    range_x=[1, 5], range_y=[1, 5],
    title="9-Box Grid: Performance vs Potential")
fig.update_traces(textposition="top center")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Сотрудники по категориям")
labels = {}
for d in data:
    labels.setdefault(d["label"], []).append(d["name"])
for label, names in labels.items():
    st.write(f"**{label}** ({len(names)}): {', '.join(names[:5])}...")
