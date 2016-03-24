import json, sys
from decimal import Decimal

def convert_dict_to_playjson(json, indentation):
    if isinstance(json, dict):
        print "Json.obj()",
        indentation += 1
        for k, v in json.items():
            print ""
            print "\t" * indentation,
            if v is None:
                sys.stdout.write('.addNull("' + k + '")')
            else:
                sys.stdout.write('.add("' + k + '", ')
                convert_dict_to_playjson(v, indentation)
                sys.stdout.write(")")

        sys.stdout.write(".build()")
        indentation -= 1
    elif isinstance(json, list):
        print 'Json.arr()',
        indentation += 1
        for v in json:
            print ""
            print "\t" * indentation,
            sys.stdout.write('.add(')
            convert_dict_to_playjson(v, indentation)
            sys.stdout.write(")")

        sys.stdout.write(".build()")
        indentation -= 1
    elif isinstance(json, basestring):
        sys.stdout.write('"' + json.replace("\\", "\\\\") + '"')
    else:
        sys.stdout.write(str(json))
    return

try:
    decoded = json.loads(sys.argv[1], parse_float=Decimal)
    convert_dict_to_playjson(decoded, 0)
    print ""
except (ValueError, KeyError, TypeError):
    print "JSON format error"
