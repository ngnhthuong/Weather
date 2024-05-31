const currentDate = new Date();
const formatDate = currentDate.toDateString();
const formatNow = "Now: " + formatDate;
const dateElement = document.getElementsByClassName("date");
dateElement[0].textContent = formatNow;



