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

---

## Phase 1 (détaillée) — Carrefour réel et établissement des baselines

*Date : 28 juin 2026*

### Ce que je voulais faire
Mettre en place le terrain d'expérimentation scientifique : importer un vrai carrefour d'Abidjan, créer plusieurs niveaux de trafic, et mesurer comment le feu actuel se comporte. Ces mesures servent de référence (baseline) que mon IA devra battre.

### Le carrefour choisi
Carrefour "Après Barrage" (Riviera Palmeraie), boulevard Mitterrand, Cocody. Réputé pour ses embouteillages aux heures de pointe (7h-9h, 17h-19h). Plus de 50 000 véhicules/jour sur le boulevard. L'État y construit un échangeur depuis 2023, ce qui me donne un angle fort : mon IA est une alternative logicielle peu coûteuse à une infrastructure de plusieurs dizaines de milliards de FCFA.

### Import du carrefour
Via l'OSM Web Wizard de SUMO (sélection de zone sur OpenStreetMap dans le navigateur). J'ai cadré le carrefour et ses approches, en mode "Car-only Network", sans polygones ni transports en commun.

### Contenu du réseau
- 1 seule intersection à feux (mon carrefour) — idéal pour une étude sur carrefour unique.
- 54 points géométriques au total, 103 segments de routes.

### Le feu actuel (baseline "temps fixe")
4 phases, cycle de 90 secondes :
- Phase 0 (39s) : vert axe 1
- Phase 1 (6s) : orange
- Phase 2 (39s) : vert axe 2
- Phase 3 (6s) : orange
Durées rigides, ne s'adaptent jamais au trafic. C'est ce que mon IA va améliorer.

### Trois niveaux de trafic (reproductibles, seed=42)
- Fluide : 1440 véhicules
- Moyen : 3000 véhicules
- Saturé : 6000 véhicules

### Premiers résultats (feu à temps fixe)
| Scénario | Véhic. sortis | Durée(s) | Attente(s) | Perte(s) | Vitesse(m/s) |
|----------|---------------|----------|------------|----------|--------------|
| Fluide   | 744           | 302      | 216        | 246      | 7,01         |
| Moyen    | 801           | 583      | 439        | 461      | 6,43         |
| Saturé   | 1052          | 559      | 444        | 464      | 7,17         |

### Ce que je retiens
- Le temps d'attente explose en charge (216s → ~440s) : le feu à temps fixe est dépassé. C'est la justification de mon projet.
- Point à creuser : seuls 744/801/1052 véhicules sur les milliers injectés ont terminé en 1h. Le reste reste coincé. Réaliste, mais mes moyennes ne portent que sur les véhicules passés, ce qui peut biaiser la comparaison.

### Reste à faire en Phase 1
- Affiner les niveaux de trafic pour des mesures plus propres.
- Ajouter la baseline "feu actué" (capteurs prolongeant le vert) — mon vrai point de comparaison.
- Puis passer à la Phase 2 : l'agent DQN.

### État à la fin de la session
Carrefour importé et analysé, 3 scénarios créés, script de mesure fonctionnel, premières baselines mesurées. Tout sauvegardé sur Git/GitHub.
