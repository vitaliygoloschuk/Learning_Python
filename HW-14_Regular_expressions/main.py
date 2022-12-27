import re

emails = "director_rc@vsau.vin.ua" \
      "pr_tr@vsau.vin.ua" \
      "dep_rector@vsau.vin.ua"
check = re.search ("(\w+)@(\w+)?(\.)(\w+.)+" , emails)

if check:
  print("YES! We have a match!")
else:
  print("No match")