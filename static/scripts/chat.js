var chat_room_id = undefined;
var last_received = 0;

// смайлики
var emoticons = {
	'\\(angel\\)' : 'angel_smile.png',
	'\\(angry\\)' : 'angry_smile.png',
	'\\(broken\\)' : 'broken_heart.png',
	':\\/' : 'confused_smile.png',
	'\\(cry\\)' : 'cry_smile.png',
	'\\(devil\\)' : 'devil_smile.png',
	'\\(embarrassed\\)' : 'embarrassed_smile.png',
	'\\(envelope\\)' : 'envelope.png',
	'\\(heart\\)' : 'heart.png',
	'\\(kiss\\)' : 'kiss.png',
	'\\(lightbulb\\)' : 'lightbulb.png',
	':o' : 'omg_smile.png',
	':\\)' : 'regular_smile.png',
	':\\(' : 'sad_smile.png',
	'8\\|' : 'shades_smile.png',
	':D' : 'teeth_smile.png',
	'\\(thumbs_down\\)' : 'thumbs_down.png',
	'\\(thumbs_up\\)' : 'thumbs_up.png',
	':p' : 'tongue_smile.png',
	':\\|' : 'whatchutalkingabout_smile.png',
	';\\)' : 'wink_smile.png',
}

/**
 * Initialize chat:
 * - Set the room id
 * - Generate the html elements (chat box, forms & inputs, etc)
 * - Sync with server
 * @param chat_room_id the id of the chatroom
 * @param html_el_id the id of the html element where the chat html should be placed
 * @return
 */
function init_chat(chat_id, html_el_id) {
	chat_room_id = chat_id;
	layout_and_bind(html_el_id);
	sync_messages();
}

/**
 * Asks the server which was the last message sent to the room, and stores it's id.
 * This is used so that when joining the user does not request the full list of
 * messages, just the ones sent after he logged in.
 * @return
 */
function sync_messages() {
    $.ajax({
        type: 'POST',
        data: {id:window.chat_room_id},
        url:'/chat/sync/',
		dataType: 'json',
		success: function (json) {
        	last_received = json.last_message_id;
		}
    });

	setTimeout("get_messages()", 2000);
}

/**
 * рендерим скилет чата и добавляем свои обработчики на интересующие нас события
 */
function layout_and_bind(html_el_id) {
		// рендерим скилет чата
		var html = '<div id="chat-messages-container">'+
						'<div id="chat-messages"> </div>'+
						'<div id="chat-last"> </div>'+
					'</div>'+
					'<div id="chat-smiles-container"> </div>'+
					'<form id="chat-form">'+
						'<input name="message" type="text" class="message" value="" />'+
						'<input type="submit" value="Отправить"/>'+
					'</form>';

		//рендерим чатик
		$("#"+html_el_id).append(html);

		//вставляем панель с сайликами
		for(key in emoticons){
			$("#chat-smiles-container").append('<img style="margin: 3px;" src="/static/images/chat/'+ emoticons[key] +' " value="'+ key.replace(/\\/g,'') +'" />');
		}

		//навешиваем обработчиков нажатия на каждый смайлик
		$.each($('#chat-smiles-container > img'), function(i, obj) {
			$(obj).bind('click', function(eventObj){
				$('#chat-form > input.message').val($('#chat-form > input.message').val() + ' ' + $(eventObj.target).attr('value') + ' ');
			});
		});

		// прикручиваем свой обработчик отправки формы
    	$("#chat-form").submit( function () {
            var $inputs = $(this).children('input');
            var values = {};

            $inputs.each(function(i,el) {
            	values[el.name] = $(el).val();
            });
			values['chat_room_id'] = window.chat_room_id;

        	$.ajax({
                data: values,
                dataType: 'json',
                type: 'post',
                url: '/chat/send/'
            });
            $('#chat-form .message').val('');

            return false;
	});
};

/**
 * получаем список сообщений и отображаем их
 */
function get_messages() {
    $.ajax({
        type: 'POST',
        data: {id:window.chat_room_id, offset: window.last_received},
        url:'/chat/receive/',
		dataType: 'JSON',
		success: function (json) {
			var scroll = false;
			//если находимся внизу div-а, то прокручиваем при каждом новом сообщении
			var $containter = $("#chat-messages-container");
			//вобще без понятия откуда тут взялось 13, но без него никак.
			if ($containter.scrollTop() == $("#chat-messages").outerHeight() - $containter.innerHeight()){
				scroll = true;
			}
			//alert($containter.scrollTop());
			//alert($("#chat-messages").outerHeight() - $containter.innerHeight());
			// добавляем сообщения
			$.each(json, function(i,m){
				if (m.type == 's')
					$('#chat-messages').append('<div class="system">' + replace_emoticons(m.message) + '</div>');
				else if (m.type == 'm')
					$('#chat-messages').append('<div class="message"><div class="author">'+m.author+': </div>'+replace_emoticons(m.message) + '</div>');
				else if (m.type == 'j')
					$('#chat-messages').append('<div class="join">'+m.author+' присоеденился к чату.</div>');
				else if (m.type == 'l')
					$('#chat-messages').append('<div class="leave">'+m.author+' покинул чат.</div>');

				last_received = m.id;
			})

			// прокручиваем вниз
			if (scroll)
				$containter.scrollTop($("#chat-messages").height());
		}
    });
    // ждем 2 секунды и просим прислать нам еще сообщений
    setTimeout("get_messages()", 2000);
}

/**
 * сообщаем что пользователь присоеденился к чату
 */
function chat_join() {
	$.ajax({
		async: false,
        type: 'POST',
        data: {chat_room_id:window.chat_room_id},
        url:'/chat/join/',
    });
}

/**
 * сообщаем что пользователь покидает чат
 */
function chat_leave() {
	$.ajax({
		async: false,
        type: 'POST',
        data: {chat_room_id:window.chat_room_id},
        url:'/chat/leave/',
    });
}

// добавляем обработчики событий входа в чат и выхода из чата
$(window).load(function(){
	$('#chat_label_close').click(function(obj){
		$('#chat_opened').hide();
		$('#chat_closed').show();
	});

	$('#chat_closed').click(function(obj){
		$('#chat_opened').show();
		$('#chat_closed').hide();
	});

	$('#add_room').click(function(obj){
		$('#chat_room_create').show();
	});

	$('#send_invitation').click(function(obj){
		$('#chat_send_invitation').show();
	});

	/*chat_join();*/
});
$(window).unload(function(){chat_leave()});

/**
 * заменяем в таксте сокращения смайликов тегом img
 */
function replace_emoticons(text) {
	$.each(emoticons, function(char, img) {
		re = new RegExp(char,'g');
		// replace the following at will
		text = text.replace(re, '<img src="/static/images/chat/'+img+'" />');
	});
	return text;
}