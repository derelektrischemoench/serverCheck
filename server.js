//the server has to be restarted everytime the httpresponse changes

var http=require('http');

http.createServer(function (req,res) {
    res.writeHead(404,{'Content-Type':'text/plain'});
    res.end('Hello world\n');
}).listen(8124,"127.0.0.1");

console.log("Server running @ localhost:8124");
