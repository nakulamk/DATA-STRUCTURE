#include <iostream>
#include <string>

using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;

public:
    BankAccount(const string& accNumber, const string& accHolder, double initialBalance)
        : accountNumber(accNumber), accountHolder(accHolder), balance(initialBalance) {}

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << " into the account." << endl;
        } else {
            cout << "Invalid amount for deposit." << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn $" << amount << " from the account." << endl;
        } else {
            cout << "Invalid amount for withdrawal or insufficient balance." << endl;
        }
    }

    void showBalance() const {
        cout << "Account Holder: " << accountHolder << endl;
        cout << "Account Number: " << accountNumber << endl;
        cout << "Current Balance: $" << balance << endl;
    }

    void transfer(BankAccount& recipient, double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            recipient.balance += amount;
            cout << "$" << amount << " transferred to recipient's account." << endl;
        } else {
            cout << "Invalid amount for transfer or insufficient balance." << endl;
        }
    }
};

int main() {
    BankAccount account1("12345", "Alice", 1000);
    BankAccount account2("67890", "Bob", 1500);

    account1.showBalance();
    account1.deposit(500);
    account1.showBalance();
    account1.withdraw(200);
    account1.showBalance();

    account2.showBalance();
    account1.transfer(account2, 300);
    account1.showBalance();
    account2.showBalance();

    return 0;
}