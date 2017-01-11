$tl = $('#tl');
$tr = $('#tr');
$bl = $('#bl');
$br = $('#br');

$tick = $('#tick');
$cross = $('#cross');

// $br.removeClass('visible');



$(document).keyup(function(e) {
	if (e.keyCode == 37) { // 37 == left arrow
		tl();
	} else if (e.keyCode == 38) { // 38 == up arrow
		tr();
	} else if (e.keyCode == 39) { // 39 == right arrow
		br();
	} else if (e.keyCode == 40) { // 40 == down arrow
		bl();
	} else if (e.keyCode == 88) { // 88 == x
		cross();
	} else if (e.keyCode == 86) { // 86 == v
		tick();
	}  else if (e.keyCode == 67) { // 67 == c
		rmvall();
	}
});



// $('#btn-tl').on('click', function() {
// 	tl();
// });

// $('#btn-cl').on('click', function() {
// 	rmvall();
// });

// $('#btn-tr').on('click', function() {
// 	tr();
// });

// $('#btn-bl').on('click', function() {
// 	bl();
// });

// $('#btn-br').on('click', function() {
// 	br();
// });

// $('#btn-tick').on('click', function() {
// 	tick();
// });

// $('#btn-cross').on('click', function() {
// 	cross();
// });

function tr() {
	rmvall();
	$tr.addClass('visible');
}

function br() {
	rmvall();
	$br.addClass('visible');
}

function bl() {
	rmvall();
	$bl.addClass('visible');
}

function tl() {
	rmvall();
	$tl.addClass('visible');
}

function tick() {
	rmvall();
	$tick.addClass('visible');
}

function cross() {
	rmvall();
	$cross.addClass('visible');
}

function rmvall() {
	$tl.removeClass('visible');
	$tr.removeClass('visible');
	$bl.removeClass('visible');
	$br.removeClass('visible');
	$tick.removeClass('visible');
	$cross.removeClass('visible');
}


// .delay(1000)