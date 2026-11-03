# Implementing a 5 qubit Quantum Fourier Transform

from qiskit import QuantumCircuit, transpile  # Imports QuantumCircuit to create circuits and transpile to convert circuits into simulator-compatible instructions
from qiskit.circuit.library import QFTGate  # Imports QFTGate to perform Quantum Fourier Transform
from qiskit_aer import AerSimulator  # Imports AerSimulator to simulate quantum circuits

# Step 1: Create a circuit with 5 qubits and 5 classical bits
n = 5  # Defines the number of qubits as 5
qc = QuantumCircuit(n, n)  # Creates a quantum circuit with 5 qubits and 5 classical bits

# Step 2: Prepare the input state |00001>
qc.x(0)  # Applies Pauli-X gate to qubit 0 to change its state from 0 to 1

# Step 3: Apply the 5-qubit Quantum Fourier Transform
qc.append(QFTGate(n), range(n))  # Applies the 5-qubit Quantum Fourier Transform to all 5 qubits

# Step 4: Measure all qubits
qc.measure(range(n), range(n))  # Measures all 5 qubits and stores results in classical bits

# Step 5: Display the circuit
print("5-Qubit QFT Circuit:")
print(qc.draw())

# Step 6: Create a quantum simulator
simulator = AerSimulator()  # Creates a simulator to execute the quantum circuit

# Step 7: Transpile the circuit
compiled_circuit = transpile(qc, simulator)  # Converts the circuit into instructions supported by the simulator

# Step 8: Execute the circuit
job = simulator.run(compiled_circuit, shots=1024)  # Executes the circuit 1024 times and stores the job

# Step 9: Collect measurement results
result = job.result()  # Retrieves the execution results
counts = result.get_counts()  # Extracts measurement counts for each binary outcome

# Step 10: Display the results
print("\nMeasurement Results:")
print(counts)
