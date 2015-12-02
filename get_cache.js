var url = require('system').args[1];
var dir = require('system').args[2];
var page = require('webpage').create();
var fs = require('fs');
page.open(url, function(status) {
        //console.log('Stripped down page text:\n' + page.plainText);
		console.log('Grabbing data for analysis . . . ')
		fs.write(dir, page.plainText, 'w')
		phantom.exit();
		});


