#!/usr/bin/env python3
"""
Mesure des baselines pour le carrefour Apres Barrage.
Pour chaque niveau de trafic (fluide / moyen / sature), lance une simulation
SUMO avec le feu a temps fixe et extrait les metriques de performance.
"""

import os
import subprocess
import xml.etree.ElementTree as ET

if "SUMO_HOME" not in os.environ:
    raise RuntimeError("La variable SUMO_HOME n'est pas definie.")

SUMO_BIN = "sumo"
NET_FILE = "osm.net.xml"

SCENARIOS = {
    "fluide": "routes_fluide.rou.xml",
    "moyen": "routes_moyen.rou.xml",
    "sature": "routes_sature.rou.xml",
}


def lancer_simulation(nom, routes):
    stats = f"baseline_stats_{nom}.xml"
    tripinfo = f"baseline_tripinfo_{nom}.xml"
    cmd = [
        SUMO_BIN, "-n", NET_FILE, "-r", routes,
        "--begin", "0", "--end", "3600",
        "--statistic-output", stats,
        "--tripinfo-output", tripinfo,
        "--duration-log.statistics", "true",
        "--no-step-log", "true",
        "--no-warnings", "true",
        "--ignore-route-errors", "true",
    ]
    print(f"  Simulation '{nom}' en cours...")
    subprocess.run(cmd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return stats


def lire_metriques(stats):
    root = ET.parse(stats).getroot()
    s = root.find("vehicleTripStatistics")
    return {
        "vehicules": int(s.get("count")),
        "duree": float(s.get("duration")),
        "attente": float(s.get("waitingTime")),
        "perte": float(s.get("timeLoss")),
        "vitesse": float(s.get("speed")),
    }


def main():
    print("=" * 70)
    print("BASELINES - Carrefour Apres Barrage (feu a temps fixe)")
    print("=" * 70)
    res = {}
    for nom, routes in SCENARIOS.items():
        res[nom] = lire_metriques(lancer_simulation(nom, routes))

    print("\n" + "=" * 70)
    print(f"{'Scenario':<10}{'Vehic.':>9}{'Duree(s)':>11}{'Attente(s)':>12}{'Perte(s)':>11}{'Vit(m/s)':>10}")
    print("-" * 70)
    for nom, m in res.items():
        print(f"{nom:<10}{m['vehicules']:>9}{m['duree']:>11.2f}{m['attente']:>12.2f}{m['perte']:>11.2f}{m['vitesse']:>10.2f}")
    print("=" * 70)
    print("\nReference a battre par l'agent IA.")


if __name__ == "__main__":
    main()
