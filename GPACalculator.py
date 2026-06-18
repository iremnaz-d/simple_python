
if __name__ == '__main__':
    dic = {}
    with open("StudentGrades.txt", encoding = "utf-8") as file:
        for line in file:
            lineList = line.split(",")
            name = lineList[0]
            grade = int(lineList[2])
            if name in dic:
                dic[name].append(grade)
            else:
                dic[name] = [grade] # direkt list olarak başlatıyo

    # for key in dic:
    #     sum = 0
    #     for value in dic[key]:
    #         sum += value
    #     print(f"{key}'s GPA is {sum/len(dic[key])}")   bunların yerine aşağıdaki daha iyi

    for key, values in dic.items():
        print(f"{key}'s GPA is {sum(values)/len(values)}")

