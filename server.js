var http = require('http');

var template = "<h1>Hello, world from Node Server!</h1>";
var hostname = "localhost";
var portnumber = 3000;

function requestHandler(req, res) {
	res.writeHead(200, { 'Content-Type': 'text/html' });
	res.end(template);
}

var server = http.createServer(requestHandler);

server.listen(portnumber, () => console.log('server listening at port 3000'));
