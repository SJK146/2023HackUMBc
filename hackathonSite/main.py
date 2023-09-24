from collections import OrderedDict
from flask import Flask, request, render_template

import apiFunctions
import hellDiver

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    dynamic_data = {"Key": "Item", "key2": "item2"}
    if request.method == 'POST':
        data_from_form = request.form['submit']

        dynsmic_data = esgAPI(data_from_form)
        dynamic_data = apiFunctions.esgAPI(data_from_form)
        return render_template('index.html', dynamic_data=dynamic_data)
        # Process the data (e.g., save it, perform an action, etc.)
    return render_template('index.html', dynamic_data=dynamic_data)



