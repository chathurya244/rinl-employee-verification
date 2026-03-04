from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import gridfs
import io

app = Flask(__name__)
CORS(app)

# ==============================
# MongoDB Connection
# ==============================
mongo_uri = "mongodb://127.0.0.1:27017/job_application"
client = MongoClient(mongo_uri)
db = client.job_application
fs = gridfs.GridFS(db)
applicants = db.applicants

# ==============================
# ADMIN LOGIN
# ==============================
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if data.get("username") == ADMIN_USERNAME and data.get("password") == ADMIN_PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/admin/applicants', methods=['GET'])
def get_applicants():
    data = list(applicants.find({}, {'_id': 0}))
    return jsonify(data), 200


# ==============================
# REGISTER USER
# ==============================
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.form

        applicant = {
            "name": data.get("name"),
            "father_name": data.get("father-name"),
            "gender": data.get("gender"),
            "age": int(data.get("age")) if data.get("age") else None,
            "dob": data.get("dob"),
            "state": data.get("state"),
            "qualification": data.get("qualification"),
            "phone": data.get("phone"),
            "email": data.get("email"),
            "address": data.get("address"),
            "department": data.get("department"),
        }

        applicants.insert_one(applicant)

        print("Form saved successfully")

        # pass email to next page
        return redirect(url_for("safety_page", email=data.get("email")))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==============================
# DOCUMENT UPLOAD + ID CARD
# ==============================
@app.route('/upload', methods=['POST'])
def upload():

    email = request.form.get("email")

    if not email:
        return "Email missing"

    uploaded = {}

    # save files
    for field in ["aadhaar", "pan", "photo", "certificate", "resume"]:
        file = request.files.get(field)
        if file:
            file_id = fs.put(file.read(), filename=file.filename)
            uploaded[field] = str(file_id)

    # update DB
    applicants.update_one(
        {"email": email},
        {"$set": {"documents": uploaded}}
    )

    # fetch user
    user = applicants.find_one({"email": email})

    if not user:
        return "User not found"

    emp_id = str(user["_id"])[-6:]

    return render_template(
        "sec6.html",
        name=user.get("name"),
        employee_id=emp_id,
        department=user.get("department"),
        email=user.get("email"),
        photo_url="/get_photo/" + uploaded.get("photo", "")
    )


@app.route('/get_photo/<file_id>')
def get_photo(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(io.BytesIO(file.read()), mimetype='image/jpeg')
    except:
        return "Photo not found"


# ==============================
# PAGE ROUTES
# ==============================

@app.route('/')
def home():
    return render_template("sec1.html")


@app.route('/admin')
def admin_page():
    return render_template("admin.html")


@app.route('/registerpage')
def register_page():
    return render_template("sec2.html")


@app.route('/safety')
def safety_page():
    email = request.args.get("email")
    return render_template("sec3.html", email=email)


@app.route('/mcq')
def mcq_page():
    email = request.args.get("email")
    return render_template("sec4.html", email=email)


@app.route('/uploadpage')
def upload_page():
    email = request.args.get("email")
    return render_template("sec5.html", email=email)

@app.route('/download_id')
def download_id():
    email = request.args.get("email")

    if not email:
        return "Email missing"
    
    user = applicants.find_one({"email": email})
    if not user:
        return "User not found"
    
    emp_id = str(user["_id"])[-6:]

    return render_template(
        "sec6.html",
        name=user.get("name"),
        employee_id=emp_id,
        department=user.get("department"),
        email=user.get("email"),
        photo_url="/get_photo/"+ user.get("documents", {}).get("photo", "")
    )
# ==============================
# RUN SERVER
# ==============================
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    