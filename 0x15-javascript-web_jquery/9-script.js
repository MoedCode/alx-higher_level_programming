$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(res) {
      console.log(res.hello);
      $('DIV#hello').text(res.hello);
    });
});
