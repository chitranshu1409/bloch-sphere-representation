from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt 
from math import pi

# Step 1: Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Step 2: Apply different gates to the qubit and visualize the state on the Bloch Sphere

# Initial state (|0>), which is represented as [1, 0] on the Bloch Sphere
initial_state = [1, 0, 0]
plot_bloch_vector(initial_state)
plt.title("Initial State |0> on the Bloch Sphere")
plt.show()

# Step 3: Apply Hadamard Gate (H)
qc.h(0)
# After applying Hadamard, the state will be in a superposition (|+>) represented as [1/sqrt(2), 1/sqrt(2)]
hadamard_state = [1/2**0.5, 1/2**0.5, 0]
plot_bloch_vector(hadamard_state)
plt.title("State after Hadamard Gate (|+>) on the Bloch Sphere")
plt.show()

# Step 4: Apply Pauli-X Gate (X), which will flip the state from |+> to |1>
qc.x(0)
# Pauli-X gate will flip the state to |1>, represented as [0, 1]
x_state = [0, 1, 0]
plot_bloch_vector(x_state)
plt.title("State after Pauli-X Gate (|1>) on the Bloch Sphere")
plt.show()

# Step 5: Apply Pauli-Z Gate (Z), which will introduce a phase flip
qc.z(0)
# Pauli-Z gate will flip the phase of the |1> state, represented as [-1, 0]
z_state = [-1, 0, 0]
plot_bloch_vector(z_state)
plt.title("State after Pauli-Z Gate (|1> with phase flip) on the Bloch Sphere")
plt.show()
