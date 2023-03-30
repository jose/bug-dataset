import argument_parser
import myGit
import myInfo
import myTask
import myTest
import myCoverage

param_dict = argument_parser.arg_parser()

if myTask.is_info(param_dict["task"]):
    myInfo.get_project_info(param_dict)
    myInfo.get_bug_info(param_dict)
elif myTask.is_checkout(param_dict["task"]):
    myGit.checkout(param_dict)
elif myTask.is_test(param_dict["task"]):
    myTest.test()
elif myTask.is_per_test(param_dict["task"]):
    myTest.per_test()
elif myTask.is_coverage(param_dict["task"]):
    myCoverage.coverage()
elif myTask.is_coverage_per_test(param_dict["task"]):
    myCoverage.coverage_per_test()
