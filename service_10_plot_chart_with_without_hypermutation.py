import matplotlib.pyplot as plt
from pathlib import Path
import uuid

def plot_with_without_hypermutation(data): ####
    figure_path = Path(str(uuid.uuid4())+'.png').absolute()
    _, ax =  plt.subplots(figsize=(12, 6))
    x = 0

    mutations_per_patient = data[x]
    x = x + 1
    mutations_per_patient_count = list(mutations_per_patient.values())
    mutations_per_patient_count = sorted(mutations_per_patient_count, reverse=True)
    x_axis = list(range(0, len(mutations_per_patient_count)))
    ax.bar(x_axis, mutations_per_patient_count, width=1.0, facecolor='dimgray', edgecolor='dimgray')
    ax.set_xticks([])     

    ax.set_xlabel("patients")
    ax.set_title("Original")
    #a.set_title("Preprocessed") ###is it rigth???????

    plt.tight_layout(h_pad=2.5, w_pad=1)

    plt.savefig(figure_path, format='png', dpi=500)
    plt.show()
    return figure_path