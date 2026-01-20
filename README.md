# anamika
Python chatbot project deployed on Render
# Anamika 🤖

Python chatbot project deployed on Render.

## Features
- FastAPI backend
- Cloud deployment
- Future APK & UI support

## Run locally
```bash
uvicorn main:app --reload

---

## ☁️ STEP 5 — Render पर Deploy (सबसे important)

अब Render वाला हिस्सा आता है 🔥

### Render Dashboard में जाएँ
1. https://render.com
2. **New +** → **Web Service**
3. **Connect GitHub**
4. Repository चुनें:  
   👉 `hani7248390 / anamika`

---

### Render settings ऐसे रखें 👇

| Setting | Value |
|------|------|
| Runtime | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port 10000` |
| Port | 10000 |

👉 **Create Web Service**

---

## 🚀 STEP 6 — Test करना

Deploy complete होने के बाद Render आपको एक URL देगा, जैसे:
