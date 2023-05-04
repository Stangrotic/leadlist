from flask import Flask, render_template, request, redirect, url_for
import json
import requests
from google.oauth2.credentials import Credentials
from table import get_all_prospects_from_database, get_prospect_by_id_from_database, update_email_status

app = Flask(__name__)

@app.route("/")
def index():
    # Load prospects from the database (use the function you wrote earlier)
    prospects = get_all_prospects_from_database()
    print(prospects)  # Add this line to print the prospects variable

    return render_template("index.html", prospects=prospects)



# ... Rest of your code

if __name__ == "__main__":
    app.run(debug=True)

# Define the get_signalhire_data function here (moved from previous answer)
def get_signalhire_data(api_key):
    url = "https://api.signalhire.com/v3/search"
    headers = {"Authorization": f"Bearer {api_key}"}

    params = {
        "q": "founder OR 'business development'",
        "industry": "internet"
    }

    response = requests.get(url, headers=headers, params=params)
    return response

from flask import Flask, render_template, request, redirect, url_for
import json
import requests
from google.oauth2.credentials import Credentials
from table import get_all_prospects_from_database, get_prospect_by_id_from_database, update_email_status

app = Flask(__name__)

def get_signalhire_data(api_key):
    url = "https://api.signalhire.com/v3/search"
    headers = {"Authorization": f"Bearer {api_key}"}

    params = {
        "q": "founder OR 'business development'",
        "industry": "internet"
    }

    response = requests.get(url, headers=headers, params=params)
    return response

@app.route("/")
def index():
    # Load prospects from the database (use the function you wrote earlier)
    prospects = get_all_prospects_from_database()

    return render_template("index.html", prospects=prospects)

@app.route("/send_email", methods=["POST"])
def send_email_to_prospect():
    prospect_id = request.form["prospect_id"]

    # Load prospect from the database (use the function you wrote earlier)
    prospect = get_prospect_by_id_from_database(prospect_id)

    # Send email to the prospect (use the function you wrote earlier)
    email_credentials = Credentials.from_authorized_user_file("client_secret_381200326445-u8h915n3avt28s0c0iokobsjf2v67c4k.apps.googleusercontent.com.json")
    email_subject = "Your email subject"
    email_body = f"Your email template with {prospect['name']} and {prospect['company']} placeholders"
  

    # Update the email status in the database (use the function you wrote earlier)
    update_email_status(prospect["email"], "sent")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)




email_credentials = Credentials.from_authorized_user_file("client_secret_381200326445-u8h915n3avt28s0c0iokobsjf2v67c4k.apps.googleusercontent.com.json")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
