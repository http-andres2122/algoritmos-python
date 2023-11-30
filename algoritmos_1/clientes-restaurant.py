class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.consumo = 0

    def realizar_pedido(self, monto):
        self.consumo += monto

    def calcular_pago(self):
        if self.consumo > 50000:
            descuento = 0.2  # 20% de descuento
            total_pagar = self.consumo * (1 - descuento)
        else:
            total_pagar = self.consumo
        return total_pagar


def main():
    clientes = []

    # Registrar clientes
    num_clientes = int(input("Ingrese el número de clientes: "))
    for i in range(num_clientes):
        nombre_cliente = input(f"Ingrese el nombre del cliente {i + 1}: ")
        cliente = Cliente(nombre_cliente)
        clientes.append(clientes)

    # Registrar consumos
    for cliente in clientes:
        monto_consumo = float(input(f"Ingrese el monto de consumo para {cliente.nombre}: "))
        cliente.realizar_pedido(monto_consumo)

    # Mostrar pagos individuales y total
    total_pagos = 0
    for cliente in clientes:
        pago_cliente = cliente.calcular_pago()
        total_pagos += pago_cliente
        print(f"{cliente.nombre}: Pago = {pago_cliente:.2f}")

    print(f"\nTotal de todos los pagos: {total_pagos:.2f}")

if __name__ == "__main__":
    main()
