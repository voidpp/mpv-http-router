
var options = {
    socketFolder: "/usr/local/var/mpv/",
}

mp.options.read_options(options, 'ipc')

var socketFolder = options.socketFolder;

mp.msg.debug("socketFolder: '" + socketFolder + "'")

var socketPath = '';
var socketId = 1;

while(socketId < 100000) {
    socketPath = mp.utils.join_path(socketFolder, socketId + '.sock');
    if (mp.utils.file_info(socketPath) == null)
        break
    else
        mp.msg.debug("socket file '" + socketPath + "' is exists!")

    socketId++;
}

mp.msg.info("use '" + socketPath + "' to input-ipc-server")

mp.set_property("input-ipc-server", socketPath)
