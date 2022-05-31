import pathlib

listpath = ["./yalefacesgif/subject01", "./yalefacesgif/subject02" , "./yalefacesgif/subject03" , "./yalefacesgif/subject04" , "./yalefacesgif/subject05" , "./yalefacesgif/subject06" , "./yalefacesgif/subject07" , "./yalefacesgif/subject08" , "./yalefacesgif/subject09" , "./yalefacesgif/subject10" , "./yalefacesgif/subject11" , "./yalefacesgif/subject12" , "./yalefacesgif/subject13" , "./yalefacesgif/subject14" , "./yalefacesgif/subject15"]
for i in range(len(listpath)) : 
    for path in pathlib.Path(listpath[i]).iterdir():
        if path.is_file():
            old_name, old_extension= path.stem, path.suffix
            directory = path.parent
            new_name = old_name + ".gif"
            path.rename(pathlib.Path(directory, new_name))
