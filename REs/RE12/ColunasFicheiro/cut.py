def cut(filename,delimiter,field):
    result = []
    resultline = []
    deflines = []
    f = open(filename)
    lines = f.read()
    lines = lines.split("\n")
    for line in lines:
        if line != "":
            deflines.append(line)
    if type(field) == int:
        for line in deflines:
            parts = line.split(delimiter)
            result += [parts[field-1]]
        result = "\n".join(result)
    elif type(field) == list:
        for line in deflines:
            parts = line.split(delimiter)
            resultline = []
            for idx in field:
                resultline += [parts[idx-1]]
            result += [delimiter.join(resultline)]
        result = "\n".join(result)
    return result