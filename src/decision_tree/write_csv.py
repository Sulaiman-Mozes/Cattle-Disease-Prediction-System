import csv

data = [1,0,1,0,0,1]

writer = csv.writer(open("data.csv", "w+"))
writer.writerow(["fever", "loss_app", "red_eyes", "low_milk", "rot_foot", "rot_mouth"])
writer.writerow(data)


'''
#with open("train.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
'''
