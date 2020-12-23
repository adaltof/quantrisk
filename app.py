from flask import Flask, render_template, jsonify
from models import User, ThreatCommunity

app = Flask(__name__)


@app.route('/')
def initial_page():
    # Get Total Users
    usercount = User.objects.count()
    threatcount = ThreatCommunity.objects.count()
    return render_template('index.html', usercount=usercount, threatcount=threatcount)


@app.route('/user')
def list_users():
    users = User.objects()
    users_print = []
    if len(users) == 0:
        User(name='adam', email='test@test.com').save()
    for user in users:
        users_print.append(user.name)
    print(users)

    return render_template('users.html', users=users_print)

@app.route('/user/<user>')
def user_page(user):
    user = User.objects(name=user).first()
    return render_template('user.html', user=user)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
