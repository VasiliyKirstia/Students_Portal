var chat_room_id = undefined;
var last_received = 0;
var is_active = false;
var tid = undefined;

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

function init() {
	$.ajax({
        type: 'GET',
        url:'/chat/sync/',
		dataType: 'json',
		success: function (json) {
        	for(invite in json.invites){
        		$('.chat-container-invites').append('<div class="chat-block-invite"><input type="hidden" value="' + invite.room_id + '"><div class="chat-invite-closer"></div>' + invite.title + '</div>');
        	}
        	for(room in json.rooms){
        		$('.chat-container-rooms').append('<div class="chat-block-room"><input type="hidden" value="' + room.id + '"><div class="chat-room-closer"></div>' + room.title + '</div>');
        	}
		},
		onerror: alert('С сервером не удалось связаться')
    });

	set_passive_mode();
}

function set_passive_mode(){
	clearTimeout(tid);
	is_active = false;
	tid = setTimeout('active_sync()', 1000);
}

function set_active_mode(){
	clearTimeout(tid);
	is_active = true;
	tid = setTimeout('active_sync()', 1000);
}

function change_room(obj){
	$('.chat-room-current').removeClass('chat-room-current');
	$(this).addClass('chat-room-current');

	init_chat(chat_id = 10); //TODO ересь эту поправить
	room_join();
}

function remove_room(obj){
	var element = $(this).parent();
	if(element.hasClass('chat-room-current'))
		room_leave();
	element.remove();
}

function bind_handlers(){

	//вставляем панель с сайликами
	for(key in emoticons){
		$("#chat-smiles-container").append('<img style="margin: 3px;" src="/static/images/chat/'+ emoticons[key] +' " value="'+ key.replace(/\\/g,'') +'" />');
	}

	//навешиваем обработчиков нажатия на каждый смайлик
	$.each($('#chat-smiles-container > img'), function(i, obj) {
		$(obj).bind('click', function(eventObj){
			$('#chat_textarea').val($('#chat_textarea').val() + ' ' + $(eventObj.target).attr('value'));
			$('#chat_textarea').focus();
		});
	});

	//переходим в пасивный режим
	$('#chat_label_close').click(function(obj){
		$('#chat_opened').hide();
		$('#chat_closed').show();
		set_passive_mode();
	});

	//переходим в активный режим
	$('#chat_closed').click(function(obj){
		$('#chat_closed').hide();
		$('#chat_opened').show();
		set_active_mode();
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
				room_name: $('#chat_new_room_name').val(),
				//TODO добавить на формочку чекбокс
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/create_room/',
			success: function(response){
				alert('успешно добавлена была комната');
				//TODO перейти в только что добавленую комнату
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
			url: '/chat/invitation/',
			success: function(response){
				alert('все извещены');
				//TODO: придумать реакцию на успешную рассылку приглосов
			}
		});
		//TODO: очистить сланый мультиселект
		$('#chat_invited_users').val('');
	});

	//отправляем сообщение
	$("#chat_button_message_send").click( function () {
		$.ajax({
			data: {
				message: $('#chat_textarea').val(),
				room_id: chat_room_id,
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
	$('.chat-block-room').click(change_room);

	//удаляем комнаты из списка
	$('.chat-room-closer').click(remove_room);

	//переходим по приглашению
	$('.chat-block-invite').click(function(obj){
		var element = $('<div class="chat-block-room"><input type="hidden" value="' + $(this).children('input').val() + '"><div class="chat-room-closer"></div>' + $(this).text() + '</div>');
		element.click(change_room);
		element.find('.chat-room-closer').click(remove_room);
		$('.chat-container-rooms').prepend(element);
		$(this).remove();
		room_join(element); //TODO продумать присоеденение к комнате лучше
	});

	//удаляем приглашения из списка
	$('.chat-invite-closer').click(function(obj){
		$(this).parent().remove();
	});

	//TODO: $('#chat_textarea').keydown()
};

//получаем список сообщений и отображаем их TODO: проверить скролинг окна с сообщениями на адекватность
function active_sync() {
    $.ajax({
        type: 'POST',
        data: {id:window.chat_room_id, offset: window.last_received},
        url:'/chat/active_sync/',
		dataType: 'JSON',
		success: function (json) {
//TODO проверить хорошенько все классы
			var scroll = false;
			//если находимся внизу div-а, то прокручиваем при каждом новом сообщении
			var $containter = $("#chat_messages_container");
			//вобще без понятия откуда тут взялось 13, но без него никак.
			if ($containter.scrollTop() == $("#chat-messages").outerHeight() - $containter.innerHeight()){
				scroll = true;
			}
			//alert($containter.scrollTop());
			//alert($("#chat-messages").outerHeight() - $containter.innerHeight());
			// добавляем сообщения
			$.each(json, function(i,m){
				$('#chat_messages_container').append('<div class="chat-message"><div class="author">'+m.author+': </div>'+replace_emoticons(m.message) + '</div>');
				last_received = m.id;
			});

			// прокручиваем вниз
			if (scroll)
				$containter.scrollTop($("#chat_messages_container").height());
		}
    });

	clearTimeout(tid);
    if(window.is_active){
		tid = setTimeout('active_sync()', 2000); //2 секунды между синхронизациями
	}else{
		tid = setTimeout('passive_sync()', 20000); //20 секунд между синхронизациями
	}
}

function passive_sync() {
	$.ajax({
        type: 'POST',
        data: {
        	id:window.chat_room_id
		},
        url:'/chat/passive_sync/',
		dataType: 'JSON',
		success: function (json) {
			//TODO доделать мф
		}
    });

	clearTimeout(tid);
	if(window.is_active){
		tid = setTimeout('active_sync()', 2000); //2 секунды между синхронизациями
	}else{
		tid = setTimeout('passive_sync()', 20000); //20 секунд между синхронизациями
	}
}

//переходим в другую комнату
function room_join(roomObj) {
	$('.chat-room-current').removeClass('chat-room-current');
	$(roomObj).addClass('chat-room-current');
	$('#chat_messages_container').html('');

	$.ajax({
		async: false,
        type: 'POST',
        data: {
        	id: $(roomObj).children('input').val()
		},
        url:'/chat/join/',
        success: function(){
        	window.chat_room_id = $(roomObj).children('input').val()
        }
    });
}

//выходим из комнаты
function room_leave(room_id) {
	$.ajax({
		async: true,
        type: 'POST',
        data: {
        	chat_room_id:room_id
        },
        url:'/chat/leave/',
    });
}

//заменяем в таксте сокращения смайликов тегом img
function replace_emoticons(text) {
	$.each(emoticons, function(char, img) {
		re = new RegExp(char,'g');
		// replace the following at will
		text = text.replace(re, '<img src="/static/images/chat/'+img+'" />');
	});
	return text;
}

// добавляем обработчики событий входа в чат и выхода из чата
$(window).load(function(){
	init();
	bind_handlers();
});