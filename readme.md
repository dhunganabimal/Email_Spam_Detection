


# 📧 Email Spam Detection System (FastAPI + ML)

A full-stack machine learning project that detects whether an email is **SPAM** or **HAM (Safe)** using a trained ML model served through **FastAPI**, with a  frontend UI built using HTML, CSS, and JavaScript.

---

##  Features

-  Machine-learning based spam classification  
-  FastAPI backend for fast inference  
 
- Confidence score for each prediction  
 
-  CORS-enabled for frontend access  

---

##  Project Structure

```

email-spam-detection/
│
├── email_spam.ipynb        # Jupyter notebook (model training & experimentation)
├── model.py           # Model loading and prediction logic
├── main.py                 # FastAPI backend
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # Trained text vectorizer
│
├── frontend/
│   ├── index.html          # Frontend UI
│   ├── style.css           # Advanced CSS styling
│   └── script.js           # API integration logic
│
└── README.md               # Project documentation

````

---

## Machine Learning Overview

### Features Used
- Sender email length  
- Capital letters count in subject  
- TF-IDF text features from email body  
- Combined metadata + textual features  

### Model Output
- **SPAM** or **HAM (Safe)**
- Confidence score (probability of spam)

---

##  Technology Stack

### Backend
- Python  
- FastAPI  
- Scikit-learn  
- Pandas  

### Frontend
- HTML5  
- CSS3  
- JavaScript (Fetch API)

---

##  Installation & Setup

### 1 Clone the Repository
```bash
git clone https://github.com/your-username/email-spam-detector.git
cd email-spam-detector
````

---

### 2 Install Backend Dependencies

```bash
pip install fastapi uvicorn pandas scikit-learn
```

---

### 3 Start FastAPI Server

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 4 Run Frontend Server

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://127.0.0.1:5500
```

---

##  API Usage

### Endpoint

```
POST /predict
```

### Request Body

```json
{
  "sender": "unknown@weird-domain.net",
  "subject": "YOU HAVE WON A PRIZE",
  "body": "Click here to claim your prize money"
}
```

### Response

```json
{
  "result": "SPAM",
  "confidence": 0.97
}
```

---



## CORS Configuration

CORS middleware is enabled in FastAPI to allow all frontend communication:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

