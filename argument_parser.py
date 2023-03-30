import argparse
import sys
import os

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def arg_parser():
    parser = argparse.ArgumentParser(description = '   ')
    parser.add_argument('-p', '--project',  required = False, choices= get_projects(), help = '')
    parser.add_argument('-b', '--bug-ID',   required = False, help = '')
    parser.add_argument('-t', '--task',     required = True, choices = ['info', 'checkout', 'test', 'per-test', 'coverage', 'coverage-per-test'], help='')
    parser.add_argument('-v', '--version',  required = False, choices = ['buggy', 'fixed', 'fixed-only-test-change'], help='')
    parser.add_argument('-o', '--output',   required = False, help='output (clone, checkout etc) folder')

    param_dict = {}
    args = parser.parse_args()
    param_dict["task"] = args.task
    if param_dict["task"] == 'info' or param_dict["task"] == 'checkout':
        if args.project is None:
            eprint("[ERROR] -p/--project is not defined!")
            sys.exit(1)
        if args.bug_ID is None:
            eprint("[ERROR] -b/--bug-ID is not defined!")
            sys.exit(1)
        if args.version is None:
            eprint("[ERROR] -v/--version is not defined!")
            sys.exit(1)
        if args.output is None:
            eprint("[ERROR] -o/--output is not defined!")
            sys.exit(1)
        param_dict["project"] = args.project
        param_dict["bug-ID"] = args.bug_ID
        param_dict["version"] = args.version
        param_dict["output"] = args.output
    return param_dict


def get_projects():
    SCRIPTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))
    projects_set = set()
    projects_file = open(os.path.join(SCRIPTDIR, "Projects.csv"), "r")
    lines = projects_file.read().splitlines()
    for x in range(1, len(lines)):
        projects_set.add(lines[x].split(";")[0])
    projects_file.close()
    return list(projects_set)

