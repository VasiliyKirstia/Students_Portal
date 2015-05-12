var Keylogger = {
    var log = {
        key_press: [],
        key_release: []
    };

    function init(element){
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

    function send(){
        /*$.ajax({
            async: true,
            type: 'POST',
            data: {
                'log': log,
            },
            url:'/secret_research/send_pack/',
            success: function(){
                Keylogger.log = {
                    key_press: [],
                    key_release: []
                };
            },
            error: function(){
                Keylogger.send();
            }
        });*/
        alert(log);
        Keylogger.log = {
            key_press: [],
            key_release: []
        };
    }
};