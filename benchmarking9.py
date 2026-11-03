from qiskit import QuantumCircuit, transpile  # Imports QuantumCircuit to create circuits and transpile to convert them into simulator-compatible instructions
from qiskit.quantum_info import random_clifford  # Imports random_clifford to generate random Clifford gates
from qiskit_aer import AerSimulator  # Imports AerSimulator to simulate quantum circuits
from qiskit_aer.noise import NoiseModel, depolarizing_error  # Imports tools to create a noise model and depolarizing error
import matplotlib.pyplot as plt  # Imports Matplotlib for plotting graphs

# Set up a small gate-noise model
noise_model = NoiseModel()  # Creates an empty quantum noise model
error = depolarizing_error(0.01, 1)  # Creates a 1% depolarizing error model for one qubit
noise_model.add_all_qubit_quantum_error(error, ["h", "s", "sdg"])  # Applies the noise to Hadamard, S and S-dagger gates on all qubits
simulator = AerSimulator(noise_model=noise_model)  # Creates a simulator using the specified noise model

sequence_lengths = [0, 2, 4, 8, 16, 32]  # Defines the different random sequence lengths to test
number_of_sequences = 20  # Sets the number of random circuits generated for each sequence length
shots = 256  # Sets the number of times each circuit is executed
survival_probabilities = []  # Creates an empty list to store survival probabilities

for length in sequence_lengths:  # Loops through each sequence length
    circuits = []  # Creates an empty list to store quantum circuits

    for _ in range(number_of_sequences):  # Generates 20 random sequences for each length

        # Apply a random sequence of Clifford gates
        sequence = QuantumCircuit(1)  # Creates a quantum circuit with one qubit
        for _ in range(length):  # Repeats the operation according to the sequence length
            clifford = random_clifford(1).to_circuit()  # Generates a random one-qubit Clifford operation and converts it into a circuit
            sequence.compose(clifford, inplace=True)  # Adds the random Clifford circuit to the sequence

        # Append the inverse so the ideal result returns to |0>
        circuit = QuantumCircuit(1, 1)  # Creates a circuit with one qubit and one classical bit
        circuit.compose(sequence, inplace=True)  # Adds the random Clifford sequence to the circuit
        circuit.compose(sequence.inverse(), inplace=True)  # Adds the inverse sequence to return the ideal qubit state to |0>
        circuit.measure(0, 0)  # Measures qubit 0 and stores the result in classical bit 0
        circuits.append(circuit)  # Adds the completed circuit to the circuits list

    # Use the same gate set covered by the noise model
    circuits = transpile(circuits, basis_gates=["h", "s", "sdg"])  # Converts circuits into Hadamard, S and S-dagger basis gates
    results = simulator.run(circuits, shots=shots).result()  # Executes all circuits 256 times and collects the results

    zero_count = sum(result.get("0", 0) for result in results.get_counts())  # Adds the number of times measurement result 0 is obtained across all circuits
    survival = zero_count / (number_of_sequences * shots)  # Calculates the probability of measuring 0
    survival_probabilities.append(survival)  # Stores the calculated survival probability

print("Sequence lengths:     ", sequence_lengths)
print("Survival probabilities:", [round(value, 3) for value in survival_probabilities])

plt.plot(sequence_lengths, survival_probabilities, "o-")  # Plots sequence lengths against survival probabilities using circular markers and a line
plt.xlabel("Sequence length")  # Sets the X-axis label
plt.ylabel("Probability of measuring 0")  # Sets the Y-axis label
plt.title("Single-Qubit Randomized Benchmarking")  # Sets the graph title
plt.ylim(0, 1.05)  # Sets the Y-axis range from 0 to 1.05
plt.grid(True)  # Displays grid lines on the graph
plt.show()  # Displays the final graph
