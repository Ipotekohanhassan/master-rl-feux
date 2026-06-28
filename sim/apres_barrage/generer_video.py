#!/usr/bin/env python3
"""
Genere une video du carrefour Apres Barrage en mode sature.
Pilote SUMO via TraCI, capture une image par etape, puis assemble en mp4.
"""
import os
import traci
import subprocess
import shutil

DOSSIER_IMAGES = "frames"
ROUTES = "routes_sature.rou.xml"
NET = "osm.net.xml"
DUREE = 500          # secondes simulees a filmer
ZOOM = 700           # niveau de zoom camera
CENTRE_X = 2800      # centre du carrefour
CENTRE_Y = 1400

# Prepare le dossier d'images
if os.path.exists(DOSSIER_IMAGES):
    shutil.rmtree(DOSSIER_IMAGES)
os.makedirs(DOSSIER_IMAGES)

# Lance sumo-gui pilote par TraCI
sumo_cmd = [
    "sumo-gui", "-n", NET, "-r", ROUTES,
    "--start", "--quit-on-end",
    "--window-size", "1280,720",
    "--delay", "0",
]
traci.start(sumo_cmd)

# Force la camera sur le carrefour
traci.gui.setZoom("View #0", ZOOM)
traci.gui.setOffset("View #0", CENTRE_X, CENTRE_Y)

# Colore les vehicules selon leur vitesse (rouge = bloque)
traci.gui.setSchema("View #0", "real world")

print("Capture des images en cours...")
etape = 0
while etape < DUREE:
    traci.simulationStep()
    fichier = os.path.join(DOSSIER_IMAGES, f"img_{etape:04d}.png")
    traci.gui.screenshot("View #0", fichier)
    etape += 1
    if etape % 50 == 0:
        print(f"  {etape}/{DUREE} images")

traci.close()
print("Capture terminee. Assemblage de la video...")

# Assemble les images en mp4 avec ffmpeg (25 images/seconde)
subprocess.run([
    "ffmpeg", "-y", "-framerate", "25",
    "-i", os.path.join(DOSSIER_IMAGES, "img_%04d.png"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "carrefour_sature.mp4"
], check=True)

print("\nVideo creee : carrefour_sature.mp4")
