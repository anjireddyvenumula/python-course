# methods_attributes.py
# Attributes store data, methods add behavior that uses that data.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds: balance is {self.balance}")
            return False
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return True

    # __str__ controls what print() shows
    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"


account = BankAccount("Ada", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(500)
print(account)
print("History:", account.history)


# A chat history class, similar to what you use with AI models
class Conversation:
    def __init__(self, system_prompt):
        self.messages = [{"role": "system", "content": system_prompt}]

    def add_user(self, text):
        self.messages.append({"role": "user", "content": text})

    def add_assistant(self, text):
        self.messages.append({"role": "assistant", "content": text})

    def last_message(self):
        return self.messages[-1]["content"]

    def __len__(self):
        return len(self.messages)


chat = Conversation("You are a helpful assistant.")
chat.add_user("What is Python?")
chat.add_assistant("A popular programming language.")
print("Messages:", len(chat))
print("Last:", chat.last_message())
for message in chat.messages:
    print(f"  {message['role']}: {message['content']}")

# Try it:
# 1. Add a get_statement() method to BankAccount that prints every history item.
# 2. Add a clear() method to Conversation that keeps only the system prompt.
