# Implementations of 16 Qubit Random Number Generator

from qiskit import QuantumCircuit  # Imports QuantumCircuit to create quantum circuits
from qiskit_aer import AerSimulator  # Imports AerSimulator to simulate quantum circuits

# Create 16 qubits and 16 classical bits
qc = QuantumCircuit(16, 16)  # Creates a quantum circuit with 16 quantum bits and 16 classical bits

# Apply Hadamard gate to all qubits
qc.h(range(16))  # Applies Hadamard gate to all 16 qubits to create equal superposition

# Measure all qubits
qc.measure(range(16), range(16))  # Measures all qubits and stores their results in classical bits

# Display the quantum circuit
print(qc.draw())

# Create simulator
simulator = AerSimulator()  # Creates a simulator to execute the quantum circuit

# Run the circuit once
result = simulator.run(qc, shots=1).result()  # Executes the circuit once and stores the result

# Get the measurement result
counts = result.get_counts()  # Retrieves the measurement result as a dictionary

# Get the 16-bit random number
binary = list(counts.keys())[0]  # Extracts the generated 16-bit binary number from the result

# Convert binary to decimal
decimal = int(binary, 2)  # Converts the binary number into a decimal number

print("Random Binary Number :", binary)
print("Random Decimal Number:", decimal)
