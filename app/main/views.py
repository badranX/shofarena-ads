from flask import redirect, render_template, url_for, flash, request
from . import main_blueprint
from .. import mongo
from .forms import SignUp




@main_blueprint.route('/sign', methods=['GET','POST'])
def signup():
    
    form = SignUp()
    
    #if request.method == 'POST':
        #print(request.form.to_dict())
    #usr = mongo.db.driver.find_one_or_404({})

    if form.validate_on_submit():
        mongo.db.driver.insert_one(request.form.to_dict())
        
        return redirect(url_for('static', filename='registerdone.html',username=request.form[form.first_name.name]))

    flash_errors(form)
    return render_template('base.html',form=form)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"{0} : {1}".format( getattr(form, field).label.text, error))