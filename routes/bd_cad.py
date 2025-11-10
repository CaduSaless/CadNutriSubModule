from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from database.cadastro import user
from static.functions import to_dict_user, get_db_connection

bd_bp = Blueprint('bd', __name__)
nomes = ['Código','Nome', 'CPF', 'Raça', 'Gênero', 'Escolaridade', 'Email', 'Data de Nascimento']

@bd_bp.route('/')
def bd_home():
    return render_template('home-bd.html')

@bd_bp.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    try:
        db = get_db_connection()
        if not db:
            return {"message": "Erro ao conectar ao Banco de dados"}
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM Pessoa WHERE id_Pessoa = {data['codigo']}")
        cursor.execute(f"DELETE FROM Etnia_Pessoa WHERE id_Pessoa = {data['codigo']}")
        db.commit()
        db.close()
    except Exception as e:
        return {"message": f"Erro ao deletar usuário, {e}"}
        
    return {'ok': 'ok'}

@bd_bp.route('/content')
def content():
    try:
        db = get_db_connection()
        if not db:
            return {"message": "Erro ao conectar ao Banco de dados"}
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM Pessoa")
        cad = cursor.fetchall()
        db.close()
    except Exception as e:
        return {"message": f"Erro ao carregar conteúdo, {e} "}

    return render_template('itens-table.html', cad= cad)

@bd_bp.route('/get_user/<cod>')
def details(cod):
    data = to_dict_user(cod)
    return render_template('detail.html', dados=data)

@bd_bp.before_request
def authentication():
    if not 'email' in session:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    if session['email'] != user['email'] or session['senha'] != user['senha']:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    
