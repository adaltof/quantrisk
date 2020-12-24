from flask import Flask, render_template, request
from models import User, ThreatCommunity, Analysis
from forms import ThreatForm, AnalysisForm
import json

app = Flask(__name__)


@app.route('/')
def initial_page():
    # Get Total Users
    usercount = User.objects.count()
    threatcount = ThreatCommunity.objects.count()
    analysiscount = Analysis.objects.count()
    return render_template('index.html', usercount=usercount, threatcount=threatcount, analysiscount=analysiscount)


@app.route('/user')
def list_users():
    users = User.objects().to_json()
    users_json = json.loads(users)
    return render_template('users.html', users=users_json)

@app.route('/user/<user>')
def user_page(user):
    user = User.objects(name=user).first()
    return render_template('user.html', user=user)


@app.route('/threat', methods=['GET', 'POST'])
def list_threats():
    form = ThreatForm(request.form)
    message = ''
    if request.method == 'POST':
        if form.validate():
            threat = ThreatCommunity(name=form.name.data, description=form.data['description'],tcapmin=form.data['tcapmin'],
                                     tcapavg=form.data['tcapavg'], tcapmax=form.data['tcapmax'])
            #Check existing
            threatcheck = ThreatCommunity.objects(name=threat.name)
            if threatcheck is not None:
                threat.save()
                message = 'Threat community added successfully.'
            else:
                message = 'Threat community updated successfully'
        else:
            message = 'We could not add the new Threat Community as requested.'
    # Get all list
    threats = ThreatCommunity.objects().to_json()
    threats_json = json.loads(threats)
    return render_template('threats.html', threats=threats_json, form=form, message=message)


@app.route('/threat/<threat>')
def threat_page(threat):
    form = ThreatForm(request.form)
    message = ''
    threat = ThreatCommunity.objects(name=threat).first()
    if threat:
        form.name.render_kw = {'value' : threat.name, 'disabled':''}
        form.description.render_kw = {'value': threat.description}
        form.description.render_kw = {'value': threat.description}
        form.description.render_kw = {'value': threat.description}
        form.description.render_kw = {'value': threat.description}
    return render_template('threat.html', threat=threat, form=form, message=message)

@app.route('/analysis')
def list_analysis():
    analysis = Analysis.objects().to_json()
    analysis_json = json.loads(analysis)
    return render_template('analysis.html', users=analysis_json)


@app.route('/analysisnew', methods=['GET', 'POST'])
def create_analysis():
    form = AnalysisForm(request.form)
    message = ''
    if request.method == 'POST':
        if form.validate():
            analysis = Analysis(name=form.name.data, description=form.data['description'])
            # Check existing
            analysischeck = Analysis.objects(name=analysis.name)
            if analysischeck is not None:
                analysis.save()
                message = 'Analyis added successfully successfully.'
                return redirect(url_for('list_analysis'))
        else:
            message = 'We could not add the Analysis as requested.'
            return render_template('newanalysis.html', form=form, message=message)
    # Get all list
    else:
        return render_template('newanalysis.html', form=form, message=message)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

@app.errorhandler(503)
def not_found_error(error):
    return render_template('page-503.html'), 503

if __name__ == '__main__':
    app.run(debug=True)
