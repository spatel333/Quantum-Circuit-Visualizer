from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_vector
import matplotlib as plt

qc = QuantumCircuit(1)

qc.h(0)
qc.sa

print("Quantum Circuit:")
print(qc.draw())



simulator = AerSimulator()

job = simulator.run(qc)
result = job.result()

# print(result)

statevector = result.get_statevector()
print(f'Statevector: {statevector}')

bloch_vector = [2 * statevector[0].real, 2 * statevector[1].real, 2 * (statevector[0].img - statevector[1].img)]

print("Visualizing on the Bloch Sphere:")
plot_bloch_vector(bloch_vector)
plt.show()