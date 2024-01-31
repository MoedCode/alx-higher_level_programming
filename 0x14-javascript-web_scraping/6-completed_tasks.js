#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }

  try {
    const tasks = JSON.parse(body);

    // Your logic to count completed tasks for each user goes here
    const completedTasksCount = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksCount[task.userId]) {
          completedTasksCount[task.userId]++;
        } else {
          completedTasksCount[task.userId] = 1;
        }
      }
    });

    // Output the result as specified
    console.log(completedTasksCount);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
