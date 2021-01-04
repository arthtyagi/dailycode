inputString = 'arcticmonkeys'
results = dict()

for char in inputString:
    results[char] = results.get(char, 0) + 1

sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
result_string = "{"
for char, count in sorted_results:
    result_string = result_string + "'" + char + "' : " + str(count) + ", "
print(result_string[0:-2] + "}")
