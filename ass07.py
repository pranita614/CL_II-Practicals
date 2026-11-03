from qiskit import QuantumCircuit  # Imports QuantumCircuit to create quantum circuits
from qiskit_aer import AerSimulator  # Imports AerSimulator to simulate quantum circuits
from qiskit_aer.noise import NoiseModel, pauli_error  # Imports tools to create and apply quantum noise

# Create 3-qubit repetition code for logical 0 = 000
circuit = QuantumCircuit(3, 3)  # Creates a quantum circuit with 3 qubits and 3 classical bits

# Create 10% bit-flip noise
noise_model = NoiseModel()  # Creates an empty noise model
bit_flip_error = pauli_error([("X", 0.1), ("I", 0.9)])  # Creates 10% probability of bit-flip (X) error and 90% probability of no error (I)
noise_model.add_all_qubit_quantum_error(bit_flip_error, ["id"])  # Applies the noise model to identity gates on all qubits

# Apply identity gates where noise can occur
for qubit in range(3):  # Loops through all 3 qubits
    circuit.id(qubit)  # Applies an identity gate to the current qubit

# Measure all qubits
circuit.measure(range(3), range(3))  # Measures all 3 qubits and stores results in classical bits

print(circuit.draw())

# Run noisy simulation
simulator = AerSimulator(noise_model=noise_model)  # Creates a simulator with the specified noise model
counts = simulator.run(circuit, shots=1000).result().get_counts()  # Executes the circuit 1000 times and collects measurement counts

# Majority-vote error correction
decoded_counts = {"0": 0, "1": 0}  # Creates a dictionary to count decoded logical 0 and 1 results

for measured_bits, count in counts.items():  # Loops through measurement results and their occurrence counts
    decoded_bit = "0" if measured_bits.count("1") < 2 else "1"  # Uses majority voting: fewer than 2 ones means logical 0, otherwise logical 1
    decoded_counts[decoded_bit] += count  # Adds the measurement count to the corresponding decoded logical bit

corrected_bit = max(decoded_counts, key=decoded_counts.get)  # Selects the logical bit with the highest count

print("Original logical bit: 0")
print("Noisy measurement counts:", counts)
print("Decoded counts:", decoded_counts)
print("Corrected logical bit:", corrected_bit)