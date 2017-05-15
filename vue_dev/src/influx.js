// const Influx = require('influx');

import Influx from 'influx'
export default queryAll


const influx = new Influx.InfluxDB('http://localhost:8086/test')


function writeIssue(issue)
{
  influx.writePoints([
    {
      measurement: 'diagnostic',
      tags: { adasVersion: issue['adasVersion'],
              environment: issue['environment'],
              issue: issue['issue'],
              roadName: issue['roadName'],
              roadType: issue['roadType'],
              testTime: issue['testTime'],
              vehicleId: issue['vehicleId']
            },
      fields: { cause:  issue['cause'], 
                comment: issue['comment']
              },
      timestamp: issue['timestamp']
    }],
    {precision: 's'}
  );  
}

function queryIssue(timestamp)
{
  return influx.query(`select * from diagnostic where timestamp = \'${timestamp}\'`);
}

function queryAll()
{
  return influx.query('select * from diagnostic');
}

function addIssue(issue)
{
  issue.environment = 'OUTDOOR';
  issue.vehicleId = '1';
  writeIssue(issue);
}

function updateIssue(newIssue)
{
  var issue = null;
  queryIssue(issue.timestamp).then(result => {issue = result;});
  issue.cause = newIssue.cause;
  issue.comment = newIssue.comment;
  writeIssue(issue);
}

function getRandomInt(ceil){
  return Math.floor(Math.random() * ceil);
}

function insertFakeData()
{
  var ISSUES = ['INTERVENTION', 'COLLISION', 'OUT OF ROAD', 'BREAK RED LIGHT'];
  var ROADS = [{road:'TangLuGongLu', type: 'UNSTRUCTURED'}, {road:'ChuanQiaoLu', type: 'STRUCTURED'}];
  var issue = { adasVersion: 'dev_1',
                environment: 'OUTDOOR',
                issue: ISSUES[getRandomInt(4)],
                roadName: ROADS[getRandomInt(2)].road,
                roadType: ROADS[getRandomInt(2)].type,
                testTime: '2017-05-04T14:43:21Z',
                timestamp: Math.floor(Date.now()/1000),
                vehicleId: '1',
                cause: '',
                comment: ''
              };
  writeIssue(issue);
}

// insertFakeData();

