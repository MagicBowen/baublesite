from flask import Flask, request, abort, redirect, url_for
from flask_restful import Resource, Api
from influxdb import InfluxDBClient


app = Flask(__name__)
api = Api(app)

@app.route('/')
def show_index():
    return redirect(url_for('static', filename='index.html'))


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


class Diagnostics(Resource):
    def get(self):
        client = InfluxDBClient('localhost', 8086, '', '', 'test')
        querycmd = 'select * from diagnostic'
        
        parameters = list(request.args.items())
        if len(parameters) != 0:
            querycmd += get_where_cmd(parameters)

        items = client.query(querycmd)
        return {'items':list(items.get_points())}

    def post(self):
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

        return {'result': 'success'}, 201


class DiagnosticIssue(Resource):
    def get(self, timestamp):
        client = InfluxDBClient('localhost', 8086, '', '', 'test')
        items = client.query('select* from diagnostic where time = {}'.format(timestamp))
        item_list = list(items.get_points())
        result = None if len(item_list) == 0 else item_list
        return {'item':result}

    def put(self, timestamp):
        client = InfluxDBClient('localhost', 8086, '', '', 'test')
        if not request.json:
            print('format error!')
            abort(400)

        items = client.query('select* from diagnostic where time = {}'.format(timestamp))
        item_list = list(items.get_points())
        if len(item_list) == 0:
            print('result is none!')
            abort(400)

        json_body = [
            {
                "measurement": "diagnostic",
                "tags": {
                    "issue": item_list[0]['issue'],
                    "version": item_list[0]['version']
                },
                "time": timestamp,
                "fields": {
                    "cause": request.json['cause'],
                    "comments": request.json['comments']
                }
            }
        ]

        client.write_points(json_body)

        return {'result': 'success'}, 201



api.add_resource(Diagnostics, '/test/api/v1.0/diagnostics', endpoint = 'diagnostics')
api.add_resource(DiagnosticIssue, '/test/api/v1.0/diagnostics/<int:timestamp>', endpoint = 'issue')



if __name__ == '__main__':
    app.run(debug=True)