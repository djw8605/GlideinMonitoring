
from mod_python import apache

def index(req):
    s = """

<html>
<head>
<meta http-equiv="refresh" content="300" > 
<script type="text/javascript" src="http://www.google.com/jsapi"></script>
<script type="text/javascript" src="http://glidein.unl.edu/jquery.js"></script>

<script type="text/javascript">
var gready = 0;
google.load('visualization', '1', {'packages':['corechart', 'imagepiechart']});
google.setOnLoadCallback(googleReady);


function googleReady() { gready = 1; drawChart(); }

function drawChart() {
   if (gready == 1) {
        $.ajax({type: "GET", url: "stats/gsitedata",  success: parseXml});
   }

}



function parseXml(xml) {
   var data = new google.visualization.DataTable();
   data.addColumn('string', 'Site');
   data.addColumn('number', 'Glideins Running');

   $(xml).find("site").each(function() {
        data.addRow([$(this).attr("name") + " (" + parseInt($(this).attr("running")) + ")", parseInt($(this).attr("running"))])
   
   });
   var chart;
   if ($("#chartflipper").html() == "Interactive") {
   chart = new google.visualization.PieChart(document.getElementById('gviz'));
   } else {
   chart = new google.visualization.ImagePieChart(document.getElementById('gviz'));
   }

   chart.draw(data, {width: 800, height:500, title: 'Sites Running Glideins', pieSliceText:'value' });


}

function normalize(input_array) {
    normalized_total = 0;
    $(input_array).each(function() { normalized_total += parseFloat(this) });
    toReturn = [];
    if (normalized_total == 0) {
        $(input_array).each(function() { toReturn.push(0) });
    } else {
        $(input_array).each(function() { toReturn.push((parseFloat(this) / parseFloat(normalized_total)) * 100.0) });
    }
    return toReturn;
}

function parseuserdata(xml) {
    var running = [];
    var idle = [];
    var users = [];
    $(xml).find("user").each(function() {
        running.push($(this).attr("running"));
        idle.push($(this).attr("idle"));
        users.push($(this).attr("name"));
    });


    var normal_running = normalize(running);
    var normal_idle = normalize(idle);

    baseurl = "http://chart.apis.google.com/chart?cht=pc&chs=750x350&chtt=Running+Outer;+Idle+Inner&chco=FF0000,00FFFF&";
    baseurl += "chd=t:";
    baseurl += normal_idle.join(",");
    baseurl += "|";
    baseurl += normal_running.join(",");
    baseurl += "&chl=";
    var idleusers = [];
    for (var i in users) {
        idleusers.push(users[i] + " (idle: " + idle[i] + ")");
    }
    baseurl += idleusers.join("|");
    baseurl += "|";
    var runningusers = [];
    for (var i in users) {
        runningusers.push(users[i] + " (running: " + running[i] + ")");
    }
    baseurl += runningusers.join("|");
    //baseurl += "&chdl=";
    //var labels = [];
    //for ( var i in users)
    //{
    //     labels = users[i] + " (running: " + running[i] + ", idle: " + idle[i] + ")"
    //}
    //baseurl += "&chl=";
    //baseurl += users.join(",");
    $("#userdata").attr("src", baseurl);
    //$("#userdataurl").html(baseurl);
}


$(document).ready(function() {

$("#chartflipper").click( function() {
    if ($(this).html() == "Image Charts") {
    $(this).html("Interactive");
    drawChart();
    } else {
    $(this).html("Image Charts");
    drawChart();
    }

});

    $.ajax({type: "GET", url: "stats/guserdata",  success: parseuserdata});

});

</script>

</head>
<body>
<button type="button" id="chartflipper" >Image Charts</button>
<div id="gviz"></div>
<div id="userdataurl"><div>
<img id="userdata" />
<img src="stats/allsites"/>
<img src="stats/allusers"/> 
</body>

</html>



"""
    req.content_type = "text/html"
    req.write(s)



