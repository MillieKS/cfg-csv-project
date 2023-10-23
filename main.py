import csv


class SalesAnalyser:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = []

    def read_data(self):
        with open(self.data_file, 'r') as sales_csv:
            spreadsheet = csv.DictReader(sales_csv)
            self.data = list(spreadsheet)

    def run(self):
        data = self.data
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


if __name__ == "__main__":
    # Create an instance of the SalesAnalyzer class
    analyzer = SalesAnalyser('sales.csv')

    # Call the run method on the instance
    analyzer.read_data()
    analyzer.run()


