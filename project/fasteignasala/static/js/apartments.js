$(document).ready(function() {
    $('#search-button').on('click', function (e) {
        e.preventDefault()
        var searchText = $('#search-box').val();
        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {

            },
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
            }
        })
    });

});