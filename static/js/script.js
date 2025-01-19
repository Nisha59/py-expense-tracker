// Form validation to check if the date format is correct (DD-MM-YYYY)
document.getElementById('expenseForm').addEventListener('submit', function(e) {
    const dateField = document.getElementById('date');
    const dateValue = dateField.value;

    const datePattern = /^\d{2}-\d{2}-\d{4}$/; // RegEx pattern for DD-MM-YYYY format

    if (!datePattern.test(dateValue)) {
        alert('Please enter a valid date in the format DD-MM-YYYY');
        e.preventDefault();
    }
});

// Optional: You can add more JS for interactivity
