import csv


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            print(dict(row))
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print('Total sales: {}'.format(total))
    months = len(data)
    average = total / months
    print('average sales: {}'.format(average))
    lowest_sales = min(sales)
    print('lowest_sales:{}'.format(lowest_sales))
    highest_sales = max(sales)
    print('highest_sales:{}'.format(highest_sales))
    percentage_changes = []
    for i in range(1, len(data)):
        current_month = int(data[i]['sales'])  # Get the sales value for the current month
        previous_month = int(data[i - 1]['sales'])  # Get the sales value for the previous month
        monthly_change = current_month - previous_month
        percentage_change = (monthly_change / previous_month) * 100
        percentage_changes.append(percentage_change)
    for i, percentage_change in enumerate(percentage_changes):
        print('Percentage change for month {}: {}%'.format(i + 2, percentage_change))
        # Use *args when you have a variable number of arguments (like for calculating a sum from one or more values).


run()

# checking that the push path works
