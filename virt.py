import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

response_json = response.json()

print(response_json)


import pandas as pd

data = {'Имя': ['Егор', 'Анна', 'Никита','Марина'],
        'Возраст': [25, 35, 19, 33],
        'Город': ['Москва', 'Ростов', 'Калуга', 'Питер']}
df = pd.DataFrame(data)
print(df)

import numpy as np

a1 = np.array([1,3,4,5,6])
a2 = np.array([[1,2,4,5,9], [4,3,6,3,21]])
print(a1)
print(a2)



import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x,y)
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('График')
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.show()


from PIL import Image

ing = Image.open('C:\\worm\\1.jpg')
ing2 = ing.rotate(90)
ing2.save('new_1.jpg')
ing = ing.resize((ing.width//2, ing.height//2))
ing.save('new_2.jpg')
ing = ing.reduce(2)
ing.save('new_3.jpg')
ing.show()

print(ing.format, ing.size, ing.mode)

















