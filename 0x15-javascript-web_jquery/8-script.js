$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(res) {
      console.log(res);
      
      // Assuming res.results is an array of movie objects
      $.each(res.results, function(index, movie) {
        // Create a new <li> element for each movie title
        const listItem = $('<li>').text(movie.title);
        // Append the new <li> to the <ul> with id "list_movies"
        listItem.appendTo('ul#list_movies');
      });
    });
});
