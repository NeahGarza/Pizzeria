import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzas.settings")

import django 
django.setup()

from MainApp.models import Pizza, Topping

pizzas = Pizza.objects.all()
top = Topping.objects.get(id=1)
print(top)

t_type = top.entry_set.all()
for topping in toppings:
    print(t_type)

profile = Profile.objects.get(user=1)
    
"""


for t in topics:
    print(f"Topic ID: {t.id}    Topic: {t}")

entries = Entry.objects.all()

for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Text: {e}")
    print(f"Date added: {e.date_added}")
    print()

"""