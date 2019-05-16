window.onload = function () {
    formatNumber()
};

document.addEventListener('DOMContentLoaded', formatNumber());


function formatNumber() {
    var div_list = document.body.getElementsByClassName('price-text')
    for(var i=0; i < div_list.length; i++) {
        num = div_list[i].textContent
        div_list[i].innerHTML = 'Verð: ' + num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.') + 'kr.'
    }

};