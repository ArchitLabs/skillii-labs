# A tiny expert system, written for this video: a rules engine and an inference engine.
# The rules are if-then rules a person wrote by hand. The inference engine applies
# them to the facts it is given, again and again, to deduce new facts.

RULES = [
    ({"has fur"}, "mammal"),
    ({"has feathers"}, "bird"),
    ({"mammal", "eats meat"}, "carnivore"),
    ({"carnivore", "has stripes"}, "tiger"),
    ({"bird", "cannot fly", "swims"}, "penguin"),
]


def infer(facts):
    known = set(facts)
    changed = True
    while changed:
        changed = False
        for needs, then in RULES:
            if needs <= known and then not in known:
                print(f"  rule: {' + '.join(sorted(needs))} -> {then}")
                known.add(then)
                changed = True
    print(f"  new facts: {len(known - set(facts))}")


# Inside its domain: one deduced fact leads to the next.
print("case 1: has fur, eats meat, has stripes")
infer(["has fur", "eats meat", "has stripes"])

# Outside its domain: no rule fits, so it deduces nothing.
print("case 2: has scales, lives in water")
infer(["has scales", "lives in water"])
