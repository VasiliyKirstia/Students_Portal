$(document).ready(function(){
    $('#form_with_big_data').submit(function(eventObj){
        $('#loading').show();
    });
    $(window).unload(function(){
        $('#loading').hide();
    });
});