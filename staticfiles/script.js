$(function(){
var col = `<div class="col-2"><img id="flamelogo" src="{% static 'flame.png'%}"></div>`;
	for (var i = 0; i < 6; i++) {
		$("#footrow").append(col);
	}
});