$(document).ready(function($){
    $("#title").click(function(){
        $("#title").text("Boo!");
    });
    $.getScript("js/user.js", function(){

    });
    console.dir(user);


});