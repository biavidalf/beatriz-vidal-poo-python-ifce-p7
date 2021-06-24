from app import app
from app.models.cliente import Cliente
from flask import render_template, url_for, redirect, flash
from app.models.formulario import LoginForm, RegisterForm, AttForm


c1 = Cliente("Beatriz", "1234", "bia@gmail", "123")
clientes = [c1]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for x in clientes:
            if x.get_email() == form.email.data:
                if x.get_senha() == form.senha.data:
                    return redirect(url_for('clientes'))
                else:
                    flash('Senha incorreta.')
            else:
                flash('Email não cadastrado.')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        for x in clientes:
            if x.get_email() == form.email.data:
                flash('Email já em uso, insira um e-mail válido')
            else:
                nome = str(form.nome.data)
                senha = str(form.senha.data)
                email = str(form.email.data)
                cnpjcpf = str(form.cnpjcpf.data)
                user = Cliente(nome, senha, email, cnpjcpf)
                clientes.append(user)
                print(clientes)
                return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/clientes')
def clientes():
    return render_template('clientes.html', client=clientes)


@app.route('/logatualizar')
def logatualizar():
    form = LoginForm()
    if form.validate_on_submit():
        for x in clientes:
            if x.get_email() == form.email.data:
                if x.get_senha() == form.senha.data:
                    return redirect(url_for('atualizar'))
                else:
                    flash('Senha incorreta.')
            else:
                flash('Email não cadastrado.')
    return render_template('login.html', form=form)


@app.route('/atualizar')
def atualizar():
    form = AttForm()
    if form.validate_on_submit():
        for x in clientes:
            if x.get_email() == form.antigo.data:
                x.set_email(form.novo.data)
            elif x.get_senha() == form.antigo.data:
                x.set_senha(form.novo.data)
            elif x.get_nome() == form.antigo.data:
                x.set_nome(form.novo.data)
            elif x.get_cnpjcpf() == form.antigo.data:
                x.set_cnpjcpf(form.novo.data)
            else:
                flash('Campo inválido.')
    return render_template('att.html', form=form)


@app.route('/deletar')
def deletar():
    form = LoginForm()
    if form.validate_on_submit():
        for x in clientes:
            if x.get_email() == form.email.data:
                if x.get_senha() == form.senha.data:
                    clientes.remove(x)
                else:
                    flash('Senha incorreta.')
            else:
                flash('Email não cadastrado.')
    return render_template('del.html', form=form)

