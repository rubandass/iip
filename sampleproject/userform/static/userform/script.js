// $(document).on("click", "label.statustxt", function () {
//     var txt = $(".statustxt").text();
//     $(".statustxt").replaceWith("<input class='statustxt form-control'/>");
//     $(".statustxt").val(txt);
// });

// $(document).on("blur", "input.statustxt", function () {
//     var txt = $(this).val();
//     $(this).replaceWith("<label class='statustxt' id='status' style='cursor:pointer'></label>");
//     $(".statustxt").text(txt);
//     fetch('status/', {
//         method: 'POST',
//         credentials: 'same-origin',
//         headers: {
//             "X-CSRFToken": getCookie("csrftoken")
//         },
//         body: JSON.stringify({
//             status: txt
//         })
//     });

// });

$('.editUser').click(function () {
    $('#userForm')[0].reset();
    $("#user").val($(this).data('id'));
    $("input[name='status']").val($(this).data('status'));
    $("#userModal").modal('show');
});

$("form#userForm").submit(function (e) {
    e.preventDefault();
    var formData = new FormData(this);
    var url = $(this).attr('action');
    console.log($("input[name='status']").val(), $("#user").val());

    fetch('status/', {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            status: $("input[name='status']").val(),
            user: $("#user").val()
        })
    }).then(response => response.json()).then(response => {
        // console.log(response.data);
        document.location.reload();
    });

});

function updateDate() {
    fetch('getstatus/', {
        method: 'GET',
        credentials: 'same-origin',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
    }).then(response => response.json()).then(response => {
        console.log(response.data[0]['date']);
        $('#date').val(response.data[0]['date']);
    });
}


// function populateTableValues() {
//     var newHtml = '<td>' + objUser.username + '</td>'
//         + '<td>' + objUser.fname + '</td>'
//         + '<td>' + objUser.lname + '</td>';
// $('#tr_' + objUser.id).html(newHtml);
// }
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
