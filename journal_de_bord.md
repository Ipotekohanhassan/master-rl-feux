# Journal de bord — Mémoire de Master

**Sujet :** Optimisation adaptative des intersections saturées par apprentissage par renforcement — contrôle intelligent et autonome des feux de signalisation.

**Pourquoi ce journal ?**
Je note ici, au fil de l'eau, ce que je fais, les choix que je prends et les problèmes que je rencontre. L'idée, c'est de ne pas avoir à tout reconstruire de mémoire au moment de rédiger le mémoire. Chaque session de travail = une petite entrée.

---

## Phase 0 — Mise en place de l'environnement de travail

*Date : 27 juin 2026*

### Ce que je voulais faire
Installer toute la chaîne d'outils sur mon MacBook Air (Apple Silicon) : le simulateur de trafic, la passerelle pour le piloter depuis Python, et les bibliothèques d'IA pour l'apprentissage par renforcement.

### Les outils installés
- SUMO 1.27.1 (simulateur de trafic, via l'installeur officiel .pkg)
- TraCI (passerelle de contrôle temps réel depuis Python)
- sumolib (manipulation des réseaux SUMO)
- Gymnasium (environnements d'apprentissage par renforcement)
- Stable-Baselines3 (algorithme DQN, embarque PyTorch)
- sumo-rl (lien entre SUMO et Gymnasium)

### Mon environnement
- macOS Apple Silicon (ARM64)
- Python 3.11.9 via pyenv, isolé dans un environnement virtuel
- Projet dans ~/master-rl-feux

### Problèmes rencontrés et solutions
1. Homebrew refusait de s'installer (Command Line Tools introuvables) : réglé avec un lien symbolique vers mon Xcode complet.
2. SUMO impossible via Homebrew (recette cassée par la dernière version de Homebrew) : installé via l'installeur officiel .pkg, plus simple.
3. Chemin SUMO_HOME difficile à trouver (arborescence .pkg particulière sur Mac) : le bon chemin était dans .../EclipseSUMO/share/sumo.
4. Python de Homebrew cassé (bug module XML, rédhibitoire car SUMO communique en XML) : réglé en passant par pyenv (Python 3.11.9 propre).
5. Coupure réseau pendant l'installation des bibliothèques : relancé la commande, le cache a fait le reste.

### Ce que je retiens
- Sur Mac Apple Silicon, attention aux chemins d'installation non standards.
- Quand une méthode s'acharne à planter, changer d'approche plutôt que s'entêter.
- Isoler Python dans un venv dédié = projet reproductible.

### Décisions à justifier à l'oral
- Installeur .pkg pour SUMO : version stable, complète, officielle.
- pyenv plutôt que Python système : contourner un bug, garantir la stabilité.
- Environnement virtuel : isolement des dépendances, reproductibilité.

### État à la fin de la phase
Tout fonctionne. SUMO répond en ligne de commande, toutes les bibliothèques d'IA s'importent sans erreur. Dépendances figées dans requirements.txt.

---

## Phase 1 — [à venir] Baselines et cadrage scientifique

*Date : *

### Ce que je voulais faire

### Ce que j'ai fait

### Problèmes rencontrés

### Ce que je retiens

### État à la fin de la phase

---

## Phase 2 — [à venir] DQN sur intersection unique

*Date : *

---

## Phase 3 — [à venir] Extension multi-intersections

*Date : *

---

## Phase 4 — [à venir] Robustesse et approfondissement

*Date : *

---

## Phase 5 — [à venir] Rédaction et soutenance

*Date : *
