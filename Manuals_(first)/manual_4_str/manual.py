apple = 'Яблочко красное'
print(apple[2])

print(apple[0: 11])
print(apple[0: 12])

lesson = 'Пифагоровы штаны во все стороны равны'
print(lesson.find('ш'))

print(lesson.rfind('а'))

name = input()
cat = 'Привет, ' + name + '! Как дела?'
print(cat)

name = input()
cat = "Привет, %s! Как дела?"
print(cat % name)

name = input()
robot = "Робот Федя"
cat = "Привет, %s! Я - %s."
print(cat % (name, robot))

name = input()
robot = "Робот Федя"
cat = f"Привет, {name}! Я - {robot}."
print(cat)

cat = f"Привет, {2 + 2}! Я - {99 // 11}."
print(cat)

doggy = "fvbtmgrienwdef9gjn4ie9fjevr9bni4ej0cvr9n143d0ecjv9nir" \
        "fvrin49e8vkrjb9in4feok@cvrj9nigmf403dkBejrv9nmg14fo30kevrj" \
        "4jgvrb9jmefin4gvr9j0km9oeinf4gvrkefmni4fegvr9jm9eoinf4gv" \
        "in4fgvr9jmno1 f4erv9jemfni4vr9jme9nief4vr9jk8efj9omnie@4gr" \
        "3ni4rv9jmenif4vr9j0k9emnif4vr9jekm9ndw9jd0kc9ovmrin end"
print(doggy.find('@'))

alex = "У Лукоморья дуб зеленый"
onion = alex[16:23] + " " + alex[2:5]
print(onion)
oak = "%s %s %s%s" % (alex[12:15], alex[13], alex[6:9], alex[10])
print(oak)
