#!/usr/bin/env node

$(document).ready(function () {
    $('DIV#toggle_header').click(function () {
        $('header').toggleClass($('header').hasClass('red') ? 'green' : 'red');
    });
});
