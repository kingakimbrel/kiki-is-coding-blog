$(document).ready(function () {

    $('.chevron-toggle').on('click', function () {
        $('.glyphicon', this)
            .toggleClass('glyphicon-chevron-right')
            .toggleClass('glyphicon-chevron-down');
    });

    $('.archive-item').on('click', function () {
        var year = parseInt($(this).find('.h-year').val());
        var month = parseInt($(this).find('.h-month').val());
        var itemId = '#item-' + year + '-' + month;
        var url = "/get_posts/" + year + "/" + month;
        var elem = $(this);

        $.ajax({
            url: url,
            type: 'GET',
            success: function (data) {
                $(itemId).html(data);
                elem.removeClass('archive-item').off('click');
            },
        });
    });

    $('#submitComment').click(function (event) {
        var form = $("#newComment");
        form.validate({
            rules: {
                author: {
                    required: true
                },
                text: {
                    required: true
                }
            },
            messages:{
                author: {
                    required: '*Author is required'
                },
                text: {
                    required: '*Comment is required'
                }
            },
            errorClass: "has-error",
        });
        if (!form.valid()) {
            return;
        }

        event.preventDefault();

        $('#submitComment').prop('disabled', true);
        $.ajax({
            url: "/add_new_comment/",
            type: 'POST',
            data: $('form#newComment').serialize(),
            success: function (data) {
                $("#commentsDiv").html(data);
            },
            error: function (data) {
              alert("Ooops... We have a problem. Please refresh the page.");  
            },
        });
    });

});
