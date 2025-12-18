Dieses Projekt ist ein vollständiges HR- und Ressourcen-Management-System, bestehend aus:

🖥 Backend: FastAPI + SQLAlchemy + PostgreSQL

🌐 Frontend: Angular (SCSS)

🗄 Datenbank: PostgreSQL

🔐 Erweiterbar für Authentifizierung

📦 Clean Architecture mit insgesamt 15+ Datenbanktabellen

🚀 Hauptfunktionen
👥 Benutzerverwaltung (Users)

Mitarbeiter anlegen

Mitarbeiterdaten bearbeiten

Sprachen, Adressen, Gruppen zuordnen

Mitarbeiterstatus verwalten (aktiv, inaktiv, ausgeschieden)

🏢 Organisationsstruktur

Abteilungen (Departments) verwalten

Positionen verwalten

Arbeitszeitmodelle verwalten

🌍 Sprachenverwaltung

Sprachen hinzufügen / bearbeiten

Sprachkenntnisse pro Mitarbeiter zuordnen

🚗 Ressourcenverwaltung (Resources)

Räume

Fahrzeuge

Weitere Ressourcen können leicht ergänzt werden

📆 Reservierungssystem

Räume buchen

Fahrzeuge buchen

Reservierungsstatus verwalten

Übersicht über alle Reservierungen
users
addresses
departments
positions
working_time_types
contracts
salaries
certificates
languages
user_languages
groups
user_groups
resources
rooms
cars
reservations
insurance_types
user_insurances

python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt

DATABASE_URL=postgresql+psycopg://hr_user:1234@localhost:5432/hr_system


uvicorn app.main:app --reload


Backend erreichbar unter:

➡️ http://127.0.0.1:8000

🌐 Frontend – Angular Installation

n das Frontend wechseln
cd hr-frontend

2️⃣ Abhängigkeiten installieren
npm install

3️⃣ Angular starten
ng serve -o


Frontend erreichbar unter:

➡️ http://localhost:4200
*.sql
*.sql.gz
*.dump
hr_api2/
│── app/
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   ├── db.py
│   └── main.py
│
├── hr-frontend/
│   ├── src/app/
│   ├── components/
│   ├── pages/
│   └── services/
│
├── .env
└── README.md
