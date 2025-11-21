

# 🚀 AI-Assisted CI/CD Pipeline

**A fully automated CI/CD system powered by Python, Docker, GitHub Actions, and an AI Code Review Step.**

![CI Status](https://img.shields.io/github/actions/workflow/status/ROHIT7773TRX/ai-assisted-cicd/ci.yml?label=CI%20Build\&style=for-the-badge)
![Docker Pulls](https://img.shields.io/docker/pulls/rohitpoonia/ai-assisted-cicd?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge)

---

## 📌 **Project Overview**

This project demonstrates a **modern CI/CD pipeline** integrating:

* **Automated Testing** using Pytest
* **AI-Powered Static Code Review**
* **Docker Image Build & Push**
* **GitHub Actions CI Pipeline**
* **Containerized Python Application**

It is designed as a **portfolio-ready project** that shows your ability to combine software engineering, automation, DevOps, and AI tools.

---

## 🧠 **Key Features**

✔ Automated testing on every push
✔ AI-assisted review step inside CI
✔ Dockerized Python application
✔ Docker image automatically pushed to Docker Hub
✔ Clear, production-style folder structure
✔ Ready for CD integration (Render/Railway/AWS)

---

## 📁 **Project Structure**

```
ai-assisted-cicd/
├── ai/
│   └── analyze_code.py     # AI-based static analysis
├── src/
│   └── app.py              # Main application
├── tests/
│   └── test_app.py         # Test cases
├── Dockerfile              # Build container image
├── requirements.txt        # Python dependencies
├── .github/workflows/
│   └── ci.yml              # CI pipeline
└── README.md               # Documentation
```

---

## 🚀 **How It Works**

### **1️⃣ Push Code to GitHub**

Triggers the CI pipeline automatically.

### **2️⃣ GitHub Actions Pipeline Runs**

* Install dependencies
* Run pytest
* Perform AI code review
* Build Docker image
* Push to Docker Hub

### **3️⃣ Docker Image Published**

Image name used:

```
docker pull rohitpoonia/ai-assisted-cicd:latest
```

You can run it locally:

```
docker run -it rohitpoonia/ai-assisted-cicd:latest
```

---

## 🧪 **Run Tests Locally**

```
pytest
```

---

## 🐳 **Build & Run with Docker**

### Build:

```
docker build -t ai-assisted-cicd .
```

### Run:

```
docker run -it ai-assisted-cicd
```

---

## 🤖 **AI Code Review**

The file `ai/analyze_code.py` runs basic AI/static checks on your code, and it is integrated into GitHub Actions:

```
python ai/analyze_code.py
```

You can extend it later to use OpenAI API or HuggingFace.

---

## 🌍 **Deployment**

Currently deployed via **Docker Hub image**.

You can deploy the image on:

* Render
* Railway
* AWS ECS / ECR
* Azure Container Apps
* Google Cloud Run


## 📬 Contact

Created by **Rohit Poonia**
GitHub: `ROHIT7773TRX`
Docker Hub: `rohitpoonia`

