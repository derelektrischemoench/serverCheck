//the server has to be restarted everytime the httpresponse changes

var http=require('http');

http.createServer(function (req,res) {
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write('hello world');
    res.end();
}).listen(8124,"127.0.0.1");

console.log("Server1 running @ localhost:8124");

//Server2
var http2=require('http');

http2.createServer(function (req,res) {
    res.writeHead(404,{'Content-Type':'text/html'});
    res.write('hello world2');
    res.end();
}).listen(8125,"127.0.0.1");

console.log("Server2 running @ localhost:8125");
