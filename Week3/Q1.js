const questions = [
  {
    question: "What's the best shape?",
    options: ["Triangle", "Hexagon"]
  },
  {
    question: "  Which planet is known as the Red Planet?",
    options: ["Mars", "Venus"]
  },
  {
    question: "  What is the capital of India?",
    options: ["New Delhi", "Mumbai"]
  },
  {
    question: "Which language is mainly used for web development?",
    options: ["JavaScript", "C++"]
  }
];
let i = 0;

function display(number) {
  const quest = questions[number];
  document.getElementById('span-quesno').innerHTML = number + 1;
  document.getElementById('qTitle').innerHTML = `${quest.question}`;
  document.getElementById('label-opt1').innerHTML = quest.options[0];
  document.getElementById('label-opt2').innerHTML = quest.options[1];
}

function next() {
  if (i < questions.length)
    display(i++);
  else {
    alert('End of Quiz!');
  }
}

next();