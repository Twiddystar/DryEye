from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>🩺 Dry Eye Questionnaire</title></head>
        <body>
            <h1>Benvenuto!</h1>
            <p>Questa è l'applicazione per il questionario dell'occhio secco.</p>
            <p>Visita <a href='/docs'>/docs</a> per accedere alla documentazione delle API.</p>
        </body>
    </html>
    """
