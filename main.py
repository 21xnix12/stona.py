from flask import Flask
import random  
import string
app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

facts_list = [
    "Elon Musk twierdzi, że sieci społecznościowe zostały zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
    "Według badania przeprowadzonego w 2018 r. ponad 50% osób w wieku od 18 do 34 lat uważa, że jest zależnych od swoich smartfonów.",
    "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi.",
    "Badanie uzależnień technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych."
]

@app.route("/")
def przywitanie():
    return '<h1>Cześć! Na tej stronie możesz dowiedzieć się kilku ciekawostek na temat zależności technologicznych! <a href="/random_fack">Zobacz losowy fakt</a></h1><h1>Witamy w Generatorze Haseł</h1><p><a href="/generate_password">Kliknij tutaj, aby wygenerować hasło</a></p>'

@app.route("/random_fack")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/generate_password")
def generate_password_route():
    password = generate_password()
    return f'<h2>Twoje losowe hasło to:</h2><p>{password}</p><p><a href="/">Wróć na stronę główną</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
