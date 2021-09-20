def file_finder(dirs,file_name):
    if dirs == file_name:
        return file_name   
    for subdir in dirs[1:]:
        result = file_finder(subdir,file_name)
        if result != None:
            return dirs[0] + '/' + result