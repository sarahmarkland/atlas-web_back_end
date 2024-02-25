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

    lines.forEach((studentData) => {
      const [firstName, , , field] = studentData.split(',');
      if (!students[field]) students[field] = [];
      students[field].push(firstName);
    });
    
    const totalStudents = students.length;
    console.log(`Number of students: ${totalStudents}`);

    Object.entries(studentsByField).forEach(([field, names]) => {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });
}

module.exports = countStudents;
