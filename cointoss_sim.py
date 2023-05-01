import random
import matplotlib.pyplot as plt
import statistics as stat

def toss():
    HeadOrTail : bool
    rand = random.randint(0,1)
    if rand == 0:
        HeadOrTail = False
    else:
        HeadOrTail = True
    return HeadOrTail

def sim(money : float, sim_round : int):
    money_list = [money]
    for i in range(sim_round):
        if toss() == False:
            money *= 0.5
        else:
            money *= 1.8
        money_list.append(round(money,1))
    return money_list

def sim_mean_median(money : float, sim_round : int):
    money_list = [money]
    for i in range(sim_round):
        if toss() == False:
            money *= 0.5
        else:
            money *= 1.8
        money_list.append(round(money,1))
    return stat.mean(money_list), stat.median(money_list)

def Big_sim(NumberOfPeople : int, money: float, sim_round : int):
    mean_list = []
    median_list = []
    for i in range(NumberOfPeople):
        mean, median = sim_mean_median(money,sim_round)
        mean_list.append(mean)
        median_list.append(median)
    return mean_list,median_list

# def plot(x_axis, y_axis, x_name:str, y_name:str):
#     plt.plot(x_axis,y_axis)
#     plt.xlabel(x_name)
#     plt.ylabel(y_name)
#     plt.show()

def main():
    People_list = []
    NumberOfPeople = 100
    init_money = 100
    sim_round = 100
    mean_count = 0
    median_count = 0
    mean_list,median_list = Big_sim(NumberOfPeople, init_money, sim_round)
    mean_mean = stat.mean(mean_list)
    median_mean = stat.mean(median_list)
    [People_list.append(i) for i in range(NumberOfPeople)]
    for i in mean_list:
        if i > mean_mean:
            mean_count += 1
    for i in median_list:
        if i > median_mean:
            median_count += 1
    print(f'mean percentage: {round(mean_count/NumberOfPeople*100, 2)}%, \nmedian percentage: {round(median_count/NumberOfPeople*100,2)}%')

    figure, (mean_plot, median_plot) = plt.subplots(1,2)
    plt.subplots_adjust(wspace=0.4)
    mean_plot.plot(People_list,sorted(mean_list))
    mean_plot.set_ylabel("mean")
    median_plot.plot(People_list,sorted(median_list))
    median_plot.set_ylabel("median")
    plt.show()


    # plot(People_list,sorted(mean_list),"number of people", "mean")
    # plot(People_list,sorted(median_list),"number of people", "median")

if __name__ == "__main__":
    main()