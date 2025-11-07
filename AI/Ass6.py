# To run this code, you need to install the scikit-fuzzy library and its dependencies.
# You can install them using pip:
# pip install scikit-fuzzy networkx

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ===== STEP 1: Define Input Variables with Fuzzy Sets =====
# Temperature (0-50°C): Cold, Warm, Hot
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 25])
temperature['warm'] = fuzz.trimf(temperature.universe, [0, 25, 50])
temperature['hot'] = fuzz.trimf(temperature.universe, [25, 50, 50])

# Humidity (0-100%): Dry, Moderate, Humid
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
humidity['dry'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['moderate'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['humid'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# ===== STEP 2: Define Output Variable with Fuzzy Sets =====
# Fan Speed (0-100%): Slow, Medium, Fast
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')
fan_speed['slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['fast'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# ===== STEP 3: Define Fuzzy Rules =====
rule1 = ctrl.Rule(temperature['cold'] & humidity['dry'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['moderate'], fan_speed['slow'])
rule3 = ctrl.Rule(temperature['cold'] & humidity['humid'], fan_speed['medium'])
rule4 = ctrl.Rule(temperature['warm'] & humidity['dry'], fan_speed['slow'])
rule5 = ctrl.Rule(temperature['warm'] & humidity['moderate'], fan_speed['medium'])
rule6 = ctrl.Rule(temperature['warm'] & humidity['humid'], fan_speed['medium'])
rule7 = ctrl.Rule(temperature['hot'] & humidity['dry'], fan_speed['medium'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['moderate'], fan_speed['fast'])
rule9 = ctrl.Rule(temperature['hot'] & humidity['humid'], fan_speed['fast'])

# ===== STEP 4: Create Control System =====
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fan_simulation = ctrl.ControlSystemSimulation(fan_ctrl)

# ===== STEP 5: Test the System =====
# Test case: Temperature = 35°C, Humidity = 75%
fan_simulation.input['temperature'] = 35
fan_simulation.input['humidity'] = 75
fan_simulation.compute()

# Display result
print(f"Temperature: 35°C")
print(f"Humidity: 75%")
print(f"Recommended Fan Speed: {fan_simulation.output['fan_speed']:.2f}%")

# Try more test cases
print("\n--- More Test Cases ---")
test_cases = [(10, 30), (25, 50), (45, 90)]
for temp, humid in test_cases:
    fan_simulation.input['temperature'] = temp
    fan_simulation.input['humidity'] = humid
    fan_simulation.compute()
    print(f"Temp: {temp}°C, Humidity: {humid}% → Fan Speed: {fan_simulation.output['fan_speed']:.2f}%")

# expected output:

""">python Ass6.py
Temperature: 35°C
Humidity: 75%
Recommended Fan Speed: 54.18%

--- More Test Cases ---
Temp: 10°C, Humidity: 30% → Fan Speed: 41.22%
Temp: 25°C, Humidity: 50% → Fan Speed: 50.00%
Temp: 45°C, Humidity: 90% → Fan Speed: 67.25%

Temp: 10°C, Humidity: 30% → Fan Speed: 41.22%
Temp: 25°C, Humidity: 50% → Fan Speed: 50.00%
Temp: 45°C, Humidity: 90% → Fan Speed: 67.25%
"""