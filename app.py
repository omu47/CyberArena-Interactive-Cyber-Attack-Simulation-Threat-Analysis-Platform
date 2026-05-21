import os
from flask import Flask, render_template, request
from modules.base64_lab import decode_base64
from modules.report_generator import generate_report
from modules.rsa_demo import encrypt_message
app = Flask(__name__)
from modules.threat_analyzer import analyze_message
from modules.steg_detector import (
    extract_hidden_message,
    extract_metadata
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']

        password = generate_password_hash(
            request.form['password']
        )

        user = User(
            username=username,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect('/login')

    return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        user = User.query.filter_by(
            username=username
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect('/')

    return render_template('login.html')
@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/login')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/base64', methods=['GET', 'POST'])
def base64_lab():
    decoded_text = None

    if request.method == 'POST':
        encoded_text = request.form['encoded_text']
        decoded_text = decode_base64(encoded_text)

    if current_user.is_authenticated:

        current_user.xp += 10

        if current_user.xp >= 100:
            current_user.rank = "Cyber Specialist"

        db.session.commit()

    return render_template(
        'base64_lab.html',
        decoded_text=decoded_text
    )

@app.route('/rsa', methods=['GET', 'POST'])
def rsa_lab():

    encrypted = None

    if request.method == 'POST':

        message = request.form['message']

        encrypted = encrypt_message(message)

    return render_template(
        'rsa_lab.html',
        encrypted=encrypted
    )
@app.route('/steganography', methods=['GET', 'POST'])
def steganography_lab():

    hidden_message = None
    metadata = {}

    if request.method == 'POST':

        image = request.files['image']

        image_path = os.path.join(
            'static/uploads',
            image.filename
        )

        image.save(image_path)

        hidden_message = extract_hidden_message(image_path)

        metadata = extract_metadata(image_path)

    return render_template(
        'steganography.html',
        hidden_message=hidden_message,
        metadata=metadata
    )
@app.route('/phishing', methods=['GET', 'POST'])
def phishing_simulator():

    warning = None

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        otp = request.form['otp']

        warning = """
        WARNING:
        This was a phishing simulation.

        Attackers often impersonate security systems
        to steal credentials and OTPs using urgency
        and trust manipulation.
        """

    return render_template(
        'phishing.html',
        warning=warning
    )
@app.route('/threat-map')
def threat_map():

    return render_template('threat_map.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyberarena.db'

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )

    xp = db.Column(
        db.Integer,
        default=0
    )

    rank = db.Column(
        db.String(50),
        default="Beginner"
    )
@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))

@app.route('/ai-analyzer', methods=['GET', 'POST'])
def ai_analyzer():

    result = None

    if request.method == 'POST':

        message = request.form['message']

        result = analyze_message(message)
        report_path = generate_report(
        current_user.username if current_user.is_authenticated else "guest",
        result['risk'],
        result['score']
)
    return render_template(
    'ai_analyzer.html',
    result=result,
    report_path=report_path
)
@app.route('/leaderboard')
def leaderboard():

    users = User.query.order_by(
        User.xp.desc()
    ).all()

    return render_template(
        'leaderboard.html',
        users=users
    )
if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)