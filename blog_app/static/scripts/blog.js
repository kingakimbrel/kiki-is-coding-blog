$(document).ready(function () {
    //    function getArchive() {
    //        $.ajax({
    //            url: "/get_archive/",
    //            type: 'GET',
    //            success: function (data) {
    //                $('#archiveTree').html(data);
    //            },
    //        });
    //    };
    $('.chevron-toggle').on('click', function () {
        $('.glyphicon', this)
            .toggleClass('glyphicon-chevron-right')
            .toggleClass('glyphicon-chevron-down');
    });

});
