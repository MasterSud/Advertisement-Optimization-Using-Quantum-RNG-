from qiskit import *
import streamlit as st
from PIL import Image
import base64


def quantum_rng(num_qubits):
    circuit = QuantumCircuit(num_qubits, num_qubits)
    for i in range(num_qubits):
        circuit.h(i)
    circuit.measure(range(num_qubits), range(num_qubits))
    simulator = Aer.get_backend('aer_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    random_number = int(list(counts.keys())[0], 2)
    return random_number

main_bg = r"C:\Users\Admin\Desktop\bg.jpg"
main_bg_ext = "jpg"

side_bg = r"C:\Users\Admin\Desktop\bg.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("""Quantum Based Advertisement Optimizer""")
st.write("""
""")
st.write("""
""")
st.write("""
""")
num_qubits = 3
random_number1 = quantum_rng(num_qubits)
random_number2 = quantum_rng(num_qubits)
l=[]
dict1={0:r"C:\Users\Admin\Desktop\car.jpeg",1:r"C:\Users\Admin\Desktop\iphone.jpg",2:r"C:\Users\Admin\Desktop\dune2.jpg",3:r"C:\Users\Admin\Desktop\zara.jpg",4:r"C:\Users\Admin\Desktop\asuslaptop.jpg",5:r"C:\Users\Admin\Desktop\mcd.jpg",6:r"C:\Users\Admin\Desktop\re.jpg",7:r"C:\Users\Admin\Desktop\headset.jpg"}
dict2={0:'Starting at Rs 50 lakhs',1:'Latest model, starting at Rs 70 lakhs',2:'Releasing today in your nearest theatres',3:'Our lastest spring collections available now',4:'Starting at Rs 75,000',5:'Try our newest items in your nearest stores',6:'Starting at Rs 2 lakhs',7:'Get yourself our newest headsets'}
while sorted(l)!=list(range(0,8)):
    image1 = Image.open(dict1[random_number1])
    image2 = Image.open(dict1[random_number2])
    if random_number1 in l:
        random_number1 = quantum_rng(num_qubits)
    elif random_number2 in l:
        random_number2 = quantum_rng(num_qubits)
    else:
        if random_number1>random_number2:
            l.append(random_number1)
            l.append(random_number2)
            st.image(image1, caption=dict2[random_number1])
            st.divider()
            st.image(image2, caption=dict2[random_number2])
            st.divider()
        elif random_number1<random_number2:
            l.append(random_number1)
            l.append(random_number2)
            st.image(image2, caption=dict2[random_number2])
            st.divider()
            st.image(image1, caption=dict2[random_number1])
            st.divider()
        else:
            random_number2 = quantum_rng(num_qubits)