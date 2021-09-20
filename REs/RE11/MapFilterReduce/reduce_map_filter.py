from functools import reduce
def reduce_map_filter(args):
    if type(args[2]) is tuple:
        args = (args[0],args[1],reduce_map_filter(args[2]))
    if args[0] == 'map':
        result = list(map(args[1],args[2]))
        return result
    elif args[0] == 'filter':
        result = list(filter(args[1],args[2]))
        return result
    elif args[0] == 'reduce':
        result = reduce(args[1],args[2])
        return result