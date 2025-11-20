"""
Script d'initialisation de la base de données pour l'application
« Gestion d'Entreprise ». Exécutez simplement :

    python main.py

Cela créera (ou mettra à jour) le fichier SQLite `gestion_entreprise.db`
avec les tables nécessaires au projet.
"""

from pathlib import Path
import sqlite3
from typing import Iterable, Tuple


DB_PATH = Path(__file__).with_name("gestion_entreprise.db")


TABLE_DEFINITIONS = {
    "departments": """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """,
    "employees": """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            job_title TEXT,
            department_id INTEGER,
            manager_id INTEGER,
            start_date TEXT,
            contract_type TEXT,
            photo_path TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (department_id) REFERENCES departments(id),
            FOREIGN KEY (manager_id) REFERENCES employees(id)
        )
    """,
    "contracts": """
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            duration TEXT,
            responsibilities TEXT,
            skills TEXT,
            admin_info TEXT,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        )
    """,
    "operations": """
        CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'en attente',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """,
}


def execute_batch(cursor: sqlite3.Cursor, statements: Iterable[Tuple[str, Tuple]]) -> None:
    """Exécute une série d'instructions SQL avec leurs paramètres."""
    for sql, params in statements:
        cursor.execute(sql, params)


def ensure_tables(connection: sqlite3.Connection) -> None:
    """Crée toutes les tables définies si elles n'existent pas."""
    cursor = connection.cursor()
    for ddl in TABLE_DEFINITIONS.values():
        cursor.execute(ddl)
    connection.commit()


def seed_defaults(connection: sqlite3.Connection) -> None:
    """
    Insère des données minimales si les tables sont vides, afin de
    faciliter les premiers tests.
    """
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM departments")
    if cursor.fetchone()[0] == 0:
        departments = [
            ("Informatique", "Développement logiciel et support technique"),
            ("Ressources humaines", "Gestion du personnel et recrutement"),
            ("Finance", "Comptabilité et suivi budgétaire"),
        ]
        cursor.executemany(
            "INSERT INTO departments (name, description) VALUES (?, ?)", departments
        )

    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        execute_batch(
            cursor,
            [
                (
                    """
                    INSERT INTO employees
                        (full_name, email, phone, job_title, department_id, start_date, contract_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "Alice Dupont",
                        "alice.dupont@example.com",
                        "+33 6 01 02 03 04",
                        "Développeuse Front-end",
                        1,
                        "2024-05-01",
                        "CDI",
                    ),
                ),
                (
                    """
                    INSERT INTO employees
                        (full_name, email, phone, job_title, department_id, start_date, contract_type)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        "Marc Lemaire",
                        "marc.lemaire@example.com",
                        "+33 6 11 22 33 44",
                        "Chef de projet",
                        1,
                        "2023-09-15",
                        "CDI",
                    ),
                ),
            ],
        )

    connection.commit()


def main() -> None:
    DB_PATH.touch(exist_ok=True)
    with sqlite3.connect(DB_PATH) as connection:
        ensure_tables(connection)
        seed_defaults(connection)

    print(f"Base de données initialisée dans : {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()

