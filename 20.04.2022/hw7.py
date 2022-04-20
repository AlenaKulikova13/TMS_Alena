
#При помощи ф-ии filter отфильтровать из кортежа слов только те, которые являются палиндромами

wds = ['refer', 'tree', 'civic', 'radar', 'level', 'state', 'kayak', 'reviver', 'racecar']
print(list(filter(lambda wds: wds == wds[::-1], wds)))