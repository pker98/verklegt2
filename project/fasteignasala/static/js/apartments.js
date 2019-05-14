function sort(){
    var sortval = $('#sortval').val();
    $.ajax({
        type: "POST",
        url: "",
        data: { sortval: sortval },
    }).done(function(data){
         $('.apartment_list').html(data.html);
    });
}

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

var slideIndex = 1;
//showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  //slides[slideIndex-1].style.display = "block";
  //dots[slideIndex-1].className += " active";
}

$(document).ready(function() {
    $('#search-button').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var min_size = $("#slider1").slider("values")[0];
        var max_size = $("#slider1").slider("values")[1];
        var min_mkr = $("#slider2").slider("values")[0] * 1000000;
        var max_mkr = $("#slider2").slider("values")[1] * 1000000;
        var min_rooms = $("#slider3").slider("values")[0];
        var max_rooms = $("#slider3").slider("values")[1];
        console.log(min_size);
        console.log(min_rooms);
        $.ajax({
            url: '?search_filter=' + searchText + '&min_mkr=' + min_mkr + '&max_mkr=' + max_mkr +
            '&min_size=' + min_size + '&max_size=' + max_size + '&min_rooms=' + min_rooms + '&max_rooms=' + max_rooms,
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
