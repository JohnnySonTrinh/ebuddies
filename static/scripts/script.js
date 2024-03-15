/* jshint esversion: 11, asi: true */


// Toggles the visibility of a dropdown menu when the dropdown button is clicked.
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");
// Handles image file selection and displays a preview of the selected image.
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
// Automatically scrolls to the bottom of a conversation thread.
const conversationThread = document.querySelector(".room__box");

// Check if the dropdown button exists to avoid errors in pages without it.
if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    // Toggle the 'show' class to display or hide the dropdown menu.
    dropdownMenu.classList.toggle("show");
  });
}

// Ensure the photo input element exists on the current page.    
if (photoInput)
  photoInput.onchange = () => {
    // Get the first file from the file input.
    const [file] = photoInput.files;
    if (file) {
    	// Create a URL for the selected file and set it as the source for the preview image.
      photoPreview.src = URL.createObjectURL(file);
    }
};

// Check if the conversation thread container exists on the current page.
if (conversationThread) 
  // Set the scrollTop to the height of the scrollable content to scroll to the bottom.
  conversationThread.scrollTop = conversationThread.scrollHeight;