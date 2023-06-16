
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Game state
game_in_progress = False
target_number = None
attempts = 0

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Start game route
@app.route('/start', methods=['POST'])
def start_game():
    global game_in_progress, target_number, attempts
    game_in_progress = True
    target_number = 42  # Change this to your desired target number
    attempts = 0
    return redirect('/play')

# Play game route
@app.route('/play', methods=['GET', 'POST'])
def play_game():
    global game_in_progress, attempts
    if not game_in_progress:
        return redirect('/')
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts += 1
        if guess == target_number:
            return render_template('win.html', attempts=attempts)
        elif guess < target_number:
            message = "Too low! Try again."
        else:
            message = "Too high! Try again."
        return render_template('play.html', message=message)
    
    return render_template('play.html', message='')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=8080)

