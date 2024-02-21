// task 1 - create a program that will be execute through command line
// it should display the message "Welcome to Holberton School... etc"
// user should be able to input their name on new line
// program should display "Your name is: INPUT"
// program should display "This important software is now closing"

process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write(`Welcome to Holberton School, what is your name?\n`);
    process.stdout.write(`Your name is: ${chunk}`);
    process.stdout.write(`This important software is now closing\n`);
  }
});
process.stdin.on('end', () => {
  process.stdout.write('end\n');
});
