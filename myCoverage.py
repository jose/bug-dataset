import csv
import json
import os
import subprocess as sp
from myTest import *

#================= get coverage statistics =======================

def cov_stat_dump(cov_stat):
    cov_granularity = ["lines", "statements", "functions", "branches"]
    for gr in cov_granularity:
        print("Number of "+str(gr)+": "+str(cov_stat[gr]["total"]))
        print("\tcovered:\t"+str(cov_stat[gr]["covered"]))
        print("\tcovered (%):\t"+str(cov_stat[gr]["pct"]))
        print("\tskipped (%):\t"+str(cov_stat[gr]["skipped"]))


def get_cov_stat_from_god_json(json_data, type):
    cov_stat_of_type = {}
    cov_stat_of_type["total"] = json_data["total"][type]["total"]
    cov_stat_of_type["covered"] = json_data["total"][type]["covered"]
    cov_stat_of_type["skipped"] = json_data["total"][type]["skipped"]
    cov_stat_of_type["pct"] = json_data["total"][type]["pct"]
    return cov_stat_of_type


def _get_cov_stat(json_data):
    cov_stat = {}
    cov_stat["lines"] = get_cov_stat_from_god_json(json_data, "lines")
    cov_stat["statements"] = get_cov_stat_from_god_json(json_data, "statements")
    cov_stat["functions"] = get_cov_stat_from_god_json(json_data, "functions")
    cov_stat["branches"] = get_cov_stat_from_god_json(json_data, "branches")
    return cov_stat


def get_cov_stat():
    try:
        json_data = json.load( open("./coverage/coverage-summary.json") )
        cov_stat = _get_cov_stat(json_data)
        cov_stat_dump(cov_stat)
    except:
        pass


# ======================= tests + coverage =============

def coverage():
    param_dict = read_config()
    sp.call("rm -rf coverage/", shell=True)

    set_node_version(get_command(param_dict, "Node version"))

    if get_command(param_dict, "Pre-command").count(".sh")==0:
       run_pre_and_post_command(get_command(param_dict, "Pre-command"))
    run_npm_install()
    run_pre_and_post_command(get_command(param_dict, "Pre-command"))
    run_test_command(get_command(param_dict, "Test command"))
    get_test_stat()
    zip_test_results()

    run_coverage_command(get_command(param_dict, "Coverage command"))
    get_cov_stat()
    run_pre_and_post_command(get_command(param_dict, "Post-command"))


def coverage_per_test():
    param_dict = read_config()
    sp.call("rm -rf coverage/", shell=True)

    set_node_version(get_command(param_dict, "Node version"))

    run_npm_install()
    run_pre_and_post_command(get_command(param_dict, "Pre-command"))

    run_test_command(get_command(param_dict, "Test command"))
    get_test_stat()
    zip_test_results()

    run_pertest_command(get_command(param_dict, "Coverage command"))
    run_pre_and_post_command(get_command(param_dict, "Post-command"))
