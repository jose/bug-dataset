
def is_checkout(task):
    if task == "checkout":
        return True
    return False


def is_test(task):
    if task == "test":
        return True
    return False


def is_info(task):
    if task == "info":
        return True
    return False


def is_per_test(task):
    if task == "per-test":
        return True
    return False


def is_coverage(task):
    if task == "coverage":
        return True
    return False


def is_coverage_per_test(task):
    if task == "coverage-per-test":
        return True
    return False
