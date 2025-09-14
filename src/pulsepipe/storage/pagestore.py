import sqlite3
from typing import List
from pulsepipe.core.config import Config

class PageStore:
    def __init__(self, config: Config):
        self.db_path = config.sqlite_path
        self._ensure_schema()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _ensure_schema(self):
        schema = """
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            html TEXT,
            markdown TEXT,
            image_urls TEXT
        );
        """
        with self._connect() as conn:
            conn.execute(schema)
            conn.commit()

    def save_page(self, url: str, html: str, markdown: str, image_urls: List[str]):
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO pages (url, html, markdown, image_urls) VALUES (?, ?, ?, ?)",
                (url, html, markdown, ",".join(image_urls))
            )
            conn.commit()

    def get_page(self, url: str) -> dict:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM pages WHERE url = ?", (url,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "url": row[1],
                    "html": row[2],
                    "markdown": row[3],
                    "image_urls": row[4].split(",")
                }
            return {}

    def delete_page(self, url: str):
        with self._connect() as conn:
            conn.execute("DELETE FROM pages WHERE url = ?", (url,))
            conn.commit()

    def list_pages(self) -> List[str]:
        with self._connect() as conn:
            cursor = conn.execute("SELECT url FROM pages")
            return [row[0] for row in cursor.fetchall()]
