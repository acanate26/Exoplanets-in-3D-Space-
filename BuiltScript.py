import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv("Exoplanets.csv", comment="#")

df = df.dropna(subset=["sy_dist", "ra", "dec", "pl_rade"]).copy()

# Convert RA/Dec/distance (spherical) to Cartesian (x, y, z) in parsecs
ra_rad = np.radians(df["ra"])
dec_rad = np.radians(df["dec"])
dist = df["sy_dist"]  # parsecs

df["x"] = dist * np.cos(dec_rad) * np.cos(ra_rad)
df["y"] = dist * np.cos(dec_rad) * np.sin(ra_rad)
df["z"] = dist * np.sin(dec_rad)

# Create a 3D scatter plot of the exoplanets
df["pl_eqt_fill"] = df["pl_eqt"]
temp_known = df["pl_eqt_fill"].notna()

df["hover"] = (
    "<b>" + df["pl_name"] + "</b><br>"
    + "Host star: " + df["hostname"].astype(str) + "<br>"
    + "Distance: " + df["sy_dist"].round(1).astype(str) + " pc<br>"
    + "Radius: " + df["pl_rade"].round(2).astype(str) + " Earth radii<br>"
    + "Discovery: " + df["discoverymethod"].astype(str) + " (" + df["disc_year"].astype(str) + ")"
)

methods = df["discoverymethod"].value_counts()
top_methods = methods.index.tolist()

fig = go.Figure()

fig.add_trace(
    go.Scatter3d( 
      x=[0], y=[0], z=[0],
      mode="markers+text",
      marker=dict(size=6, color="yellow", symbol="diamond", line=dict(color="white", width=1)),
    text=["Sol (our Sun)"],
    textposition="top center",
    textfont=dict(color="white", size=11),
    hoverinfo="text",
    hovertext=["Sol - the Sun, our reference point"],
    name="Sol",
    showlegend=True,
))

palette = [
    "#4FC3F7", "#FF8A65", "#AED581", "#BA68C8", "#FFD54F",
    "#4DB6AC", "#F06292", "#90A4AE", "#A1887F", "#DCE775",
]

for i, method in enumerate(top_methods):
    sub = df[df["discoverymethod"] == method]
    color = palette[i % len(palette)]

    fig.add_trace(go.Scatter3d(
        x=sub["x"], y=sub["y"], z=sub["z"],
        mode="markers",
        marker=dict(
            size=np.clip(sub["pl_rade"] * 1.4, 2, 22),
            color=color,
            opacity=0.75,
            line=dict(width=0),
        ),
        text=sub["hover"],
        hoverinfo="text",
        name=f"{method} ({len(sub)})",
    ))

fig.update_layout(
      template="plotly_dark",
      title=dict(
          text= "Confirmed Exoplanets in 3D Space (relative to Earth)",
          font= dict(size=20, color="white"),
          x=0.5,
      ),
      scene=dict(
        xaxis=dict(title="x (parsecs)", backgroundcolor="rgb(10,10,20)", gridcolor="rgba(255,255,255,0.15)"),
        yaxis=dict(title="y (parsecs)", backgroundcolor="rgb(10,10,20)", gridcolor="rgba(255,255,255,0.15)"),
        zaxis=dict(title="z (parsecs)", backgroundcolor="rgb(10,10,20)", gridcolor="rgba(255,255,255,0.15)"),
        bgcolor="rgb(5,5,15)",
       ),
    paper_bgcolor="rgb(5,5,15)",
    font=dict(color="white"),
    legend=dict(
        title="Discovery method (click to toggle)",
        bgcolor="rgba(20,20,30,0.7)",
        bordercolor="rgba(255,255,255,0.2)",
        borderwidth=1,
    ),
    margin=dict(l=0, r=0, t=60, b=0),
    height=850,
)

fig.write_html(
    "Exoplanets_3d.html",
    include_plotlyjs="cdn",
    full_html=True,
    config={"displaylogo": False},
)

print(f"Plotted {len(df)} exoplanets in 3D space. Output saved to 'Exoplanets_3d.html'.")
print("Saved to Exoplanets_3d.html")
   