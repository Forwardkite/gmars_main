//Operation
const operation = (type) => {
    switch (type){
        case "nav":
            animator("ham");
            $("menu").css("right") >= "0px" ? $("menu").css("right","-100%") : $("menu").css("right", "0px");
            overlay();
        break;
    }   
}


//Overlay
const overlay = (no) => {
    if (no == 1){
        operation("nav");
    } else {
        $(".overlay").length > 0 ? $(".overlay").remove() : $("body").append('<div class="overlay" onclick="overlay(1)"></div>');
    }
}

// LINK TO EXTERNAL PAGE

// HOLIDAYS
// const linkHolidays = document.querySelector('.link_holidays');
// linkHolidays.addEventListener('click', (event) => {
//   event.preventDefault();
//   window.location.href = 'https://gmarsholidays.gmarsgroup.com/';
// });

// // STUDY ABROAD
// const linkStudyabroad = document.querySelector('.link_studyabroad');
// linkStudyabroad.addEventListener('click', (event) => {
//   event.preventDefault();
//   window.location.href = 'https://gmarsedu.com/';
// });

// //HIRING SOLUTIONS
// const linkHiringsolutions = document.querySelector('.link_hiringsolutions');
// linkHiringsolutions.addEventListener('click', (event) => {
//   event.preventDefault();
//   window.location.href = 'https://hiringsolutions.gmarsgroup.com/';
// });

// //EVENT MANAGEMENT
// const linkEventmanagement = document.querySelector('.link_eventmanagement');
// linkEventmanagement.addEventListener('click', (event) => {
//   event.preventDefault();
//   window.location.href = 'https://www.instagram.com/gmarsmanagementpvtltd/';
// });
