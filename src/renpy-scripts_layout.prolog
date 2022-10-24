:- module(renpy_scripts, [layout/2,
                          python_save_point_path/2]).

layout(Folder, Layout) :-
    is-string(Folder),
    exists_directory(Folder),
    !,
    string_concat(Folder, "/game/", Game_folder),
    rpy-files(Game_folder, Files0),
    os-spec-files(Game_folder, Files0, Files),
    (   % renpy_scripts:label_head(?Label)
        % . . . a running label head.
        abolish(renpy_scripts:label_head/1),
        % renpy_scripts:call_from(?Calling_label, ?Called_label, ?Save_point)
        abolish(renpy_scripts:call_from/3),
        asserta(renpy_scripts:label_head(undefined)),
        foreach(member(File, Files),
                collect-symbols(File))
    ),
    Layout = Files.

python_save_point_path(Save_point, String) :-
    call-path-to(Save_point, Path),
    python-save_point-list(Path, String).

put-label-head(Line) :-
    split_string(Line, "\s(", "\s\t", ["label",Label|_]),
    !,
    abolish(renpy_scripts:label_head/1),
    asserta(renpy_scripts:label_head(Label)).

collect-symbol(Line) :-
    split_string(Line, "\s", "\s\t", ["call",Called_label|Rest]),
    last(Rest, Save_point),
    renpy_scripts:label_head(Label_head),
    !,
    assertz(renpy_scripts:call_from(Label_head, Called_label, Save_point)).

is-string(Term) :-
    forall(member(X,Term), number(X)).

rpy-files(Folder, Files) :-
    directory_files(Folder, Files0),
    findall(F,
            (member(F, Files0),
             string_concat(_, ".rpy", F)),
            Files).

os-spec-files(Folder, Files0, Files) :-
    findall(F,
            (member(E, Files0),
             string_concat(Folder, E, F0),
             prolog_to_os_filename(F0, F)),
            Files).

collect-symbols(Token) :-
    Token == rpy_in,
    !,
    read_line_to_string(Token, Line),
    (   Line == end_of_file
    ;   string_concat("label ", _, Line),
        put-label-head(Line),
        collect-symbols(Token)
    ;   sub_string(Line, B1, _, _, "call "),
        sub_string(Line, B2, _, _, " from "),
        B1 < B2,
        collect-symbol(Line),
        collect-symbols(Token)
    ;   collect-symbols(Token)
    ).
collect-symbols(File) :-
    is-string(File),
    exists_file(File),
    !,
    open(File, read, _, [alias(rpy_in),
                         newline(detect)]),
    collect-symbols(rpy_in),
    !,
    close(rpy_in, []).

call-path-to(Save_point, Path) :-
    \+ is_list(Save_point),
    !,
    renpy_scripts:call_from(C2, _, Save_point),
    call-path-to([(C2,Save_point)], Path).
call-path-to(Acc, Acc) :-
    [(C0,_S0)|_] = Acc,
    \+ renpy_scripts:call_from(_L2, C0, _S2),
    !.
call-path-to([(Calling_label,Save_point)|Acc], Path) :-
    renpy_scripts:call_from(C2, Calling_label, S2),
    call-path-to([(C2,S2),(Calling_label,Save_point)|Acc], Path).

python-save_point-list(Path, String) :-
    python-save_point-list_1(Path, String0),
    string_concat("[u'", String0, String2),
    string_concat(String2, "']", String).

python-save_point-list_1([], "").
python-save_point-list_1([(_Calling_label,Save_point)], Save_point) :- !.
python-save_point-list_1([(_Calling_label,Save_point)|Rest], String) :-
    python-save_point-list_1(Rest, String0),
    string_concat("',u'", String0, String2),
    string_concat(Save_point, String2, String).
