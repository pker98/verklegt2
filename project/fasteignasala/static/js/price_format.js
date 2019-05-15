function formatNumber(num) {
  document.getElementById('price-text').innerHTML = 'Verð: ' + num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.') +' kr.';
}