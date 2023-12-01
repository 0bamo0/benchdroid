import time

startTime = time.time()
i = 0
while(i < 10000000):
    i = i + 1
result = time.time() - startTime

file_path = "results.txt"

with open(file_path, "a") as file:
    file.write(str(result) + "\n")

print(f"Result appended to {file_path}")
