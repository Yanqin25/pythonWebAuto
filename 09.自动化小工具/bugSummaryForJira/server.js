var express = require('express')
var fs = require('fs')
var util = require('util');
var bodyParser = require('body-parser');
var path = require('path')
var SumaryBug = require('./sumaryBug.js')
var app = express()
//使用模板引擎
app.set('views', path.join(__dirname, '/public/views'));
app.set('view engine', 'ejs');
var urlencodedParser = bodyParser.urlencoded({ extended: false })
app.use(express.static('public'));

app.get('/', function(req, res) {
    res.redirect('/login');
})
app.get('/login', function(req, res) {
    fs.readFile('./public/views/login.html', 'utf-8', function(err, data) {
        if (err) {
            console.log(err);
        } else {
            res.end(data)

        }
    });

})

app.post('/doLogin', urlencodedParser, function(req, res) {

    // 输出 JSON 格式
    var response = {
        "username": req.body.username,
        "password": req.body.password
    };
    res.redirect('/sumary');
})
app.get('/sumary', function(req, res) {
    fs.readFile('./public/views/sumary.html', 'utf-8', function(err, data) {
        if (err) {
            console.log(err);
        } else {
            res.end(data)
        }
    });

})
app.post('/doSumary', urlencodedParser, function(req, res) {
    var response = {
        "JSESSIONID": req.body.JSESSIONID,
        "RequireNo": req.body.RequireNo,
        'modelName': req.body.modelName,
        'filter': req.body.filter
    };
    // res.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' })
    SumaryBug.postRequest(response.JSESSIONID, response.RequireNo, response.modelName, response.filter)
        .then(function(bugData) {

            return SumaryBug.countBug(bugData)
        }).then(function(result) {
            res.render('result', { result: result })
            // res.end(JSON.stringify(result));
        }).catch(function(err) {
            res.writeHead(200, { 'Content-Type': 'text/html;charset=utf-8' });
            res.end(err);
        })


})
var server = app.listen(8888, function() {
    var host = server.address().address
    var port = server.address().port
    console.log('server has been started,the address is :http://%s:%s', host, port);
})



//jira登录获取JSESSIONID