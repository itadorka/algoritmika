import random
noun = ['тыква', 'призрак', 'оборотень', 'смерть', 'кладбище', 'могила', 'дети']
verb = ['напугал', 'убил', 'вызвал', 'вырыл', 'охотились', 'ели']
adj = ['ужасающий', 'милый', 'уродливый', 'маленьки', 'злой', 'противный']

line = int(input())

for i in range(line):
    print(adj[random.randint(0, len(adj))], noun[random.randint(0, len(noun))], verb[random.randint(0, len(verb))], noun[random.randint(0, len(noun))])


