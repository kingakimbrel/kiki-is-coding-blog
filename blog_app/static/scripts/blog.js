$(document).ready(function(){
    $('#viewPost').on('click', function(){
    var post_id = parseInt($(this).parent().find('#postID').val());

      $.ajax({ url: "/view_post/" + post_id + "/",
                 type: 'GET',
                 success: function(data) {
                         $('#pageContent').html(data);
                     },
        });
    });
 });