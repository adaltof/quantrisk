from flask import Flask, render_template, jsonify
from models import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def template_test():
    return render_template('template.html', my_string='Teste 123')

@app.route('/users')
def list_users():
    users = User.objects()
    users_print = []
    if len(users) == 0:
        User(name='adam', email='test@test.com').save()
    for user in users:
        users_print.append(user.name)
    print(users)

    return render_template('users.html', users=users_print)

if __name__ == '__main__':
    app.run(debug=True)
