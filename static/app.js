var socket = null;
$(document).ready(function() {
    socket = new WebSocket("ws://" + document.domain + ":8888/websocket/");

    socket.onopen = function() {
	socket.send("Online");
    }

    socket.onmessage = function(message) {
	var txt = message.data;
	$(".container").append("<p>" + txt + "</p>");
    }
});

function submit() {
    var text = $("input#message").val();
    socket.send(text);
    $("input#message").val('');
}