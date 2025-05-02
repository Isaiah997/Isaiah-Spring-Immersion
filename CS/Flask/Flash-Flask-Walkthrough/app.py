from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = "Alice"
    return render_template('home.html', name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
