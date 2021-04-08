from flask import Flask, request, abort, render_template
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', name='/')


@app.route('/api/', methods=['POST'])
def healthCheck():
    param = request.json['param']
    if(not param):
        abort(500)
    apiData = requests.get('https://api.fda.gov/drug/label.json?search=purpose:'+param)
    iti = apiData.json()
    #return iti
#    # ab = {"dos":thisdict["result"]}
#     ab.dos=iti.dos[0].dosage_and_administration[0]
#     ab.result = iti.result[0].description[0]
    result = iti['results'][0]
    parsedData = {'description':result['description'], 'dosage_and_administration': result['dosage_and_administration'], 'indications_and_usage':result['indications_and_usage']}
    return parsedData
    #return apiData.json()
