nested_list = [[i * j for j in range(1, 4)] for i in range(1, 4)]
sliced_list = [sublist[1:] for sublist in nested_list if
sum(sublist) > 5]
print(sliced_list)

for i in range(1,4):
    print(i)


class Base:
 def __init__(self):
    print("Base initialized")
class Derived(Base):
 def __init__(self):
    super().__init__()
    print("Derived initialized")
obj = Derived()
