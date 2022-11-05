from flask import Blueprint, render_template


blueprint = Blueprint('pugs', __name__)


@blueprint.route('/pugs')
def pugs():
    return render_template('pugs.html', pugs=['Potato', 'Lulu', 'Winston'])
