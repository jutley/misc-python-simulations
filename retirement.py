import numpy
import math

# Edit these values as appropriate
starting_savings=1000000
annualized_returns=0.07
stddev=0.10
annual_contributions=19000+6000+3500
starting_age=27
retirement_age=65
target=5000000

# An array with the percentage of the max annual contribution across accounts per year
yearly_contribution_percentages = [1.0] * 100 + [0] * 100

trials=10000

def trial():
  savings = starting_savings
  returns = numpy.random.normal(annualized_returns, stddev, retirement_age - starting_age)
  for i in range(retirement_age - starting_age):
    annual_return = returns[i]
    multiplier = 1 + annual_return
    savings *= multiplier
    savings += annual_contributions * yearly_contribution_percentages[i]
  return savings

results=[]
for i in range(trials):
  results.append(trial())

successes=0
for r in results:
  if r > target:
    successes += 1

print(successes / trials)

