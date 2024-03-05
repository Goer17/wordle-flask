from flask import Blueprint, render_template, session, request

from exts import db
from models import User

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/rank')
def rank():
    rank_query = db.session.query(
        User.username,
        User.solved_number,
        (User.total_guess_times / User.solved_number).label('avg_guess')
    ).order_by(
        User.solved_number.desc(),
        (User.total_guess_times / User.solved_number)
    ).limit(50).all()
    
    uid = session.get('uid')
    if uid:
        user = db.session.get(User, uid)
        # TODO
    
    return render_template('user/rank.html', rank_query=rank_query)