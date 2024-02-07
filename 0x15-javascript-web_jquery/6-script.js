#!/usr/bin/env node

$(document).ready(function() {
    $('DIV#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});
