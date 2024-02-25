// reading a file synchronously with NodeJS
// Using the database.csv provided, create a function named
// countStudents that accepts a path in an argument
// attempts to read the database synchronously

const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.trim().split('\n').slice(1);
    const students = {};

    for (const line of lines) {
      const student = line.split(',');
      if (!students[student[3]]) {
        students[student[3]] = [];
      }
      students[student[3]].push(student[0]);
    }
    console.log(`Number of students: ${lines.length}`);
    for (const [cls, names] of Object.entries(students)) {
      console.log(`Number of students in ${cls}: ${names.length}. List: ${names.join(', ')}`);
    }
  }
