"""Aplica o mysql-schema.sql no banco configurado (usa a mesma config do app.py)."""

from pathlib import Path

import pymysql

from app import DB_CONFIG

SQL_FILE = Path(__file__).with_name("mysql-schema.sql")


def statements(text: str):
    lines = [ln for ln in text.splitlines() if not ln.strip().startswith("--")]
    for raw in "\n".join(lines).split(";"):
        stmt = raw.strip()
        if stmt:
            yield stmt


def main() -> None:
    sql = SQL_FILE.read_text(encoding="utf-8")
    conn = pymysql.connect(**{k: v for k, v in DB_CONFIG.items() if k != "cursorclass"})
    try:
        with conn.cursor() as cur:
            for stmt in statements(sql):
                cur.execute(stmt)
        conn.commit()
        with conn.cursor() as cur:
            cur.execute("SHOW TABLES")
            tables = [row[0] for row in cur.fetchall()]
        print("OK - tabelas no banco:", tables)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
