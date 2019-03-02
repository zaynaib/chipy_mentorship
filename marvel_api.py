import requests

r =requests.get('https://github.com/zaynaib')
print('This response is from github',r.status_code)



'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the 
'''