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
    $( "#slider1" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 0, 500 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            }
        });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  } );

$(document).ready(function() {
    $( "#slider2" ).slider({
        range: true,
        min: 0,
        max: 500000000,
        values: [ 0, 500000000 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            }
        });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  } );

$(document).ready(function() {
    $( "#slider3" ).slider({
        range: true,
        min: 0,
        max: 10,
        values: [ 0, 10 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            }
        });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  } );

