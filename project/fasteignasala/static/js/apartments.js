$(document).ready(function() {
    $('#search-button').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: [ function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="apartment_container">
                            <a href="/${d.id}">
                            <div class="see_more">
                            <p>Skoða nánar</p>
                            </div>
                            <div class="crop">
                                <img class="apartment-img" src="${d.first_image}"/>
                            </div>
                            </a>
                            <p class="apartment_address">${d.address}
                                <span class="apartment_zip">${d.zip} </span>
                            </p>

                            <div class="info">
                                <p>${d.type}</p>
                                <p>${d.num_rooms} herbergi</p>
                                <p>${d.size} m<sup>2</sup></p>
                            </div>

                            <div class="price_container">
                                <div class="price">Verð: ${d.price} kr.</div>
                            </div>
                            </div>`
                });
                $('.apartment_list').html(newHtml.join(''));
                $('#search-box').val('');
            }],
            error: function (xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
                console.log('whoops');
            }
        })
    });
});

$(document).ready(function() {
    var min = $(".min_1");
    var max = $(".max_1");
    $( "#slider1" ).slider({
        range: true,
        min: 0,
        max: 500,
        step: 10,
        values: [ 0, 500 ],

        slide: function( event, ui ) {
            min.html(ui.values[0] + " m<sup>2</sup>")
            max.html(ui.values[1] + " m<sup>2</sup>")
            }
        });
  } );




$(document).ready(function() {
    var min = $(".min_2");
    var max = $(".max_2");
    $( "#slider2" ).slider({
        range: true,
        min: 0,
        max: 200,
        values: [ 0, 200],
        slide: function( event, ui ) {
            min.html(ui.values[0] + " milljónir")
            max.html(ui.values[1] + " milljónir")
            }
        });
  } );

$(document).ready(function() {
    var min = $(".min_3");
    var max = $(".max_3");
    $( "#slider3" ).slider({
        range: true,
        min: 0,
        max: 10,
        values: [ 0, 10 ],
        slide: function( event, ui ) {
            min.html(ui.values[0] + " herbergi")
            max.html(ui.values[1] + " herbergi")
            }
        });
  } );
