# RINL Employee Verification & ID Card Management System

A full-stack web application designed to streamline employee registration, safety compliance verification, document validation, and digital ID generation for industrial plant access.

This system simulates a real-world industrial onboarding workflow where employees must review safety protocols, complete an assessment, register their details, upload required documents, and undergo verification before access approval.

---

## 🚀 Key Features

- Multi-step employee onboarding workflow
- Industrial safety guidelines (Do’s & Don’ts module)
- Safety assessment test (MCQ-based validation)
- Employee registration with form validation
- Secure document upload and storage using MongoDB GridFS
- Email-based applicant tracking
- Dynamic verification and ID card generation
- Structured REST-based backend using Flask

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- Flask-CORS
- PyMongo
- GridFS

**Database**
- MongoDB

**Frontend**
- HTML5
- CSS3
- JavaScript (Vanilla JS)

**Version Control**
- Git
- GitHub

---

## 🏗 System Architecture

Client (HTML/CSS/JS)  
⬇  
Flask Backend (REST APIs)  
⬇  
MongoDB Database  
⬇  
GridFS (File Storage for Documents)

---

## 📂 Project Structure

```
project/
├── backend/
│   └── app.py
├── frontend/
│   ├── sec1.html
│   ├── sec2.html
│   ├── sec3.html
│   ├── sec4.html
│   ├── sec5.html
│   ├── sec6.html
│   ├── styles.css
│   └── app.js
├── README.md
```

---

## ⚙️ Backend Setup

### 1️⃣ Install Dependencies

```bash
pip install flask flask-cors pymongo
```

### 2️⃣ Start MongoDB

Ensure MongoDB is running locally on default port (27017).

### 3️⃣ Run Backend Server

```bash
cd backend
python app.py
```

Backend will run at:

```
http://127.0.0.1:5000

```

---

## 🌐 Frontend Setup

No build tools required.

Simply open:

```
frontend/sec1.html
```

in your browser.

⚠️ Ensure backend is running before using the frontend.

---

## 🔄 Application Workflow

1. **Introduction Page**
2. **Safety Guidelines (Do’s & Don’ts)**
3. **Safety Assessment Test**
4. **Employee Registration**
5. **Document Upload**
6. **Verification & ID Generation**

---

## 📌 Core Functionalities Implemented

- REST API design using Flask
- Frontend-backend communication using fetch API
- File upload handling and storage via MongoDB GridFS
- Session-based email tracking
- Client-side and server-side validation
- Structured multi-page workflow system

---

## 🎯 Learning Outcomes

- Built a full-stack web application from scratch
- Implemented database connectivity and file storage
- Designed structured API endpoints
- Applied modular frontend-backend separation
- Practiced version control using Git and GitHub
- Understood real-world industrial workflow simulation

---

## 🔗 Project Repository

Add your GitHub link here:

```
https://github.com/chathurya244/rinl-employee-verification
```


## 📌 Future Enhancements

- Role-based authentication system
- Admin dashboard for verification approval
- Email notification integration
- Deployment using Render / Railway / Docker
- Production-grade WSGI server integration

---

## 👨‍💻 Author

ERRA CHATHURYA SAI  
B.Tech Student  
Full-Stack Development Enthusiast