import sqlite3
import os
import logging

DB_PATH = "chunks.db"
logger = logging.getLogger(__name__)
def init_db():
    if not os.path.exists(DB_PATH):
        logger.info("Initializing the database.")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE chunks (
                id INTEGER PRIMARY KEY,
                content TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE tfidf_vectors (
                chunk_id INTEGER,
                term TEXT,
                value REAL,
                FOREIGN KEY(chunk_id) REFERENCES chunks(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE cache (
                question TEXT PRIMARY KEY,
                answer TEXT
            )
        ''')
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully.")

def insert_chunk(content, tfidf_vector):
    logger.info("Inserting chunk into database.")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO chunks (content) VALUES (?)', (content,))
    chunk_id = cursor.lastrowid
    for term, value in tfidf_vector.items():
        cursor.execute('INSERT INTO tfidf_vectors (chunk_id, term, value) VALUES (?, ?, ?)', (chunk_id, term, value))
    conn.commit()
    conn.close()
    logger.info("Chunk inserted successfully.")

def get_cached_answer(question):
    logger.info(f"Fetching cached answer for question: {question}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT answer FROM cache WHERE question = ?', (question,))
    result = cursor.fetchone()
    conn.close()
    if result:
        logger.info(f"Cached answer found for question: {question}")
        return result[0]
    logger.info(f"No cached answer found for question: {question}")
    return None

def cache_answer(question, answer):
    logger.info(f"Caching answer for question: {question}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO cache (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()
    logger.info(f"Answer cached for question: {question}")

def search_chunks(query_terms, top_n=3):
    logger.info("Searching chunks for query terms.")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = 'SELECT chunk_id, SUM(value) as score FROM tfidf_vectors WHERE term IN ({seq}) GROUP BY chunk_id ORDER BY score DESC LIMIT ?'.format(seq=','.join(['?']*len(query_terms)))
    cursor.execute(query, query_terms + [top_n])
    chunk_ids = [row[0] for row in cursor.fetchall()]
    conn.close()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    chunks = []
    for chunk_id in chunk_ids:
        cursor.execute('SELECT content FROM chunks WHERE id = ?', (chunk_id,))
        result = cursor.fetchone()
        if result:
            chunks.append(result[0])
    conn.close()

    logger.info(f"Found {len(chunks)} chunks for query terms.")
    return chunks


