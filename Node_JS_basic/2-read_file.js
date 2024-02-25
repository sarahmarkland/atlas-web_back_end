// reading a file synchronously with NodeJS
// Using the database.csv provided, create a function named
// countStudents that accepts a path in an argument
// attempts to read the database synchronously

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync
    (path, 'utf8');
    const lines = data.split('\n');
    const headers = lines.shift().split(',');
    const students = lines.map((line) => line.split(','));
    const studentsByField = {};
    for (const header of headers) {
      studentsByField[header] = [];
    }
    for (const student of students) {
      for (const i in headers) {
        studentsByField[headers[i]].push(student[i]);
      }
    }
    const count = studentsByField.firstname.length;
    console.log(`Number of students: ${count}`);
    for (const field in studentsByField) {
      if (field !== 'firstname') {
        const list = studentsByField[field].join(', ');
        console.log(`Number of students in ${field}: ${count}. List: ${list}`);
      }
    }
  }
  catch (err) {
    throw new Error('Cannot load the database');
  }
}
