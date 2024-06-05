// Question and Answer Code

const questionSelect = document.getElementById("question");
const answerInput = document.getElementById("answer");
const submitButton = document.getElementById("submit-button");
const answerStore = document.getElementById("answer-store");

let storedAnswers = {}; // Object to store question-answer pairs

submitButton.addEventListener("click", function() {
  const selectedValue = questionSelect.value;
  const answer = answerInput.value.trim(); // Trim any leading/trailing spaces

  if (selectedValue === "") {
    alert("Please select a question first!");
  } else if (answer === "") {
    alert("Please enter your answer!");
  } else {
    // Store the answer
    storedAnswers[selectedValue] = answer;

    // Update the answer store display (basic example)
    answerStore.textContent = "Stored Answers: \n";
    for (const question in storedAnswers) {
      answerStore.textContent += question + ": " + storedAnswers[question] + "\n";
    }

    // Clear the answer input for the next question
    answerInput.value = "";
  }
});

// Fingerprint Recording Code


let touchpad = document.getElementById('touchpad');
let message = document.getElementById('message');
let loginButton = document.getElementById('loginButton');
let timer;

touchpad.addEventListener('mousedown', startTimer);
touchpad.addEventListener('mouseup', stopTimer);
touchpad.addEventListener('mouseleave', stopTimer);

function startTimer() {
    message.textContent = '';
    timer = setTimeout(recordFingerprint, 4000);
}

function stopTimer() {
    clearTimeout(timer);
}

function recordFingerprint() {
    message.textContent = 'Fingerprint recorded successfully!';
    loginButton.disabled = false;
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Logged in successfully!');
})


