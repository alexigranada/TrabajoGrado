import numpy as np
import matplotlib.pyplot as plt

# Función para crear el diagrama de Taylor
def taylor_diagram(stddev, corrcoef, ref_stddev, fig=None):
    # Cálculo de la desviación estándar y la correlación para el modelo y las observaciones
    ref = ref_stddev
    theta = np.arccos(corrcoef)
    radii = stddev

    # Creación de la figura si no existe
    if fig is None:
        fig = plt.figure()

    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2.0)
    ax.set_ylim(0, 1.5 * ref)

    # Dibujar las observaciones
    ax.plot([0], [ref], 'ko', label='Observaciones')

    # Dibujar los modelos
    for (r, t) in zip(radii, theta):
        ax.plot(t, r, 'o', label=f'Modelo (σ={r:.2f}, ρ={np.cos(t):.2f})')

    # Añadir etiquetas y leyenda
    plt.legend()
    plt.title('Diagrama de Taylor')
    return fig

# Datos de ejemplo
observations_std = 1.0  # Desviación estándar de las observaciones
model_stds = [0.8, 1.1, 1.0]  # Desviaciones estándar de los modelos
model_corrs = [0.9, 0.85, 0.95]  # Correlaciones de los modelos

fig = taylor_diagram(model_stds, model_corrs, observations_std)
plt.show()