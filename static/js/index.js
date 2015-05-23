$(function(){
    createUrl = function(){
        $.post("/group", {"_xsrf": G.getXsrf()}).done(bindUrl);
    }
    bindUrl = function(data){
        $("#share").show();
        $("#url").attr("href", data.url);
    }
    $("#submit").click(createUrl)
})