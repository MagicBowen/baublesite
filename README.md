# demo for flask and vuejs

## TODO:

[x]: constuct data in influxdb
[x]: restapi design by flask
[x]: adjust a table in UI
[x]: learn npm
[x]: learn webpack
[x]: learn html css and js
[x]: ajax of js
[x]: setup a echart website
[ ]: setup a element ui table website
[ ]: commit table content to restful api
[ ]: add new item to table
[ ]: adjust the UI theme
[ ]: build and publish


## tutorial

### install influxdb and prepare data

```bash
insert diagnostic,issue=INTERVENTION,version=dev_20170505 cause="",comments="none" 1493902371901910826
```

### design restful api

|method|url|action|
|------|---|------|
|GET|http://[hostname]/test/api/v1.0/diagnostics|get all items|
|GET|http://[hostname]/test/api/v1.0/diagnostics/timestamp|get one item|
|GET|http://[hostname]/test/api/v1.0/diagnostics?time_start=$start&time_end=$end&issues=INTERVENTION,COLLISION|get items by condition|
|POST|http://[hostname]/test/api/v1.0/diagnostics|create new item|
|PUT|http://[hostname]/test/api/v1.0/diagnostics/timestamp|update item|
|DELETE|http://[hostname]/test/api/v1.0/diagnostics/timestamp|delete item|


### install flask and flask_restful

```bash
pip install flask
pip install flask_restful
```


http://localhost:5000/test/api/v1.0/diagnostics?start=1493902415599485450&end=1493903415599485450&issues=LANE_BREAK

curl -H "Content-Type: application/json" -X POST 'localhost:5000/test/api/v1.0/diagnostics' -d '
{
    "time" : 1493902415599485500,
    "issue" : "LANE_BREAK",
    "version" : "dev_20170506",
    "cause" : "manul",
    "comments" : "no"
}
'

### install vuejs and element ui

```bash
npm install vuejs --save
npm install element-ui --save
```


```html
<p>This is another paragraph.</p>

<button id="ajax">ajax call</button>
<button id="json">json</button>

<script type="text/javascript">
    $('#json').click(function(){ 
         $.getJSON("http://localhost:5000/test/api/v1.0/diagnostics",
         function(data) {
            alert("received data " + data.items[0]["issue"]);         
          });   
    });

    $('#ajax').click(function(){ 
        // alert('ajax');
         $.ajax({ 
             type: "GET",
             dataType: "JSON",
             url: "http://localhost:5000/test/api/v1.0/diagnostics",
             success: function(data){ 
                 var content = "";
                 for (var i = 0; i < 6; i++){
                    content += "<li>" + data.items[i]["issue"] + "</li>" ;
                 }     
                $("p").html(content);
             }
         });
    });
</script>
```


download element-ui template project: 
https://github.com/ElementUI/element-starter

### install dependent package

```bash
npm install axios
```


