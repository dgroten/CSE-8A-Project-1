import csv

publisher = "Nintendo"

print("For the publisher " + publisher + ":" + "\n")

def avg_sales(publisher):
    # This function returns the average number of sales for a game published by a given publisher.
    with open("game_sales_data.csv", "r", encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        data = list(reader)
        sales = 0
        games = 0
        for i in range(len(data)):
            if data[i][3] == str(publisher):
                sales += float(data[i][7])
                games += 1
        return float(sales / games)
print("The average number of sales for a game published by " + publisher + " is " + str(avg_sales(publisher)) + " million.")

def avg_rank(publisher):
    # This function returns the average sales rank for a game published by a given publisher.
    with open("game_sales_data.csv", "r", encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        data = list(reader)
        rank = 0
        games = 0
        for i in range(len(data)):
            if data[i][3] == str(publisher):
                rank += int(data[i][0])
                games += 1
        return float(rank / games)
print("The average sales rank for a game published by " + publisher + " is " + str(avg_rank(publisher)) + ".")

def avg_critic(publisher):
    # This function returns the average critic score for a game published by a given publisher.
    with open("game_sales_data.csv", "r" , encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        data = list(reader)
        critic = 0
        games = 0
        for i in range(len(data)):
            if data[i][3] == str(publisher):
                if data[i][5] != '':
                    critic += float(data[i][5])
                    games += 1
        return float(critic / games)
print("The average critic score for a game published by " + publisher + " is " + str(avg_critic(publisher)) + ".")

def avg_user(publisher):
    # This function returns the average critic score for a game published by a given publisher.
    with open("game_sales_data.csv", "r" , encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        data = list(reader)
        user = 0
        games = 0
        for i in range(len(data)):
            if data[i][3] == str(publisher):
                if data[i][6] != '':
                    user += float(data[i][6])
                    games += 1
        return float(user / games)
print("The average user score for a game published by " + publisher + " is " + str(avg_user(publisher)) + "." + "\n")

publisher1 = "Nintendo"
publisher2 = "Sony Interactive Entertainment"
publisher3 = "Microsoft Game Studios"

print("Out of the three publishers " + publisher1 + ", " + publisher2 + ", and " + publisher3 + ":" + "\n")

def best_avg_sales(publisher1, publisher2, publisher3):
    # This function returns the publisher with the best average sales out of three given publishers.
    if avg_sales(publisher1) > avg_sales(publisher2) and avg_sales(publisher1) > avg_sales(publisher3):
        return publisher1
    elif avg_sales(publisher2) > avg_sales(publisher1) and avg_sales(publisher2) > avg_sales(publisher3):
        return publisher2
    else:
        return publisher3
print("The publisher with the best average sales is " + str(best_avg_sales(publisher1, publisher2, publisher3)) + " with an average sales number of " + str(avg_sales(best_avg_sales(publisher1, publisher2, publisher3))) + " million.")

def best_avg_rank(publisher1, publisher2, publisher3):
    # This function returns the publisher with the best average sales rank out of three given publishers.
    if avg_rank(publisher1) < avg_rank(publisher2) and avg_rank(publisher1) < avg_rank(publisher3):
        return publisher1
    elif avg_rank(publisher2) < avg_rank(publisher1) and avg_rank(publisher2) < avg_rank(publisher3):
        return publisher2
    else:
        return publisher3
print("The publisher with the best average sales rank is " + str(best_avg_rank(publisher1, publisher2, publisher3)) + " with an average sales rank of " + str(avg_rank(best_avg_rank(publisher1, publisher2, publisher3))) + ".")

def best_avg_critic(publisher1, publisher2, publisher3):
    # This function returns the publisher with the best average critic score out of three given publishers.
    if avg_critic(publisher1) > avg_critic(publisher2) and avg_critic(publisher1) > avg_critic(publisher3):
        return publisher1
    elif avg_critic(publisher2) > avg_critic(publisher1) and avg_critic(publisher2) > avg_critic(publisher3):
        return publisher2
    else:
        return publisher3
print("The publisher with the best average critic score is " + str(best_avg_critic(publisher1, publisher2, publisher3)) + " with an average critic score of " + str(avg_critic(best_avg_critic(publisher1, publisher2, publisher3))) + ".")

def best_avg_user(publisher1, publisher2, publisher3):
    # This function returns the publisher with the best average user score out of three given publishers.
    if avg_user(publisher1) > avg_user(publisher2) and avg_user(publisher1) > avg_user(publisher3):
        return publisher1
    elif avg_user(publisher2) > avg_user(publisher1) and avg_user(publisher2) > avg_user(publisher3):
        return publisher2
    else:
        return publisher3
print("The publisher with the best average user score is " + str(best_avg_user(publisher1, publisher2, publisher3)) + " with an average user score of " + str(avg_user(best_avg_user(publisher1, publisher2, publisher3))) + ".")

def ranking_avg_sales(publisher1, publisher2, publisher3):
    # This function returns a ranking of the publishers' average sales out of three given publishers.
    if avg_sales(publisher1) > avg_sales(publisher2) > avg_sales(publisher3):
        return [1, 2, 3]
    elif avg_sales(publisher1) > avg_sales(publisher3) > avg_sales(publisher2):
        return [1, 3, 2]
    elif avg_sales(publisher2) > avg_sales(publisher1) > avg_sales(publisher3):
        return [2, 1, 3]
    elif avg_sales(publisher2) > avg_sales(publisher3) > avg_sales(publisher1):
        return [3, 1, 2]
    elif avg_sales(publisher3) > avg_sales(publisher1) > avg_sales(publisher2):
        return [2, 3, 1]
    else:
        return [3, 2, 1]
    
def ranking_avg_rank(publisher1, publisher2, publisher3):
    # This function returns a ranking of the publishers' average sales rank out of three given publishers.
    # The best publisher is the one with the rank with the smallest number.
    if avg_rank(publisher1) < avg_rank(publisher2) < avg_rank(publisher3):
        return [1, 2, 3]
    elif avg_rank(publisher1) < avg_rank(publisher3) < avg_rank(publisher2):
        return [1, 3, 2]
    elif avg_rank(publisher2) < avg_rank(publisher1) < avg_rank(publisher3):
        return [2, 1, 3]
    elif avg_rank(publisher2) < avg_rank(publisher3) < avg_rank(publisher1):
        return [3, 1, 2]
    elif avg_rank(publisher3) < avg_rank(publisher1) < avg_rank(publisher2):
        return [2, 3, 1]
    else:
        return [3, 2, 1]

def ranking_avg_critic(publisher1, publisher2, publisher3):
    # This function returns a ranking of the publishers' average critic score out of three given publishers.
    if avg_critic(publisher1) > avg_critic(publisher2) > avg_critic(publisher3):
        return [1, 2, 3]
    elif avg_critic(publisher1) > avg_critic(publisher3) > avg_critic(publisher2):
        return [1, 3, 2]
    elif avg_critic(publisher2) > avg_critic(publisher1) > avg_critic(publisher3):
        return [2, 1, 3]
    elif avg_critic(publisher2) > avg_critic(publisher3) > avg_critic(publisher1):
        return [3, 1, 2]
    elif avg_critic(publisher3) > avg_critic(publisher1) > avg_critic(publisher2):
        return [2, 3, 1]
    else:
        return [3, 2, 1]

def ranking_avg_user(publisher1, publisher2, publisher3):
    # This function returns a ranking of the publishers' average user score out of three given publishers.
    if avg_user(publisher1) > avg_user(publisher2) > avg_user(publisher3):
        return [1, 2, 3]
    elif avg_user(publisher1) > avg_user(publisher3) > avg_user(publisher2):
        return [1, 3, 2]
    elif avg_user(publisher2) > avg_user(publisher1) > avg_user(publisher3):
        return [2, 1, 3]
    elif avg_user(publisher2) > avg_user(publisher3) > avg_user(publisher1):
        return [3, 1, 2]
    elif avg_user(publisher3) > avg_user(publisher1) > avg_user(publisher2):
        return [2, 3, 1]
    else:
        return [3, 2, 1]

def best_publisher():
    # This function calculates which publisher is the best out of three given publishers by adding up the rankings of each publisher in each category.
    # The best publisher is the one with the lowest score because a lower score means a higher ranking.
    score_publisher1 = int(ranking_avg_sales(publisher1, publisher2, publisher3)[0] + ranking_avg_rank(publisher1, publisher2, publisher3)[0] + ranking_avg_critic(publisher1, publisher2, publisher3)[0] + ranking_avg_user(publisher1, publisher2, publisher3)[0])
    score_publisher2 = int(ranking_avg_sales(publisher1, publisher2, publisher3)[1] + ranking_avg_rank(publisher1, publisher2, publisher3)[1] + ranking_avg_critic(publisher1, publisher2, publisher3)[1] + ranking_avg_user(publisher1, publisher2, publisher3)[1])
    score_publisher3 = int(ranking_avg_sales(publisher1, publisher2, publisher3)[2] + ranking_avg_rank(publisher1, publisher2, publisher3)[2] + ranking_avg_critic(publisher1, publisher2, publisher3)[2] + ranking_avg_user(publisher1, publisher2, publisher3)[2])
    if score_publisher1 < score_publisher2 and score_publisher1 < score_publisher3:
        return publisher1
    elif score_publisher2 < score_publisher1 and score_publisher2 < score_publisher3:
        return publisher2
    else:
        return publisher3
print("The best publisher is " + best_publisher() + ".")