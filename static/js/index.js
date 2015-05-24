$(function(){
    createUrl = function(){
        var budget = $(this).data("value");
        $.post("/group", {
                "_xsrf": G.getXsrf(),
                "budget": budget
            }
        ).done(bindUrl);
    }
    bindUrl = function(data){
        $("#share").show();
        $("#url").attr("href", data.url);
        $("#message").text("今度はみんなが行きたい場所をおしえて？");
    }
    $(".submit").click(createUrl)
})