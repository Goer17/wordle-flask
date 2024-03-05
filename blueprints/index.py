import random
from enum import Enum
from flask import Blueprint, render_template, session, request

from game import Game
from models import User
from exts import db
from utils.pop_up import ShortInfo, Wind

bp = Blueprint('index', __name__, url_prefix='/')

game = Game()
ans = random.choice(game.valid_answers)

class Color(Enum):
    WHITE = "#ffffff"
    GREEN = "#90ee90"
    YELLOW = "#dffb3f"
    GRAY = "#d3d3d3"

def init_dat() -> dict:
    return {
        "grid_color" : [[Color.WHITE] * 5 for _ in range(6)],
        "rec" : [[''] * 5 for _ in range(6)],
        "keyboard" : [
            [[ch, Color.WHITE] for ch in row] for row in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ],
        "focus": 0
    }

dat = init_dat()

pos = {}
for i in range(len(dat['keyboard'])):
    for j in range(len(dat['keyboard'][i])):
        pos[dat['keyboard'][i][j][0]] = (i, j)

@bp.route('/', methods = ['GET', 'POST'])
def index():
    global ans, dat
    short_info = None
    wind = None
    uid = session.get('uid')
    username = session.get('username')
    if request.method == 'POST':
        focus = dat['focus']
        guess = []
        for j in range(len(dat['rec'][0])):
            letter = request.form.get(f'cell-{focus}-{j}')
            if letter:
                guess.append(letter)
        if len(guess) == 5:
            guess = ''.join(guess).lower()
            if game.word_dict.is_word(guess):
                grid_color = dat['grid_color']
                rec = dat['rec']
                keyboard = dat['keyboard']
                for j in range(len(guess)):
                    rec[focus][j] = guess[j]
                    x, y = pos[guess[j]]
                    if guess[j] == ans[j]:
                        grid_color[focus][j] = Color.GREEN
                        keyboard[x][y][1] = Color.GREEN
                    elif guess[j] in ans:
                        grid_color[focus][j] = Color.YELLOW
                        if not keyboard[i][j][1] == Color.GREEN:
                            keyboard[x][y][1] = Color.YELLOW
                    else:
                        grid_color[focus][j] = Color.GRAY
                        keyboard[x][y][1] = Color.GRAY
                dat['focus'] += 1
                if guess == ans:
                    wind = Wind(
                        info='Congratulation! You have got the correct answer!',
                        close_text='Try again!'
                    )
                    # Update the database
                    user = db.session.get(User, uid)
                    user.try_times += 1
                    user.solved_number += 1
                    user.total_guess_times += dat['focus']
                    db.session.commit()
                    # Recover
                    dat = init_dat()
                    ans = random.choice(game.valid_answers)
            else:
                short_info = ShortInfo(info='Your guess is not a word!')
        else:
            short_info = ShortInfo(info='Your guess should be consist of 5 letters!')
        if dat['focus'] >= 6:
            wind = Wind(
                info=f'Correct answer: {ans}',
                close_text='Try again!'
            )
            # Recover
            dat = init_dat()
            ans = random.choice(game.valid_answers)
            # Update the database
            user = db.session.get(User, uid)
            user.try_times += 1
            db.session.commit()
        
    return render_template('index.html',
                               uid=uid,
                               username=username,
                               short_info=short_info,
                               wind=wind,
                               **dat)