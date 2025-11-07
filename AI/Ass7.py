# Simple Block World Planner (80% shorter!)
from collections import deque

def get_actions(x, y=None):
    """Generate all possible actions for blocks."""
    if y:
        return [
            (f"STACK({x},{y})", 
             {f"HOLDING({x})", f"CLEAR({y})"}, 
             {f"ON({x},{y})", f"CLEAR({x})", "ARMEMPTY"}, 
             {f"HOLDING({x})", f"CLEAR({y})"}),
            
            (f"UNSTACK({x},{y})", 
             {f"ON({x},{y})", f"CLEAR({x})", "ARMEMPTY"}, 
             {f"HOLDING({x})", f"CLEAR({y})"}, 
             {f"ON({x},{y})", "ARMEMPTY", f"CLEAR({x})"}),
        ]
    else:
        return [
            (f"PICKUP({x})", 
             {f"ONTABLE({x})", f"CLEAR({x})", "ARMEMPTY"}, 
             {f"HOLDING({x})"}, 
             {f"ONTABLE({x})", "ARMEMPTY", f"CLEAR({x})"}),
            
            (f"PUTDOWN({x})", 
             {f"HOLDING({x})"}, 
             {f"ONTABLE({x})", f"CLEAR({x})", "ARMEMPTY"}, 
             {f"HOLDING({x})"}),
        ]

def plan_blocks(start, goal, blocks=['A', 'B', 'C']):
    """Simple BFS planner for block world."""
    queue = deque([(frozenset(start), [])])
    visited = {frozenset(start)}
    
    while queue:
        state, path = queue.popleft()
        
        # Goal check
        if goal.issubset(state):
            return path
        
        # Try all actions
        for b1 in blocks:
            # Single block actions (PICKUP, PUTDOWN)
            for action_name, pre, add, delete in get_actions(b1):
                if pre.issubset(state):
                    new_state = (state - delete) | add
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [action_name]))
            
            # Two block actions (STACK, UNSTACK)
            for b2 in blocks:
                if b1 != b2:
                    for action_name, pre, add, delete in get_actions(b1, b2):
                        if pre.issubset(state):
                            new_state = (state - delete) | add
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, path + [action_name]))
    
    return None

# Main
if __name__ == "__main__":
    initial = {
        "ON(C,A)", "ONTABLE(A)", "ONTABLE(B)", 
        "CLEAR(C)", "CLEAR(B)", "ARMEMPTY"
    }
    
    goal = {
        "ON(A,B)", "ONTABLE(B)", "ONTABLE(C)", "ARMEMPTY"
    }
    
    print("="*50)
    print("SIMPLE BLOCK WORLD PLANNER")
    print("="*50)
    print("\nInitial:", sorted(initial))
    print("Goal:   ", sorted(goal))
    print("\nSearching...\n")
    
    plan = plan_blocks(initial, goal)
    
    if plan:
        print("✓ Plan Found!\n")
        for i, step in enumerate(plan, 1):
            print(f"{i}. {step}")
    else:
        print("✗ No solution found")


# expected output:
"""
==================================================
SIMPLE BLOCK WORLD PLANNER
==================================================

Initial: ['ARMEMPTY', 'CLEAR(B)', 'CLEAR(C)', 'ON(C,A)', 'ONTABLE(A)', 'ONTABLE(B)']
Goal:    ['ARMEMPTY', 'ON(A,B)', 'ONTABLE(B)', 'ONTABLE(C)']

Searching...

✓ Plan Found!

1. UNSTACK(C,A)
2. PUTDOWN(C)
3. PICKUP(A)
4. STACK(A,B)
"""