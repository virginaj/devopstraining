from flask import Flask
from flask import request
import json
app = Flask(__name__)


@app.route('/')
def hello():
    return "Check Code of countries"

#for searching country code run on address bar http://127.0.0.1:5000/api/v1/countries?name=Country_name_here
@app.route('/api/v1/countries')
def iso_country():
    name=request.args.get('name')
    dict={'UK':'GB', 'India':'IND','Ireland':'IE','France':'FR','China':'CHN','Indonesia':'IDN','Spain':'ES'}
    for d in dict.keys():
        if name==d:
            iso_code=dict[d]
    return "Country ISO Code: {}".format(iso_code)

if __name__ == '__main__':
    app.run()

