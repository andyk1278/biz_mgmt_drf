/* following code..
 * creates a new express instance,
 * defines directory to look for as entry point (current directory)
 * defines a port to run the server on
 * exports the express instance so it can be accessed from outside the file
 * ... run server with this set up by using:
 * 				$node serever.js
 */

var express = require('express');
var server = express();
server.use(express.static(__dirname));

var port = process.env.PORT || 8081;
server.listen(port);
console.log('Use port ' + port + ' to connect to this server');

exports = module.exports = server;
