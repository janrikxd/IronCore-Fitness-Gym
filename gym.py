import os
from flask import Flask, render_template, request
from db_config import create_connection
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")

@app.route("/members")
def members_list():
    search_query = request.args.get('search', '')
    conn = create_connection()
    if not conn:
        return "Database Connection Error", 500

    cursor = conn.cursor(dictionary=True)

    if search_query:
        query = "SELECT * FROM gym_members WHERE full_name LIKE %s OR email LIKE %s"
        cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
    else:
        cursor.execute("SELECT * FROM gym_members ORDER BY expiration_date ASC")

    members = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template(
        "members_list.html",
        members=members,
        search_query=search_query,
        today=datetime.now().date()
    )

@app.route("/submit_membership", methods=["POST"])
def submit_membership():
    full_name = request.form["full_name"]
    email = request.form["email"]
    membership_type = request.form["membership_type"]
    start_date = request.form["start_date"]

    conn = create_connection()
    if not conn:
        return "Database Connection Error", 500

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gym_members WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return render_template("membership.html", error="Email na ginamit ay rehistrado na!")

    start = datetime.strptime(start_date, "%Y-%m-%d")
    if membership_type == "Monthly":
        expiration_date = start + timedelta(days=30)
    elif membership_type == "Quarterly":
        expiration_date = start + timedelta(days=90)
    else:
        expiration_date = start + timedelta(days=365)

    final_expiry = expiration_date.date()
    cursor.execute("""
        INSERT INTO gym_members
        (full_name, email, membership_type, start_date, expiration_date, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        full_name, email, membership_type, start_date, final_expiry, "Active"
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return render_template(
        "confirmation.html",
        full_name=full_name,
        email=email,
        membership_type=membership_type,
        start_date=start_date,
        expiration_date=final_expiry
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
