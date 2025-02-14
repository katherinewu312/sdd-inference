from pysdd.sdd import SddManager, Vtree, WmcManager
vtree = Vtree(var_count=10, var_order=[1,2,3,4,5,6,7,8,9,10], vtree_type="balanced")
sdd = SddManager.from_vtree(vtree)
a, b, c, d, e, f, g, h, i, j = sdd.vars

# Build SDD for formula
formula = (a & b & c & d & e) | (f & g & h & i & j)

# Model Counting
wmc = formula.wmc(log_mode=False)
print(f"Model Count: {wmc.propagate()}")
wmc.set_literal_weight(a, 0.1)
wmc.set_literal_weight(b, 0.2)
wmc.set_literal_weight(c, 0.3)
wmc.set_literal_weight(d, 0.4)
print(f"Weighted Model Count: {wmc.propagate()}")

# Visualize SDD and Vtree
with open("sdd.dot", "w") as out:
    print(formula.dot(), file=out)
with open("vtree.dot", "w") as out:
    print(vtree.dot(), file=out)

# Minimize SDD:
