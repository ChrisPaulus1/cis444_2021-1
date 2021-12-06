const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = document.querySelector(tab.dataset.tabTarget)
    tabContents.forEach(tabContent => {
      tabContent.classList.remove('active')
    })
    tabs.forEach(tab => {
      tab.classList.remove('active')
    })
    tab.classList.add('active')
    target.classList.add('active')
  })
})




/*For Experience TAB*/



// Get the elements with class="column"
var elements = document.getElementsByClassName("column");

// Declare a loop variable
var i;

// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  }
}

// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "50%";
  }
}


//FOR FORUM

$(document).ready(function() {

        $('form').on('submit', function(event) {

                $.ajax({
                        data : {
                                name : $('#nameInput').val(),
                                email : $('#emailInput').val(),
                                message : $('#messageInput').val()


                        },
                        type : 'POST',
                        url : '/process'
                })
                .done(function(data) {

                        if (data.error) {
                                $('#errorAlert').text(data.error).show();
                                $('#successAlert').hide();


                        }
                        else {
                                $('#successAlert').text(data.name).show();
                                 alert("SUCCESS! I will be in touch soon")

                                $('#errorAlert').hide();
                        }




                });

                event.preventDefault();

        });

});

