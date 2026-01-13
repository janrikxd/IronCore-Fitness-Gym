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

@app.route("/submit_membership", methods=["POST"])
def submit_membership():
    full_name = request.form["full_name"]
    email = request.form["email"]
    membership_type = request.form["membership_type"]
    start_date = request.form["start_date"]

    conn = create_connection()
    cursor = conn.cursor()

    # SPECIAL FEATURE: Prevent duplicate email
    cursor.execute("SELECT * FROM gym_members WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return render_template("membership.html", error="Email already registered!")

    # SPECIAL FEATURE: Auto expiration date
    start = datetime.strptime(start_date, "%Y-%m-%d")

    if membership_type == "Monthly":
        expiration_date = start + timedelta(days=30)
    elif membership_type == "Quarterly":
        expiration_date = start + timedelta(days=90)
    else:
        expiration_date = start + timedelta(days=365)

    cursor.execute("""
        INSERT INTO gym_members
        (full_name, email, membership_type, start_date, expiration_date, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        full_name,
        email,
        membership_type,
        start_date,
        expiration_date.date(),
        "Active"
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
        expiration_date=expiration_date.date()
    )

if __name__ == "__main__":

    app.run(debug=True)

