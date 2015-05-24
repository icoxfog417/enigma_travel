var G_DEADLINE = Date.now();

showTime = function(){
    var now = moment();
    var duration = moment.duration(G_DEADLINE.diff(now));
    var zeropad = function(num){
        return ("0" + num).slice(-2);
    }
    var timer = zeropad(duration.hours()) + ":" + zeropad(duration.minutes()) + ":" + zeropad(duration.seconds());
    $("#timer").text(timer);
}

$(function(){
    var trainUrl = G.getCurrentUrl() + "/train";
    G_DEADLINE = moment($("#deadline").val(), "YYYY/MM/DD HH:mm:ss");
    getTravel = function(callback){
        $.getJSON(trainUrl).done(function(data){
            bindTravel(data);
            if(callback !== undefined){
                callback();
            }
        });
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
        $("#travel").hide("slide", {direction: "left"}, "slow");
        $.post(trainUrl, params).done(function(){
            getTravel(function(){
                $("#travel").show("slide", {direction: "right"}, "slow");
            });
        });
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
    var timer = setInterval(function(){
        showTime();
    }, 1000);
})
