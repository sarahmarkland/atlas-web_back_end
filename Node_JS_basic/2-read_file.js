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
    
    let totalStudents = 0;

    Object.values(students).forEach((studentArray) => {
      totalStudents += studentArray.length;
    });

    console.log(`Number of students: ${totalStudents}`);

    Object.entries(students).forEach(([field, studentArray]) => {
      console.log(`Number of students in ${field}: ${studentArray.length}. List: ${studentArray.join(', ')}`);
    }
    );
}
module.exports = countStudents;
