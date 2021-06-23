$(document).ready(function(){
    

    $('traer-datos').click(function(){
        //DIGIMON
        $.get({
            url: 'https://digimon-api.vercel.app/api/digimon',
            success: function(listaDG) {
 
             var tarjetas = $('#tarjetas')
             tarjetas.empty();
 
             console.log(listaDG)
 
             $.each(listaDG, function(indice, elemento){
                 tarjetas.append("<div class='card'>"+
                         "<img src='" + elemento.img + "' class='card-img-top' alt='" + elemento.name + "'>"+
                         "<div class='card-body'>"+
                             "<h5 class='card-title'>" + elemento.name + "</h5>"+
                             "<p class='card-text'><b>Nivel del Digimon:</b> " + elemento.level + "</p>"+
                        
            
                         "</div>"+
                     "</div>");
             });
 
            },
            error: function(erroerrorResponse) {
                console.error(errorResponse);
            }
        })
     })

})

