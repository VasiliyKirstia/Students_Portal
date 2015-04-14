var chat_room_id = undefined;
var is_active = false;
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

function init_chat(chat_id, html_el_id) {
	chat_room_id = chat_id;
	sync_messages();
}

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

	if(is_active){
		setTimeout("get_messages()", 2000); //2 секунды между синхронизациями
	}else{
		setTimeout("get_messages()", 20000); //20 секунд между синхронизациями
	}
}

/**
 * рендерим скилет чата и добавляем свои обработчики на интересующие нас события
 */

function bind_handlers(){

	//вставляем панель с сайликами
	for(key in emoticons){
		$("#chat-smiles-container").append('<img style="margin: 3px;" src="/static/images/chat/'+ emoticons[key] +' " value="'+ key.replace(/\\/g,'') +'" />');
	}

	//навешиваем обработчиков нажатия на каждый смайлик
	$.each($('#chat-smiles-container > img'), function(i, obj) {
		$(obj).bind('click', function(eventObj){
			$('#chat_textarea').val($('#chat_textarea').val() + ' ' + $(eventObj.target).attr('value') + ' ');
			$('#chat_textarea').focus();
		});
	});

	//переходим в пасивный режим
	$('#chat_label_close').click(function(obj){
		$('#chat_opened').hide();
		$('#chat_closed').show();
		window.is_active = false;
	});

	//переходим в активный режим
	$('#chat_closed').click(function(obj){
		$('#chat_closed').hide();
		$('#chat_opened').show();
		window.is_active = true;
	});

	//показываем формочку добавления комнаты
	$('#add_room').click(function(obj){
		$('#chat_send_invitation').hide();
		$('#chat_room_create').slideToggle();
	});

	//показываем формочку отправки приглашения
	$('#send_invitation').click(function(obj){
		$('#chat_room_create').hide();
		$('#chat_send_invitation').slideToggle();
	});

	//отправляем запрос на создание комнаты
	$("#chat_button_room_create").click( function () {
		alert($('#chat_new_room_name').val());

		$.ajax({
			data: {
				room_name: $('#chat_new_room_name').val()
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/send/',
			success: function(response){
				alert('успешно добавлена была комната');
			}
		});

		$('#chat_new_room_name').val('');
	});

	//рассылаем приглашения
	$("#chat_button_invitation_send").click( function () {
		alert($('#chat_invited_users').val());

		$.ajax({
			data: {
				users: $('#chat_invited_users').val()
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/send/',
			success: function(response){
				alert('все извещены');
			}
		});

		$('#chat_invited_users').val('');
	});

	//отправляем сообщение
	$("#chat_button_message_send").click( function () {
		$.ajax({
			data: {
				message: $('#chat_textarea').val()
			},
			async: true,
			dataType: 'json',
			type: 'post',
			url: '/chat/send/',
			success: function(response){
				alert('послал сообщение успешно');
			}
		});
		$('#chat_textarea').val('');
		$('#chat_textarea').focus();
	});

	//переходим в другую комнату
	$('.chat-block-room').click(function(obj){
		$('.chat-room-current').removeClass('chat-room-current');
		$(this).addClass('chat-room-current');
	});

	//$('#chat_textarea').keydown()
};

//получаем список сообщений и отображаем их TODO: проверить скролинг окна с сообщениями на адекватность
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

//присоеденяем пользователя к комнате
function chat_join() {
	$.ajax({
		async: false,
        type: 'POST',
        data: {chat_room_id:window.chat_room_id},
        url:'/chat/join/',
    });
}

//уходим из комнаты
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
	//init_chat();
	bind_handlers();
	/*chat_join();*/
});

$(window).unload(function(){chat_leave()});

//заменяем в таксте сокращения смайликов тегом img
function replace_emoticons(text) {
	$.each(emoticons, function(char, img) {
		re = new RegExp(char,'g');
		// replace the following at will
		text = text.replace(re, '<img src="/static/images/chat/'+img+'" />');
	});
	return text;
}