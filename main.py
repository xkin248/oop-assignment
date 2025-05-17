from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from Flask on Azure!"

@app.route("/test")
def test():
    return "🚀 Flask is working perfectly!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # Azure uses PORT env var
    app.run(host="0.0.0.0", port=port)
