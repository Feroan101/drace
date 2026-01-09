from drace.constants import IGNORED_RULES, ONLY
from .z200 import z200, z201, z202, z227, z22_
from drace import utils

def rule_z2_series(lines: list[str], tree, file: str) -> list[dict]:
    results = []
    rules   = [z200, z202, z227] 
    methods = [lines, tree]

    for method, rule in zip(methods, rules):
        rule_name = (rule.__name__[-4:]).upper()
        if ONLY and rule_name not in ONLY: continue
        if rule_name in IGNORED_RULES: continue
        results.extend(rule.check(method, file))

    results.extend(z201.check(lines, tree, file))
    results.extend(z22_.check(lines, tree, file))

    return results
