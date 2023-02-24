# customer_list.py

from customer import Customer

def main():
    # create and print two customers
    cust1 = Customer("John Smith", "1 Oak St.")
    cust2 = Customer("Sally Brown", "3 Elm St.")
    print(cust1.getName() + ", " +
          cust1.getStrAddr() + ", " +
          str(cust1.getCreationDate()))
    print(cust2.getName() + ", " +
          cust2.getStrAddr() + ", " +
          str(cust2.getCreationDate()))

if __name__ == "__main__":
    main()
