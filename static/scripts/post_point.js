$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

function testAJAX() {
    
    var postArguments = {};
    postArguments["point_text"] = $("#point_text").val();
    
    console.log("Posting");
    $.post("xml_http_request_test", postArguments, processPointPostResponse);
    console.log("Posted");
}

function processPointPostResponse(response){
    
    console.log("Parsing");
    var result = JSON.parse(response).result;
    console.log("Parsed");
    
    if (result.status == "success") {
        var point_html = result.point_html;
        insertPointHTML(point_html);
    } else {
        var message = result.message;
    }
}

function insertPointHTML(point_html){
    
    var pointSection = $("#point_section");
    
    var seperator = $("<div class=\"seperator\" \></div>");
    seperator.hide();
    pointSection.prepend(seperator);
    seperator.show('slow');
    
    
    
    console.log(point_html);
    
    var newPoint = $(point_html);
    
    newPoint.hide();
    pointSection.prepend(newPoint);
    newPoint.show('fast');
}

function showPointFailure(message){
    
}