$(document).ready(function () {
    function getLatestPost() {
        $.ajax({
            url: "/get_latest_post/",
            type: 'GET',
            success: function (data) {
                $('#latestPosts').html(data);
            },
        });
    };

    function getArchive() {
        $.ajax({
            url: "/get_archive/",
            type: 'GET',
            success: function (data) {
                $('#archiveTree').html(data);
            },
        });
    };

    getLatestPost();
    getArchive();
});
