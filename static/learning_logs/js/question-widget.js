//to create a widget that shows an after session question


// Create array constant
const afterQuestions = ["apple", "banana", "orange", "grape", "pineapple"];

// Create object with a div id
const questionDiv = document.getElementById(questionWidget).firstChild;

// Create a function that calls a random element of the array
function getAfterQuestions() {
  var randomIndex = Math.floor(Math.random() * afterQuestions.length);
  return afterQuestions[randomIndex];
}

// Create a function that prints the element inside the div object
function printQuestion() {
  questionDiv.textContent = getAfterQuestions();
}

var getButton = document.getElementById('getQuestion')

if (getButton.addEventListener)
    getButton.addEventListener("click", printQuestion, false);
else if (getButton.attachEvent)
    getButton.attachEvent('onclick', printQuestion);

alert("Hello World!");
