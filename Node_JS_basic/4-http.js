// create a small HTTP server using Node.js http module

const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  res.end('Hello Holberton School!');
});

const PORT = 1245;
app.listen(PORT);

module.exports = app;
