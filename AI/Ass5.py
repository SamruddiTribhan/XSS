"""
COMPUTER TROUBLESHOOTING EXPERT SYSTEM

This is a forward-chaining inference engine that diagnoses computer problems
based on user-provided symptoms. It uses a set of rules to infer solutions.

How it works:
1. User enters observed symptoms (problems)
2. The forward_chaining algorithm matches symptoms against rules
3. When rule premises match, conclusions (solutions) are inferred
4. Process repeats until no new inferences can be made
5. All inferred solutions are displayed to the user
"""

rules = [
    ([("problem", "power_light_off")],
     ("solution", "check_power_supply")),
    ([("problem", "computer_not_starting"), ("solution", "power_supply_ok")],
     ("solution", "check_RAM")),
    ([("problem", "blank_display"), ("solution", "power_supply_ok")],
     ("solution", "check_monitor_cable")),
    ([("problem", "computer_not_starting"), ("problem", "blank_display")],
     ("solution", "check_graphics_card")),
    ([("problem", "strange_beep")],
     ("solution", "check_motherboard")),
    ([("problem", "computer_not_starting"), ("problem", "strange_beep")],
     ("solution", "check_hard_disk")),
    ([("problem", "computer_not_starting"), ("solution", "RAM_ok")],
     ("solution", "check_operating_system")),
]

VALID_SYMPTOMS = ["computer_not_starting", "power_light_off", "blank_display", "strange_beep"]


def forward_chaining(facts, rules):
    """
    Forward-chaining inference engine.

    Args:
        facts (set): Initial set of known facts as tuples (category, value)
        rules (list): List of (premises, conclusion) tuples for inference

    Returns:
        set: All facts including original facts and inferred conclusions

    Algorithm:
    - Repeatedly applies rules to derive new facts
    - Stops when no new facts can be inferred
    """
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(premise in inferred for premise in premises) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True

    return inferred


if __name__ == "__main__":
    print("=" * 50)
    print("  COMPUTER TROUBLESHOOTING EXPERT SYSTEM")
    print("=" * 50)
    print("\nEnter the problems (symptoms) you observe.")
    print("\nAvailable symptoms:")
    for symptom in VALID_SYMPTOMS:
        print(f"  - {symptom}")
    print("\nType 'done' when finished entering symptoms.\n")

    # Collect user-provided symptoms
    facts = set()

    while True:
        symptom = input("Enter a symptom (or 'done'): ").strip().lower()

        if symptom == "done":
            break

        if symptom in VALID_SYMPTOMS:
            fact = ("problem", symptom)
            facts.add(fact)
            print(f"Added: {symptom}")
        else:
            print("Unknown symptom. Please choose from the list above.")

    if not facts:
        print("\nNo symptoms entered. Exiting.")
    else:
        # Run inference engine to derive solutions
        inferred_facts = forward_chaining(facts, rules)

        print("\n" + "=" * 50)
        print("DIAGNOSIS RESULTS")
        print("=" * 50)

        print("\nObserved Problems:")
        for fact in facts:
            print(f"  • {fact[1]}")

        print("\nSuggested Actions / Solutions:")
        solutions = [fact[1] for fact in inferred_facts if fact[0] == "solution"]
        if solutions:
            for solution in solutions:
                print(f" • {solution}")
        else:
            print("  No solution found. Please provide more symptoms.")

        print("\n" + "=" * 50)



# expected output:
"""
=================================================
  COMPUTER TROUBLESHOOTING EXPERT SYSTEM
==================================================

Enter the problems (symptoms) you observe.

Available symptoms:
  - computer_not_starting
  - power_light_off
  - blank_display
  - strange_beep

Type 'done' when finished entering symptoms.

Enter a symptom (or 'done'): blank_display
Added: blank_display
Enter a symptom (or 'done'):  strange_beep
Added: strange_beep
Enter a symptom (or 'done'): done

==================================================
DIAGNOSIS RESULTS
==================================================

Observed Problems:
  • strange_beep
  • blank_display

Suggested Actions / Solutions:
 • check_motherboard

==================================================

Available symptoms:
  - computer_not_starting
  - power_light_off
  - blank_display
  - strange_beep

Type 'done' when finished entering symptoms.

Enter a symptom (or 'done'): blank_display
Added: blank_display
Enter a symptom (or 'done'):  strange_beep
Added: strange_beep
Enter a symptom (or 'done'): done

==================================================
DIAGNOSIS RESULTS
==================================================

Observed Problems:
  • strange_beep
  • blank_display

Suggested Actions / Solutions:
 • check_motherboard

=================================================="""