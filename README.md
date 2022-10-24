# Ren'Py Scripts Layout

I hope you healthy and happy, Ren'Py devs.

Ren'Py scripts form a call tree, or forest, or graphs, somehow.
When I tried to re-build a call tree from some Ren'Py scripts,
I found it a soul-crashing work.

And I, as a Prolog user, am aware of the power of Prolog that,
beyond its logical expressiveness, it's also a data-structure builder.

SWI-Prolog, version 8.4.1 for x64-win64, was used.

## Usage

Step 1, install a SWI-Prolog instance.

Step 2, execute `swipl` to enter its REPL interface, a command-line interface.

Step 3, consult a set of Ren'Py scripts.

    ```
    ?- renpy_scripts:layout("/path/to/a/renpy/game/root/folder", R).
    R = [
      "/path/to/a/renpy/game/root/folder/game/first_script.rpy",
      "/path/to/a/renpy/game/root/folder/game/second_script.rpy",
      |...
    ].
    ```
At this step, call-relations will be loaded, then the database is ready to be consulted.

Ren'Py dev uses `call some_label (arg1, arg2) from some_save_point` statement
to put save-point while calling some label.

So, at tep 4, you may want to consult the database to know one or more paths
going to some save-point.

    ```
    ?- renpy_scripts:python_save_point_path("some_save_point", Path).
    Path = "[u'sp_1',u'sp_2', ..., u'some_save_point']" ;
    Path = ...
    ...
    ```
    
And, as we know, call-branches in Ren'Py are not context-free.
In some sandbox game, more than one characters share the same scene, and
a great good call-tree analyzer tends to hold rich information written in
Ren'Py `if-else` conditional statements.

Though, my analyzer is just a sniffer with automatic listing, to
give you hints to suspicious parts. When you find a single path, that's good.
Bug if several paths are listed for a save-point, take care to find all conditions out.
