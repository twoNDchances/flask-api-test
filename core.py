from flask import render_template, redirect, url_for, Blueprint
from form import UserForm
import requests


main = Blueprint(name='main', import_name=__name__)

@main.route('/')
def main_root():
    return redirect(url_for('main.home'))


@main.route('/home', methods=['POST', 'GET'])
def home():
    api_url = url_for('userresource', _external=True)
    # users = User.query.all()
    form = UserForm()
    if form.validate_on_submit():
        data_send = {'name': form.name.data, 'age': form.age.data}
        try:
            response = requests.post(url=api_url, json=data_send)
            if response.status_code == 200:
                return redirect(url_for('main.home'))
            else:
                return redirect(url_for('main.home'))
        except:
            print('error code')
            return redirect(url_for('main.home'))
    return render_template(template_name_or_list='index.html', form=form, users=requests.get(url=api_url).json())