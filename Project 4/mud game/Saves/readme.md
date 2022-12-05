```
Author: 
Description: This file gives a quick overview of how the saved game feature of this mud game server works.
```
1. This directory keeps all the various saved games of players connected to this mud game server.

2. A new save file is created when a user starts a new game. Subsequently, users can load thier saved
   game and continue their adventure.

3. Users can only have one saved game file, which is overwritten everytime a new save is initiated.

4. Saved games are created with the following structure "player_alias - datetime".
