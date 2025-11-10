from flask import Blueprint, session, request, redirect, url_for, flash
from database.cadastro import user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['POST'])
def auth():
    session.clear()
    email = request.form.get('email')
    senha = request.form.get('senha')
    if email == user['email'] and senha == user['senha']:
        session['email'] = email
        session['senha'] = senha
        return redirect(url_for('cadastro.homepage_cad'))
    flash('Login inválido')
    return redirect(url_for('homepage'))

@auth_bp.route('/logout')
def logout():
    session.pop('email')
    session.pop('senha')
    print(session)
    return redirect('/')