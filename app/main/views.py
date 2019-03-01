from flask import redirect, render_template, url_for, flash, request
from . import main_blueprint
from .. import mongo
from .forms import SignUp




@main_blueprint.route('/sign', methods=['GET','POST'])
def signup():
    flash("hilo")
    
    form = SignUp()
    
    if request.method == 'POST':
        print(request.form.to_dict())
    usr = mongo.db.driver.find_one_or_404({})

    if form.validate_on_submit():
        print("validated YAHYA")
        mongo.db.driver.insert_one(request.form.to_dict())
        return redirect(url_for('static', filename='registerdone.html'))

    flash_errors(form)
    return render_template('form.html',form=form,userr=usr)


def flash_errors(form):
    
    for field, errors in form.errors.items():
        for error in errors:
            
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))



