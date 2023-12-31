# exceptional handling
try:
    file = open("data.txt", mode='a')
    file.write("Today i've earn 100 rup!!")
except FileNotFoundError:
    file = open("data.txt", mode="w")
    file.write("We created a new file and this is out first text")
else:
    file = open("data.txt", mode='a')
    file.write("Today i've earn 1000 rup!!")
finally:
    file.close()
