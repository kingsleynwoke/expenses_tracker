from matplotlib import pyplot as plt
from sum_category import sum_category_expenses
from budget import check_budget

def plots():
    """
    Plots bar and pie chart for visualising summary of remaing
    balance and summary ofexpenses
    """
    #Create figures
    plt.style.use(['science', 'notebook', 'grid'])
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 1
    fig0, ax0 = plt.subplots(figsize=(10,8), tight_layout=True)
    fig1, ax1 = plt.subplots(figsize=(10,8), tight_layout=True)

    #Create values for plotting using the following functions
    sum_category_value = sum_category_expenses()
    check_budget_value = check_budget()

    bar_category = [key for key in check_budget_value.keys()]
    bar_values = [value for value in check_budget_value.values()]
    pie_category = [key for key in sum_category_value.keys()]
    pie_values = [value for value in sum_category_value.values()]

    print("\n###############################################################")
    print("     !!!  Plotting in progress, kindly check your screen  !!!     ")
    print("###############################################################\n")

    #Plotting begins here.
    #(1) Pie chart
    colors = ["steelblue", "peru", "olive", "silver", 
              "cadetblue", "dimgray", "sienna", "darkgreen"]
    ax0.pie(pie_values, labels=pie_category, autopct='%.1f%%', colors=colors,
            wedgeprops={'linewidth': 1.0, 'edgecolor': 'black'})
    ax0.set_title("Summary of expenses in percentage", fontsize=20, pad=20, color="r", fontweight="bold")
    
    #(2) Bar chart
    new_bar = ax1.bar(bar_category, bar_values, ec="black")
    ax1.set_title("Remaining balance", fontsize=20, pad=20, color="r", fontweight="bold")
    ax1.tick_params(rotation=45)
    ax1.set_xlabel("Categories", labelpad=15)
    ax1.set_ylabel("Expenses in Euros", labelpad=15 )
    ax1.bar_label(new_bar, padding=3, fontsize='x-large')
    ax1.margins(y=0.2)
    
    plt.show()
    fig0.savefig("expenses_pie_chart.jpg", dpi=200)
    fig1.savefig("expenses_bar_chart.jpg", dpi=200)

if __name__ == '__main__':
        plots()
