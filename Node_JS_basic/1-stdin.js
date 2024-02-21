// task 1 - create a program that will be execute through command line
// it should display the message "Welcome to Holberton School... etc"
// user should be able to input their name on new line
// program should display "Your name is: INPUT"
// program should display "This important software is now closing"

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  console.log(`Your name is: ${data.toString().trim()}`);
}
);

process.stdin.on('exit', () => {
  console.log('This important software is now closing');
}
);
