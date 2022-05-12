def calculate_net(gross, vat=0.23):
    return gross / (1 + vat)


print(calculate_net(123))
print(calculate_net(123, 0.08))
print(calculate_net(50, 0.05))

net = calculate_net(50, 0.05)

print(f"{net:.2f}")  # Sformatuj string z dwoma miejscami po przecinku
