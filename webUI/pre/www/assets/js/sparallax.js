// ------------------------------------------
// Sparallax.js - v0.1
// viewport based parallax
//
// Copyright (c) 2017 Harry Park (harrypark.io)
// MIT license
// ------------------------------------------

$('.sparallax').each(function(i) {
	var $spara = $(this);
	var units = 'px';
	var limits = $spara.attr('data-sparallax-limits').split(', ');
	var yUpperLim = limits[0];
	var yLowerLim = limits[1];

	$(window).scroll(function() {
		move();
	});

	$(window).resize(function() {
		move();
	});

	function move() {
		var offset = $spara.offset();
		var win = $(window);
		var scrollX = window.pageXOffset;
		var scrollY = window.pageYOffset;

		var limAdj = 1;
		var sparaHeight = ($spara.height() * limAdj);

		var toptop = (((((scrollY + win.height()) - sparaHeight) - win.height()) + sparaHeight) - sparaHeight);
		var bottombottom = ((scrollY + win.height()) - sparaHeight) + sparaHeight;

		if (bottombottom > offset.top && toptop < offset.top) {
			var percy = (scrollY - (offset.top - win.height())) / ((offset.top + sparaHeight) - (offset.top - win.height()));
			percy = Math.round(percy * 100);

			var updateVal;

			if ($spara.hasClass('sparallax-reverse')) {
				yVal = ((yUpperLim - yLowerLim) * (percy / 100)) - yUpperLim;
			} else {
				yVal = ((yLowerLim - yUpperLim) * (percy / 100)) - yLowerLim;
			}

			update(0, yVal);
		}

	}

	function update(x,y) {
		x = x.toString() + units;
		y = y.toString() + units;
		$spara.css('transform', 'translate3d('+x+', '+y+', 0)');
	}
});