from wtforms import Form, StringField, validators, IntegerField, DecimalField

class ThreatForm(Form):
    name = StringField('Threat Community Name', [ validators.DataRequired(), validators.Length(min=4, max=50)], render_kw={'placeholder': 'APTXX'})
    description = StringField('Description', [validators.Length(min=1, max=120)])
    tcapmin = IntegerField('TCAP Min', [validators.NumberRange(min=0, max=100)])
    tcapavg = IntegerField('TCAP Avg', [validators.NumberRange(min=0, max=100)])
    tcapmax = IntegerField('TCAP Max', [validators.NumberRange(min=0, max=100)])



class AnalysisForm(Form):
    name = StringField('Analysis Name', [validators.DataRequired(), validators.Length(min=4, max=50)], render_kw={'placeholder': 'analysis1'})
    description = StringField('Description', [validators.Length(min=1, max=120)])
    lefmin = DecimalField('LEF Min')
    lefavg = DecimalField('LEF Avg')
    lefmax = DecimalField('LEF Max')
    tefmin = DecimalField('TEF Min')
    tefavg = DecimalField('TEF Avg')
    tefmax = DecimalField('TEF Max')
    cfmin = DecimalField('CF Min')
    cfavg = DecimalField('CF Avg')
    cfmax = DecimalField('CF Max')
    tcapmin = IntegerField('TCAP Min', [validators.NumberRange(min=0, max=100)])
    tcapavg = IntegerField('TCAP Avg', [validators.NumberRange(min=0, max=100)])
    tcapmax = IntegerField('TCAP Max', [validators.NumberRange(min=0, max=100)])
    vulnmin = IntegerField('Vuln Min', [validators.NumberRange(min=0, max=100)])
    vulnavg = IntegerField('Vuln Avg', [validators.NumberRange(min=0, max=100)])
    vulnmax = IntegerField('Vuln Max', [validators.NumberRange(min=0, max=100)])
    rsmin = IntegerField('RS Min', [validators.NumberRange(min=0, max=100)])
    rsavg = IntegerField('RS Avg', [validators.NumberRange(min=0, max=100)])
    rsmax = IntegerField('RS Max', [validators.NumberRange(min=0, max=100)])
