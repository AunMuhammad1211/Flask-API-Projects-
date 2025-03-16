document.addEventListener("DOMContentLoaded", function () {
  const message = "This form is for AI and Data Science Students";
  let index = 0;
  let forward = true; // Flag to track direction

  function typeEffect() {
      const displayText = document.getElementById("formMessage");

      if (forward) {
          // Typing forward
          displayText.textContent = message.substring(0, index++);
          if (index > message.length) {
              forward = false; // Start backtracking
              setTimeout(typeEffect, 1000); // Pause before deleting
              return;
          }
      } else {
          // Backtracking (deleting)
          displayText.textContent = message.substring(0, index--);
          if (index < 0) {
              forward = true; // Start typing again
          }
      }
      setTimeout(typeEffect, 100); // Speed of typing
  }

  // Start the animation
  typeEffect();
});
