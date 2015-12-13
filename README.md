Chrooms
=======

Chrooms (short for "Changing Rooms") glues together a Team Fortress 2 (TF2) server and a Mumble server, moving users to the Mumble chat room corresponding to the team they are playing on at the moment. Chrooms might also work for Source games other than TF2.

Components
----------

There are now two ways of hooking up chrooms with your Team Fortress 2 server. One involves the server mod EventScripts and one involves watching the console log file. We recommend using the log watcher.


Log Watcher
-----------

0. Get chrooms by running `git clone https://github.com/JonasOlson/chrooms.git` in a directory of your choice.
0. Add the following argument to your server invocation: `-consolelog /var/log/srcds/tf2.log`, i.e. when you start your server.
0. Copy the example config `chrooms/chrooms.cfg.example` to `chrooms/chrooms.cfg`.
0. Configure Chrooms in `chrooms/chrooms.cfg`. A password (also called "secret") for administration of the Mumble server is set with `icesecretwrite` in `/etc/mumble-server.ini`. Set the same secret in the configuration file for Chrooms. (Note that `icesecretwrite` must be commented out if you want the Mumble server to require no password.)
0. Start the log-watcher script when you start your server by calling `chrooms/log-watcher.bash`
0. Play on the TF2 server using the same username as in Mumble. (You don't need to match upper and lower cases, though.)

EventScripts
------------

0. Install EventScripts on the TF2 server by extracting [build 379](http://forums.eventscripts.com/viewtopic.php?p=407186#p407186) to the directory `tf/`. (The forum post says that build 379 is intended for Counter Strike, but using this version seems to be the only way to get it to work for TF2.) EventScripts generates an error message when the TF2 server starts, but it doesn't affect us.
0. Get chrooms by running `git clone https://github.com/JonasOlson/chrooms.git` in a directory of your choice.
0. Create a symbolic link to `chrooms/chrooms` from `tf/addons/eventscripts/chrooms` by running `ln -s chrooms/chrooms tf/addons/eventscripts/chrooms`. The exact path to the tf directory depends on where your TF2-server is installed.
0. Copy the example config `tf/addons/eventscripts/chrooms/chrooms.cfg.example` to `tf/addons/eventscripts/chrooms/chrooms.cfg`.
0. Configure Chrooms in `tf/addon/eventscripts/chrooms/chrooms.cfg`. A password (also called "secret") for administration of the Mumble server is set with `icesecretwrite` in `/etc/mumble-server.ini`. Set the same secret in the configuration file for Chrooms. (Note that `icesecretwrite` must be commented out if you want the Mumble server to require no password.)
0. Chooms is turned on and off with the following commands in the TF2 server console:

 * `es_load chrooms`
 * `es_unload chrooms`
 * `es_reload chrooms`

 To load Chrooms automatically when the TF2 server starts, put the first of these commands in `tf/cfg/autoexec.cfg`.
0. Play on the TF2 server using the same username as in Mumble. (You don't need to match upper and lower cases, though.)
