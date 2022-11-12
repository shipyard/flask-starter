from flask import Blueprint, render_template


blueprint = Blueprint('pugs', __name__)


@blueprint.route('/pugs')
def pugs():
    pugs = ['Potato', 'Lulu', 'Winston', 'El Puggio', 'Kjartan the Pugnacious', 'Velma the Pugess']
    return render_template('pugs.html', pugs=pugs)
