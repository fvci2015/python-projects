class PaymentReceipt:
    def __init__(self, customer_name, amount, payment_method):
        self.customer_name = customer_name
        self.amount = amount
        self.payment_method = payment_method

    def generate_receipt(self):
        receipt = f"""
        Payment Receipt
        -----------------
        Customer Name: {self.customer_name}
        Amount: ${self.amount:.2f}
        Payment Method: {self.payment_method}
        -----------------
        Thank you for your payment!
        """
        return receipt

def main():
    customer_name = input("Enter customer name: ")
    amount = float(input("Enter payment amount: "))
    payment_method = input("Enter payment method: ")

    receipt = PaymentReceipt(customer_name, amount, payment_method)
    print(receipt.generate_receipt())

if __name__ == "__main__":
    main()