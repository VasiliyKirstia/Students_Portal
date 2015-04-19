var chat_room_id = undefined;
var last_message_id = 0;
var last_invite_id = 0;
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

//переходим в другую комнату
function room_join(roomObj) {
	$.ajax({
		async: false,
        type: 'POST',
        data: {
        	'chat_room_id': $(roomObj).children('input').val(),
		},
        url:'/chat/join/',
        success: function(){
			$('.chat-room-current').removeClass('chat-room-current');
			$(roomObj).addClass('chat-room-current');
			$('#chat_messages_list').html('');

        	window.chat_room_id = $(roomObj).children('input').val();
        	window.last_message_id = 0;
        }
    });
}

//выходим из комнаты
function room_leave(roomObj) {
	$.ajax({
		async: true,
        type: 'POST',
        data: {
        	'chat_room_id': $(roomObj).children('input').val(),
        },
        url:'/chat/leave/',
        success: function(){
        	window.chat_room_id = undefined;
        }
    });
}

//заменяем в таксте сокращения смайликов тегом img
function replace_emoticons(text) {
	$.each(emoticons, function(char, img) {
		re = new RegExp(char,'g');
		text = text.replace(re, '<img src="/static/images/chat/'+img+'" />');
	});
	return text;
}

function set_passive_mode(){
	clearTimeout(tid);
	is_active = false;
	tid = setTimeout('passive_sync()', 1000);
}

function set_active_mode(){
	clearTimeout(tid);
	is_active = true;
	tid = setTimeout('active_sync()', 1000);
}

function change_room(obj){
	$('.chat-room-current').removeClass('chat-room-current');
	$(this).addClass('chat-room-current');

	room_join(this);
}

function remove_room(obj){
	var element = $(this).parent();
	room_leave(element);
	if(element.hasClass('chat-room-current'))
		$('#chat_messages_list').html('');
	element.remove();
}

function add_room(room_id, room_name){
	var new_room = $(
		'<div class="chat-block-room">' +
			'<input type="hidden" value="' + room_id + '">' +
			'<div class="chat-room-closer"></div>' +
			room_name +
		'</div>'
	);

	new_room.click(change_room);
	new_room.find('.chat-room-closer').click(remove_room);

	$('.chat-container-rooms').append(new_room);
	return new_room;
}

function add_invite(room_id, invite_title, invite_id){
	var new_invite = $(
		'<div class="chat-block-invite">' +
			'<input type="hidden" value="' + room_id + '">' +
			'<div class="chat-invite-closer"></div>' +
			invite_title +
		'</div>'
	);

	new_invite.click(
		function(){
			var room = $('.chat-block-room > input[value="' + room_id + '"]').parent();

			if(room.find('input[type="hidden"]').val() == undefined){
				room = add_room(room_id, invite_title);
			}

			$(this).remove();
			room_join(room);
			remove_invite(room_id);
		}
	);
	new_invite.find('.chat-invite-closer').click(
		function(){
			remove_invite(room_id);
			$(this).parent().remove();
		}
	);

	window.last_invite_id = invite_id;
	$('.chat-container-invites').append(new_invite);
}

function remove_invite(room_id){
	$.ajax({
		data: {
			'room_id': room_id,
		},
        type: 'post',
        url:'/chat/remove_invite/',
    });
}

function init() {
	$.ajax({
        type: 'post',
        url:'/chat/init/',
		dataType: 'json',
		success: function (json) {
        	for(var i in json.invites_list){
        		add_invite(json.invites_list[i].room_id, json.invites_list[i].title, json.invites_list[i].id);
        	}
        	for(var i in json.rooms_list){
        		add_room(json.rooms_list[i].room_id, json.rooms_list[i].title);
        	}
		},
    });

	set_passive_mode();
	$('#send_invitation').hide();
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
		$.ajax({
			data: {
				'new_room_name': $('#chat_new_room_name').val(),
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/create_room/',
			success: function(json){
				add_room(json.new_room_id, json.new_room_name);
				$('#chat_new_room_name').val('');
			}
		});
	});

	//рассылаем приглашения
	$("#chat_button_invitation_send").click( function () {
		$.ajax({
			data: {
				invited_users_list: $('#chat_invited_users').val(),
				chat_room_id: window.chat_room_id
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/invitation/',
			success: function(){
				//TODO: придумать реакцию на успешную рассылку приглосов
			}
		});
		//TODO: очистить сланый мультиселект
	});

	//отправляем сообщение
	$("#chat_button_message_send").click( function () {
		$.ajax({
			data: {
				message: $('#chat_textarea').val(),
				chat_room_id: window.chat_room_id
			},
			async: false,
			dataType: 'json',
			type: 'post',
			url: '/chat/send/',
		});
		if(window.chat_room_id != undefined){
			$('#chat_textarea').val('');
			$('#chat_textarea').focus();
		}
	});
}

//получаем список сообщений и отображаем их TODO: проверить скролинг окна с сообщениями на адекватность
function active_sync() {
	$.ajax({
		type: 'POST',
		data: {
			'chat_room_id': window.chat_room_id,
			'last_message_id': window.last_message_id,
			'last_invite_id': window.last_invite_id,
		},
		url:'/chat/active_sync/',
		dataType: 'JSON',
		success: function (json) {
//TODO проверить хорошенько все классы
			var scroll = false;
			//если находимся внизу div-а, то прокручиваем при каждом новом сообщении
			var $containter = $("#chat_messages_container");

			if ($("#chat_messages_list").outerHeight() + 20 == $containter.scrollTop() + $containter.innerHeight()){
				scroll = true;
			}
			//alert($containter.scrollTop());
			//alert($("#chat-messages").outerHeight() - $containter.innerHeight());
			// добавляем сообщения
			for(var i in json.new_messages){
				$('#chat_messages_list').append('<div class="chat-message"><div class="author">'+json.new_messages[i].author+'</div>'+replace_emoticons(json.new_messages[i].message) + '</div>');
				window.last_message_id = json.new_messages[i].id;
			}
			for(var i in json.new_invites){
				add_invite(json.new_invites[i].room_id, json.new_invites[i].title, json.new_invites[i].id);
			}
			// прокручиваем вниз
			if (scroll)
				$containter.scrollTop($("#chat_messages_list").height() + 20);
		}
	});
	//TODO убрать эту херню
	//------------------------------------
	if(window.chat_room_id == undefined)
		$('#send_invitation').hide();
	else
		$('#send_invitation').show();
	//------------------------------------

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
        	'chat_room_id': window.chat_room_id,
        	'last_message_id': window.last_message_id,
        	'last_invite_id': window.last_invite_id,
		},
        url:'/chat/passive_sync/',
		dataType: 'JSON',
		success: function (json) {
			$('#chat_closed > .chat-messages-count').text(json.new_messages_count);
			$('#chat_closed > .chat-invites-count').text(json.new_invites_count);
		}
    });

	clearTimeout(tid);
	if(window.is_active){
		tid = setTimeout('active_sync()', 2000); //2 секунды между синхронизациями
	}else{
		tid = setTimeout('passive_sync()', 20000); //20 секунд между синхронизациями
	}
}

// добавляем обработчики событий входа в чат и выхода из чата
$(window).load(function(){
	init();
	bind_handlers();
});