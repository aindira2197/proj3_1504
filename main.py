student = {
    "name": "Ali",
    "marks": [80, 90, 85]
}

avg = sum(student["marks"]) / len(student["marks"])
print(avg)

text = "apple banana apple orange banana apple"

words = text.split()
d = {}

for w in words:
    d[w] = d.get(w, 0) + 1

print(d)
