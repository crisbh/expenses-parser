import numpy as np
import pandas as pd


def read_expenses_spreadsheet(filename, commerce=""):
    """
    Read the spreadsheet provided by a given commerce.
    Returns as a pandas dataframe.
    """

    supported_commerce = ["CMR"]
    assert (
        commerce in supported_commerce
    ), f"Your spreadsheet type is not supported.\n \
        Supported types are: {supported_commerce}."

    # read by default 1st sheet of an excel file
    dfinput = pd.read_excel(filename)

    return dfinput


def get_transaction_type(dataframe):
    """
    Get the transaction type of each element in the spreadsheet df.
    """
    descripcion = dataframe["DESCRIPCION"]

    for i, transaction in enumerate(descripcion):
        transaction_split = transaction.split()
        if "COMPRA" in transaction_split:
            print(f"item {i} is a purchase")
        elif "PAGO" in transaction_split:
            print(f"item {i} is a payment")
        elif "UBER" in transaction_split:
            print(f"item {i} is a UBER")
        else:
            print(f"Transaction type of item {i} not known")


def get_expenditure_shop(dataframe, shop, verbose=False):
    """
    Get the total expenditure for a given shop.
    """
    descripcion = dataframe["DESCRIPCION"]
    valor = dataframe["VALOR CUOTA"]

    count = 0
    grand_total = 0

    for i, transaction in enumerate(descripcion):
        transaction_split = transaction.split()
        if shop in transaction_split:
            grand_total += valor[i]
            count += 1
            if verbose:
                print(f"item {i} is a from {shop}")
                print(f"Match found: {transaction} for {valor[i]}")

    if count > 0:
        print(f"-> Shopped {count} times at {shop} for a total of {grand_total}.")
        # print(f"-------------------------------------------------")

    return [grand_total, count]


def get_expenditure_shop_list(shop_lists):
    """
    Get the total expenditure for a list of shops, i.e. a category.
    """
    for i_list, shop_list in enumerate(shop_lists):
        print(f"Looking for {shop_list} ...\n")

        total_category = 0
        for i_shop, shop in enumerate(shop_list):
            total, count = get_expenditure_shop(dfinput, shop)
            total_category += total

        print(f"\n*****************************************************")
        print(f"** The grand total for this category is: {total_category}")
        print(f"*****************************************************\n")


spreadsheet_cmr = "mayo-2024.xlsx"
# spreadsheet_cmr = 'junio-2024.xlsx'
# spreadsheet_cmr = 'julio-2024.xlsx'

# TODO replace these inputs by parser

# read by default 1st sheet of an excel file
dfinput = read_expenses_spreadsheet(spreadsheet_cmr, "CMR")

shop_list_eat_out = np.loadtxt("shop_list_eatout.txt", dtype="str")
shop_list_groceries = np.loadtxt("shop_list_groceries.txt", dtype="str")
shop_list_retail = np.loadtxt("shop_list_retail.txt", dtype="str")
shop_list_pets = np.loadtxt("shop_list_pets.txt", dtype="str")
shop_list_transport = np.loadtxt("shop_list_transport.txt", dtype="str")

shop_lists = [
    shop_list_eat_out,
    shop_list_groceries,
    shop_list_retail,
    shop_list_pets,
    shop_list_transport,
]

# Get results from all lists
# identify_transaction_type(dfinput)
get_expenditure_shop_list(shop_lists)
