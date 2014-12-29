Chrooms
=======

Chrooms (short for "Changing Rooms") glues together a Team Fortress 2 (TF2) server and Mumble server, and moves users to the Mumble chatroom corresponding to the team they are playing on at the moment. Chrooms might also work for Source games other than TF2.

Installation instructions:

0. Install the TF2 server.
0. Install EventScripts on the TF2 server by extracting [build 379](http://forums.eventscripts.com/viewtopic.php?p=407186#p407186) to the directory `tf/`. (The forum post says that build 379 is intended for Counter Strike, but using this version seems to be the only way to get it to work for TF2.) EventScripts generates an error message when the TF2 server starts, but it doesn't affect us.
0. Install Chrooms by copying `chrooms/chrooms/` to `tf/addon/eventscripts/`.
0. Configure Chrooms in `tf/addon/eventscripts/chrooms/chrooms.cfg`. A password (also called "secret") for administration of the Mumble server is set with `icesecretwrite` in `/etc/mumble-server.ini`. Set the same secret in the configuration file for Chrooms. (Note that `icesecretwrite` must be commented out if you want the Mumble server to require no password.)
0. Chooms is turned on and off with the following commands in the TF2 server console:

 * `es_load chrooms`
 * `es_unload chrooms`
 * `es_reload chrooms`

 To load Chrooms automatically when the TF2 server starts, put the first of these commands in `tf/cfg/autoexec.cfg`.
0. Play on the TF2 server using the same username as in Mumble. (You don't need to match upper and lower cases, though.)
