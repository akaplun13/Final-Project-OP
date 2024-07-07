import csv

data_sources = []


def add_new_data_source():
    file_path = input("Enter data source file path: ").strip()
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            records = sum(1 for record in headers)
            revenue = 0
            gross_profit = 0
            for row in reader:
                revenue += int(row[8])
                gross_profit += int(row[10])

        print(f"Datasource structure: {', '.join(headers)}")
        print(f"Total records: {records}")

        data_sources.append({'file_path': file_path, 'records': records, 'revenue': revenue,
                             'grossProfit': gross_profit, 'metric': None})
        print('\n\n\n\n\n', data_sources)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

# частина Даші закомічена з мого акаунту
    def check_existing_information():
        print("\nExisting Information:")
        for i, source in enumerate(data_sources, start=1):
            metric_info = f"Metric: {source['metric']}" if source['metric'] else "Metric: Not calculated"
            print(f"{i}) Datasource: {source['file_path']} | {metric_info}")


def calculate_metric():
    if not data_sources:
        print("No data sources available. Please add a data source first.")
        return

    print("\nSelect data source:")
    for i, source in enumerate(data_sources, start=1):
        print(f"{i}. {source['file_path']}")

    try:
        choice = int(input("Select data source: ").strip())
        if choice < 1 or choice > len(data_sources):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please select a valid data source number.")
        return

    selected_source = data_sources[choice - 1]

    try:
        total_revenue = 0
        total_gross_profit = 0
        for row in selected_source:
            try:
                total_revenue = int(selected_source['revenue'])
                total_gross_profit = int(selected_source['grossProfit'])
            except ValueError:
                print("Skipping a row due to invalid data.")

        if total_revenue == 0:
            print("Total revenue is zero. Cannot calculate Gross Profit Margin.")
            return

        gross_profit_margin = (total_gross_profit / total_revenue) * 100
        selected_source['metric'] = f"Gross Profit Margin = {gross_profit_margin:.2f}%"

        print(f"Based on the dataset, Gross Profit Margin was calculated. Value is: {gross_profit_margin:.2f}%")
    except KeyError:
        print("The dataset must contain 'revenue' and 'grossProfit' columns.")
