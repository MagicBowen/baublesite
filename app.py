#!flask/bin/python
from flask import Flask, jsonify, request, abort
from influxdb import InfluxDBClient

app = Flask(__name__)

def get_para_value(paras, key):
    for p in paras:
        if p[0] == key:
            return p[1]
    return None

def get_where_cmd(paras):
    start = get_para_value(paras, 'start')
    end = get_para_value(paras, 'end')
    issues = get_para_value(paras, 'issues')
    issue_cmd = ''
    if issues is not None:
        items = issues.split(',')
        issue_cmd += ' and '
        for i, issue in enumerate(items):
            issue_cmd += 'issue =~ /{}/'.format(issue)
            if i < len(items) - 1:
                issue_cmd += ' or '
    return " where time > {} and time < {} {}".format(start, end, issue_cmd)


@app.route('/test/api/v1.0/diagnostics', methods=['GET'])
def get_items():
    client = InfluxDBClient('localhost', 8086, '', '', 'test')
    querycmd = 'select * from diagnostic'
    
    parameters = list(request.args.items())
    if len(parameters) != 0:
        querycmd += get_where_cmd(parameters)

    items = client.query(querycmd)
    return jsonify({'items':list(items.get_points())})


@app.route('/test/api/v1.0/diagnostics/<int:timestamp>', methods=['GET'])
def get_item(timestamp):
    client = InfluxDBClient('localhost', 8086, '', '', 'test')
    items = client.query('select* from diagnostic where time = {}'.format(timestamp))
    item_list = list(items.get_points())
    result = None if len(item_list) == 0 else item_list
    return jsonify({'item':item_list})


@app.route('/test/api/v1.0/diagnostics', methods=['POST'])
def post_item():
    client = InfluxDBClient('localhost', 8086, '', '', 'test')
    if not request.json or not 'time' in request.json:
        print('--------', request.json)
        abort(400)

    json_body = [
        {
            "measurement": "diagnostic",
            "tags": {
                "issue": request.json['issue'],
                "version": request.json['version']
            },
            "time": request.json['time'],
            "fields": {
                "cause": request.json['cause'],
                "comments": request.json['comments']
            }
        }
    ]

    client.write_points(json_body)

    return jsonify({'result': 'success'}), 201






if __name__ == '__main__':
    app.run(debug=True)