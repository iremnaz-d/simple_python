
'''dictionary = {"INFO":0,
        "ERROR":0,
        "WARNING":0}'''

if __name__ == '__main__':
    dictionary ={}

    try:
        with open("server.txt", "r") as file: #with open ile dosyayı kapamaya gerek kalmaz
         for line in file:
            fileList = line.split(" - ")
            log_type = fileList[1] #split zaten string olarak döndürür, str dönüşümüne gerek yok

            if log_type in dictionary:
                dictionary[log_type] += 1
            else:
                dictionary[log_type] = 1 #key yoksa bile ekler



    except FileNotFoundError:
        print("File not found")

    print(dictionary)
