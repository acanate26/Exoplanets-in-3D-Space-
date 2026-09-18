EXOPLANETS IN 3D SPACE:

An interactive 3D visualization of every confirmed exoplanet, plotted at its true position in space relative to Earth — built with Python and Plotly.

🛠️WHAT THIS IS:

This project takes NASA's public catalog of confirmed exoplanets and turns it from a flat spreadsheet into a navigable 3D star map. Instead of a static chart, you can rotate, zoom, and hover over individual planets to explore where they sit in space and how they compare to one another.

Each planet's position is calculated from its real astronomical coordinates — right ascension, declination, and distance from Earth — converted into Cartesian (x, y, z) coordinates, the same way you'd convert a compass direction and distance into a point on a map, just in three dimensions instead of two.

🗂️WHAT IT SHOWS:
-6,289 confirmed exoplanets, positioned at their real distance and direction from Earth (in parsecs)
-Sol (our Sun) marked at the center as a reference point
-Point size scaled to each planet's radius (relative to Earth)
-Point color grouped by discovery method (Transit, Radial Velocity, Direct Imaging, etc.) — toggle any group on/off from the legend
-Hover details on every planet: name, host star, distance, radius, and how/when it was discovered
-A pattern worth noticing

The planets aren't spread evenly across the sky — they cluster heavily in certain directions. That's not where exoplanets actually concentrate; it's a reflection of where our telescopes have looked. Missions like Kepler stared at one fixed patch of sky for years, so that region is massively overrepresented in the data. It's a good reminder that a visualization of "what we've found" is really a visualization of "where we've looked."

📊DATA SOURCE:

NASA Exoplanet Archive — Planetary Systems Composite Parameters (PSCompPars) table, downloaded September 2026. This table gives one best-estimate row per confirmed planet, combining measurements from multiple studies.

Tech stack
Python — data loading and coordinate transformation
pandas — cleaning and filtering the dataset
NumPy — spherical-to-Cartesian coordinate conversion
Plotly — interactive 3D rendering, exported to a single standalone HTML file
Running it yourself

Clone this repo and install the dependencies:
bash
   pip install pandas numpy plotly
Download the latest PSCompPars table as a CSV and save it as Exoplanets.csv in this folder or whatever file.name you choose!
Run the build script:
bash
   python3 build_viz.py
Open the generated Exoplanets_3d.html in any browser!


Data courtesy of NASA's Exoplanet Archive(https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars), operated by the California Institute of Technology under contract with NASA.


<img width="1806" height="832" alt="Screenshot 2026-09-17 235847" src="https://github.com/user-attachments/assets/4e9229ab-67af-4825-bac0-b2a52af79ce3" />









