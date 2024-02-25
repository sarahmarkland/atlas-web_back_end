// reading a file asynchronously with NodeJS

const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.trim().split('\n').slice(1);
        const students = {};

        lines.forEach((studentData) => {
          const [firstName, , , field] = studentData.split(',');
          if (!students[field]) students[field] = [];
          students[field].push(firstName);
        });

        console.log(`Number of students: ${lines.length}`);

        Object.entries(students).forEach(([field, names]) => {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        });
        resolve();
      }
    });
  });
}

module.exports = countStudents;
