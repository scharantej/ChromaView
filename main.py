
# Import necessary modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Define 'colors' table
class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color_name = db.Column(db.String(80), unique=True, nullable=False)
    hue = db.Column(db.Integer, nullable=False)
    hex_code = db.Column(db.String(7), unique=True, nullable=False)

    def __repr__(self):
        return '<Color %r>' % self.color_name

# Create database tables
db.create_all()

# Home page route
@app.route('/')
def index():
    """Render home page with list of colors."""
    colors = Color.query.all()
    return render_template('index.html', colors=colors)

# Individual color page route
@app.route('/color/<color_name>')
def color(color_name):
    """Render individual color page."""
    color = Color.query.filter_by(color_name=color_name).first()
    return render_template('color.html', color=color)

# About page route
@app.route('/about')
def about():
    """Render about page."""
    return render_template('about.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
