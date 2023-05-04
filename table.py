import sqlite3
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText

def get_all_prospects_from_database():
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prospects;")
    prospects = cursor.fetchall()

    conn.close()
    return prospects


def get_prospect_by_id_from_database(prospect_id):
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM prospects WHERE id = ?;", (prospect_id,))
    prospect = cursor.fetchone()

    conn.close()
    return prospect


def update_email_status(prospect_id, status):
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE prospects SET email_status = ? WHERE id = ?;", (status, prospect_id))

    conn.commit()
    conn.close()


# Create the prospects table if it doesn't exist
conn = sqlite3.connect("prospects.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prospects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    email_status TEXT NOT NULL DEFAULT "not_sent",
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

# ... (search_signalhire and parse_signalhire_response functions)

def store_prospect_in_database(prospect):
    conn = sqlite3.connect("prospects.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO prospects (name, company, email)
    VALUES (?, ?, ?);
    """, (prospect["name"], prospect["company"], prospect["email"]))

    conn.commit()
    conn.close()

# ... (send_email and update_email_status functions)

def main():
    signalhire_api_key = "ErLf7TuqUG1BPE8Lxy3U93O63o2G"
    query = "founders business development early-stage web startups"

import requests

def get_signalhire_data(api_key):
    url = "https://api.signalhire.com/v3/search"
    headers = {"Authorization": f"Bearer {api_key}"}

    # Add your query parameters to find founders and business development personnel
    params = {
        "q": "founder OR 'business development'",
        "industry": "internet"
    }

    response = requests.get(url, headers=headers, params=params)
    return response


    response = search_signalhire(signalhire_api_key, query)
    prospects = parse_signalhire_response(response)

    for prospect in prospects:
        store_prospect_in_database(prospect)

        email_credentials = Credentials.from_authorized_user_file("client_secret_381200326445-u8h915n3avt28s0c0iokobsjf2v67c4k.apps.googleusercontent.com.json")
        email_subject = "Your email subject"
        email_body = f"Your email template with {prospect['name']} and {prospect['company']} placeholders"

       

if __name__ == "__main__":
    main()
