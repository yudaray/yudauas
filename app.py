from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Prayuda Azisyamsizar Akbar Ray, Sistem Informasi, 2119113947"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
