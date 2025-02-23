from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator

# Step 1: Map the Problem to a quantum-native format
def bell_state():

    # Create new circuit with 2 qubits
    qc = QuantumCircuit(2)

    # Add Hamard Gate to qubit 0
    qc.h(0)

    # Perform a controlled-X gate on qubit 1, controlled by qubit 0
    qc.cx(0, 1)

    # Return a drawing of the circuit using MatPlotLib ("mpl")
    # Remove "mpl" to get a text drawing
    # qc.draw("mpl")
    print(qc.draw())

    """
    When creating quantum circuits, one must also consider the type of data to be returned.
    Qiskit provides two ways to return data:
        - obtain a probability distribution for a set of qubits, or
        - obtain the expectation value of an observable
    Prepare the workload to measure the circuit in one of these two ways with Qiskit Primitives
    (explained in detail in step 3)
    """

    """
    This example measures expectation values by using the 'qiskit.quantum_info submodule,
    which is specified using operators. The following code creates 6 two-qubit Pauli operators:"""
    
    # Set up 6 different observables
    observable_labels = ["IZ", "IX", "ZI", "XI", "ZZ", "XX"]
    observables = [SparsePauliOp(label) for label in observable_labels]

# Step 2: Optimize the circuits and operators











if __name__ == "__main__":
    bell_state()