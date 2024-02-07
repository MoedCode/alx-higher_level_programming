#!/usr/bin/env node

$(document).ready(function() {
    $('DIV#add_item').click(function() {
        $('<li>').text('Item').appendTo('.my_list');
    });
});
