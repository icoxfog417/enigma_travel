
$(function(){
    var trainUrl = G.getCurrentUrl() + "/train";
    getTravel = function(){
        $.getJSON(trainUrl).done(bindTravel);
    }
    bindTravel = function(data){
        $("#travel").attr("src", data.image_url);
        $("#travel").data("travel_id", data.travel_id);
    }
    train = function(isLike){
        var params = {
            "_xsrf": G.getXsrf(),
            "travel_id": $("#travel").data("travel_id"),
            "is_like": isLike
        };
        $.post(trainUrl, params).done(getTravel);
    }
    decide = function(){
        var url = G.getCurrentUrl() + "/result" + location.search;
        location.href = url;
    }

    $("#like").click(function(){
        train(true);
    })
    $("#dislike").click(function(){
        train(false);
    })
    $("#decide").click(function(){
        decide();
    })
    getTravel();

})