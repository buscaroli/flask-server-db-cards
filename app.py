from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# select a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# initialise the database
db = SQLAlchemy(app)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"<Card {self.id}>"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        card_q = request.form["question"]
        card_a = request.form["answer"]
        new_card = Card(question=card_q, answer=card_a)

        try:
            db.session.add(new_card)
            db.session.commit()
            return redirect('/')
        except:
            return "Error adding your card."

    else:
        cards = Card.query.order_by(Card.created_at).all()
        return render_template('index.html', cards=cards)


@app.route('/delete/<int:id>')
def delete(id):
    card_to_delete = Card.query.get_or_404(id)

    try:
        db.session.delete(card_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting the card."


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    card = Card.query.get_or_404(id)
    if request.method == "POST":
        card.question = request.form["question"]
        card.answer = request.form["answer"]
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Errot updating the card."
    else:
        return render_template('update.html', card=card)


if __name__ == "__main__":
    app.run(debug=True)
