# ass4

# import ai library for constraint satisfaction problems (CSP) for timetable
from constraint import Problem, AllDifferentConstraint

# library installation command
"""
pip install python-constraint
"""

problem = Problem()
# decalre variables,domains and constraints for timetable
classes = ["AI", "ML", "OS"]
timeslots = ["9AM", "10AM", "11AM", "1PM"]

# add variables and their domains
classV = {
    'AI': "MR_RVSIR",
    'ML': "MR_MVSIR",
    'OS': "MR_OVSIR",
}

for cls in classes:
    problem.addVariable(cls, timeslots)

# add constraint that all classes must be in different timeslots
problem.addConstraint(AllDifferentConstraint(), classes)

# get solutions
solutions = problem.getSolutions()

print(f"Total solutions found: {len(solutions)}\n")
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for cls, time in solution.items():
        print(f"  {cls} ({classV[cls]}): {time}")
    print()

# expected output:
"""
Total solutions found: 24

Solution 1:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 10AM

Solution 2:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 9AM

Solution 3:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 11AM

Solution 4:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 9AM

Solution 5:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 10AM

Solution 6:
  AI (MR_RVSIR): 1PM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 11AM

Solution 7:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 9AM

Solution 8:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 10AM

Solution 9:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 1PM

Solution 10:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 9AM

Solution 11:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 10AM

Solution 12:
  AI (MR_RVSIR): 11AM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 1PM

Solution 13:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 9AM

Solution 14:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 1PM

Solution 15:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 11AM

Solution 16:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 9AM

Solution 17:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 1PM

Solution 18:
  AI (MR_RVSIR): 10AM
  ML (MR_MVSIR): 9AM
  OS (MR_OVSIR): 11AM

Solution 19:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 1PM

Solution 20:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 10AM
  OS (MR_OVSIR): 11AM

Solution 21:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 10AM

Solution 22:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 11AM
  OS (MR_OVSIR): 1PM

Solution 23:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 11AM

Solution 24:
  AI (MR_RVSIR): 9AM
  ML (MR_MVSIR): 1PM
  OS (MR_OVSIR): 10AM
"""