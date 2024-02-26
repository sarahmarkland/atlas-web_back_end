const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

// Route for the root path
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for /students path
app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  countStudents(databasePath)
    .then((students) => {
      res.send(`This is the list of our students: \n${JSON.stringify(students)}`);
    })
    .catch((error) => {
      console.error(error);
      res.status(500).send('Internal Server Error');
    });
});

// Listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running and listening on port ${PORT}`);
});

// Export the app variable
module.exports = app;
