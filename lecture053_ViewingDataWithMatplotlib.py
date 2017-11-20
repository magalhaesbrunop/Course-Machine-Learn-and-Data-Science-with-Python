import matplotlib.pyplot as plt
import numpy

"""
salary = numpy.array([100, 200, 600, 300, 500, 400, 150])
print(salary, '\n')

#plt.plot(salary)
#plt.plot(salary, c='Red')
plt.plot(salary, c='Red', ls='--', marker='s')
plt.show()
"""

salaryCleaner = numpy.array([100, 200, 400, 300])
salaryLabourer = numpy.array([50, 300, 400, 450])
salaryProgrammer = numpy.array(([200, 250, 350, 700]))

plt.plot(salaryCleaner, c='Green', marker='s', ms=6, label='Salary Cleaner')
plt.plot(salaryLabourer, c='Red', ls='--', marker='^', ms=6, label='Salary Labourer')
plt.plot(salaryProgrammer, marker='o', ms=6, label='Salary Programmer')
plt.legend()
#plt.legend(loc='upper left')
#plt.legend(loc='upper right')
plt.show()
