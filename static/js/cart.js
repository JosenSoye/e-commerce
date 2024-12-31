let count = 0;

// Get button and count display elements
const addToBagButton = document.getElementById('addToBagButton');
const bagCount = document.getElementById('bagCount');

// Add click event listener to the button
addToBagButton.addEventListener('click', () => {
    count++; // Increment the count
    bagCount.textContent = count; // Update the displayed count
});