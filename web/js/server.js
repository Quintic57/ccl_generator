/*server.js*/
const hostname = '127.0.0.1';
const port = 3000;
const http = require('http');
const fs = require('fs');

const htmlPage = "../ccl_generator.html";

fs.readFile(htmlPage, function(err, html){
    if (err) {
        throw err;
    }

    const server = http.createServer(function(req, res) {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/html');
      res.write(html);
      res.end();
    });

    server.listen(port, hostname, function() {
      console.log('Server running at http://'+ hostname + ':' + port + '/');
    });
});