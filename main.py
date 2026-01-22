from flask import Flask, request, redirect, url_for

from admission_agent import get_admission_info
from fee_agent import get_fee_info
from placement_agent import get_placement_info
from student_agent import get_student_details

app = Flask(__name__)

# simple in-memory user store (hackathon purpose)
users = {"student": "1234"}

# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect(url_for("home"))
        else:
            return "<h3 style='color:red;text-align:center;'>Invalid username or password</h3>"

    return """
    <html>
    <head>
        <title>Login</title>
        <style>
            body { background:black; font-family: Arial; }
            .box {
                width:320px; margin:120px auto;
                background:#111; padding:25px;
                border-radius:10px; text-align:center;
                box-shadow:0 0 10px red;
                color:white;
            }
            input, button {
                width:90%; padding:10px; margin:8px;
            }
            button {
                background:red; color:white; border:none;
                cursor:pointer;
            }
            a { color:red; text-decoration:none; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Student Login</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
            <p><a href="/register">Create Account</a></p>
        </div>
    </body>
    </html>
    """

# ---------------- REGISTER PAGE ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("login"))

    return """
    <html>
    <head>
        <title>Create Account</title>
        <style>
            body { background:black; font-family: Arial; }
            .box {
                width:320px; margin:120px auto;
                background:#111; padding:25px;
                border-radius:10px; text-align:center;
                box-shadow:0 0 10px red;
                color:white;
            }
            input, button {
                width:90%; padding:10px; margin:8px;
            }
            button {
                background:red; color:white; border:none;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Create Account</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Register</button>
            </form>
        </div>
    </body>
    </html>
    """

# ---------------- HOME PAGE ----------------
@app.route("/home")
def home():
    return """
    <html>
    <head>
        <title>MAS Home</title>
        <style>
            body { background:black; color:white; font-family: Arial; }
            .container {
                display:flex; justify-content:center;
                gap:20px; margin-top:50px;
            }
            .card {
                background:#111; width:260px;
                padding:20px; border-radius:10px;
                box-shadow:0 0 10px red;
                text-align:center;
            }
            button {
                background:red; color:white;
                border:none; padding:10px;
                width:100%; cursor:pointer;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align:center;">Multi-Agent College System</h1>
        <div class="container">
            <div class="card">
                <h3>Admission Agent</h3>
                <a href="/student"><button>View Details</button></a>
            </div>
            <div class="card">
                <h3>Fees Agent</h3>
                <a href="/student"><button>View Details</button></a>
            </div>
            <div class="card">
                <h3>Placement Agent</h3>
                <a href="/student"><button>View Details</button></a>
            </div>
        </div>
    </body>
    </html>
    """

# ---------------- STUDENT DETAILS ----------------
@app.route("/student")
def student():
    student = get_student_details()
    admission = get_admission_info()
    placement = get_placement_info()

    return f"""
    <html>
    <head>
        <title>Student Details</title>
        <style>
            body {{ background:black; color:white; font-family: Arial; }}
            .box {{
                background:#111; max-width:500px;
                margin:80px auto; padding:25px;
                border-radius:10px;
                box-shadow:0 0 10px red;
            }}
            button {{
                background:red; color:white;
                border:none; padding:10px;
                width:100%; cursor:pointer;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Student Information</h2>
            <p><b>Name:</b> {student['name']}</p>
            <p><b>Department:</b> {student['department']}</p>
            <p><b>Marks:</b> {student['marks']}%</p>
            <p><b>Eligibility:</b> {admission['eligibility']}</p>
            <p><b>Fees:</b> ₹60,000</p>
            <p><b>Placement:</b> {placement['average_package']}</p>
            <a href="/pay"><button>Pay Now</button></a>
        </div>
    </body>
    </html>
    """

# ---------------- PAYMENT PAGE ----------------
@app.route("/pay")
def pay():
    return """
    <html>
    <head>
        <title>Payment</title>
        <style>
            body {
                background:black; color:white;
                font-family: Arial; text-align:center;
                padding-top:120px;
            }
            .box {
                background:#111; width:350px;
                margin:auto; padding:30px;
                border-radius:10px;
                box-shadow:0 0 10px red;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Payment Successful</h2>
            <p>Fees payment completed.</p>
            <p>Status: Confirmed</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
 