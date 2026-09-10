à utiliser avec **https://hackmd.io/**

# :clipboard:  Présentation du sujet

* **Sujet** : Application pour gérer une liste de players et de joueuses
* **Tuteur / Tutrice** : Rick Auray (rick.auray@ensai.fr)
* [Dépôt GitHub](https://github.com/ludo2ne/ENSAI-projet-info-2A-template)

# :dart: Échéances

---
Dossier d'Analyse :  :clock1: <iframe src="https://free.timeanddate.com/countdown/i83zdl7u/n1264/cf11/cm0/cu2/ct4/cs0/ca0/co0/cr0/ss0/cac009/cpcf00/pcfff/tcfff/fs100/szw256/szh108/iso2023-10-07T12:00:00" allowtransparency="true" frameborder="0" width="130" height="16"></iframe>

---

```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#E3F2FD',
      'primaryTextColor': '#0D47A1',
      'primaryBorderColor': '#1E88E5',
      'lineColor': '#42A5F5',
      'secondaryColor': '#E8F5E9',
      'tertiaryColor': '#FFF3E0',
      'sectionBkgColor': '#F5F5F5',
      'altSectionBkgColor': '#FFFFFF',
      'sectionBkgColor2': '#EEEEEE',
      'gridColor': '#E0E0E0',
      'todayLineColor': '#E53935'
    }
  }
}%%
gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    title       Planning du Projet

    section Jalons & Échéances
    TP1 et Suivi 1                            :milestone, m1, 2026-08-28, 0d
    TP2 et Suivi 2                            :milestone, m2, 2026-09-04, 0d
    TP3 et Suivi 3                            :milestone, m3, 2026-09-11, 0d
    Dossier Analyse                           :milestone, r1, 2026-09-17, 0d
    TP4                                       :milestone, m4, 2026-09-18, 0d
    TP5 et Suivi 5                            :milestone, m5, 2026-09-25, 0d
    Suivi 6                                   :milestone, m6, 2026-11-03, 0d
    Suivi 7                                   :milestone, m7, 2026-11-05, 0d
    Rapport + Code                            :milestone, r2, 2026-11-25, 0d
    Soutenance                                :milestone, r3, 2026-12-09, 0d

    section Événements
    Vacances de Toussaint                     :crit, vac, 2026-10-26, 2026-10-30
    3j immersion                              :active, imm, 2026-11-03, 3d

    section Phase d'Analyse
    Découverte du sujet                       :done, a1, 2026-08-28, 2026-09-04
    Création du diagramme de classe           :active, a2, 2026-09-04, 2026-09-11
    Création du diagramme d'activité          :active, a3, 2026-09-04, 2026-09-11
    Création du diagramme de cas d'utilisation:active, a4, 2026-09-04, 2026-09-11
    Création du diagramme de séquence         :active, a5, 2026-09-04, 2026-09-11
    Création du modèle de données             :active, a6, 2026-09-04, 2026-09-11
    Rédaction du dossier d'analyse            :active, a7, 2026-09-11, 2026-09-17

    section Phase de Développement
    Création de la base de données            :d1, 2026-09-18, 2026-09-26
    Création de l'API                         :d2, 2026-09-27, 2026-10-04
    Fonctionnalité calculerDJU                :d3, 2026-10-04, 2026-10-15
    Fonctionnalité creerZonage                :d4, 2026-10-04, 2026-10-15
    Fonctionnalité consulterDJU               :d4, 2026-10-04, 2026-10-15
    Autres fonctionnalités basiques           :d5, 2026-10-04, 2026-10-15
    Fonctionnalités connexion                 :d6, 2026-10-16, 2026-10-25
    Fonctionnalités changerFormat             :d8, 2026-10-16, 2026-10-25
    Fonctionnalités conserverResultats        :d7, 2026-10-16, 2026-10-25
    Mise à jour des diagrammes UML            :d9, 2026-10-26, 2026-11-04
    Rédaction du rapport final                :d10, 2026-11-08, 2026-11-22
    Préparation de la soutenance              :d11, 2026-11-25, 2026-12-06
```

# :calendar: Livrables

| Date    | Livrables                                                    |
| ------- | ------------------------------------------------------------ |
| 17 sept. | [Dossier d'Analyse](https://www.overleaf.com/)               |
| 25 nov. | Rapport final + code (:hammer_and_wrench:  [correcteur orthographe et grammaire](https://www.scribens.fr/))|
| 09 déc. | Soutenance                                                   |

# :construction: Todo List

## Dossier Analyse

* [x] Diagramme de Gantt
* [x] Diagramme de cas d'utilisation
* [x] Diagramme de classe
* [ ] Répartition des parties à rédiger

## Code

* [ ] Créer dépôt Git commun
  * [ ] vérifier que tout le monde peut **push** et **pull**
* [ ] Version 0 de l'application
  * coder une et une seule fonctionnalité simple de A à Z, et faire tourner l'appli
  * cela permettra à toute l'équipe d'avoir une bonne base de départ
* [ ] Lister classes et méthodes à coder

---

* [ ] appel WS
* [ ] création WS
* [ ] Vue inscription
* [ ] hacher password

---

<style>h1 {
    color: darkblue;
    font-family: "Calibri";
    font-weight: bold;
    background-color: seagreen;
    padding-left: 10px;
}

h2 {
    color: darkblue;
    background-color: darkseagreen;
    margin-right: 10%;
    padding-left: 10px;
}

h3 {
    color: darkblue;
    background-color: lightseagreen;
    margin-right: 20%;
    padding-left: 10px;
}

h4 {
    color: darkblue;
    background-color: aquamarine;
    margin-right: 30%;
    padding-left: 10px;
}

</style>
