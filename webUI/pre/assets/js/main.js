$tl = $('#tl');
$tr = $('#tr');
$bl = $('#bl');
$br = $('#br');
$(document).ready(function() {
	$ftl;
	$ftr;
});
// $br.removeClass('visible');

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

function rmvall() {
	$tl.removeClass('visible');
	$tr.removeClass('visible');
	$bl.removeClass('visible');
	$br.removeClass('visible');
}


// .delay(1000)