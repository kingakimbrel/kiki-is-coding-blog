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

});
