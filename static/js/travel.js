var G_DEADLINE = Date.now();
var G_TIMER = null;

decide = function(){
    var url = G.getCurrentUrl() + "/result" + location.search;
    location.href = url;
}

showTime = function(){
    var zeropad = function(num){
        return ("0" + num).slice(-2);
    }
    var now = moment();
    var duration = moment.duration(G_DEADLINE.diff(now));

    if(duration.asSeconds() < 0){
        clearInterval(G_TIMER);
        decide();
    }else{
        var timer = zeropad(duration.hours()) + ":" + zeropad(duration.minutes()) + ":" + zeropad(duration.seconds());
        $("#timer").text(timer);
    }
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
        var messages = ["いい感じね", "私は、ここ好きよ", "うーん、どうかしら？", "たまにはいいかもね", "ちょっと休憩するわ", "好きな人は好きかもね"];
        var index = Math.floor(Math.random() * (messages.length - 1));
        $("#message").text(messages[index]);
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
    G_TIMER = setInterval(function(){
        showTime();
    }, 1000);
})
