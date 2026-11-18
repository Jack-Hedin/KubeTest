import os 
import numpy as np
import matplotlib.pyplot as plt


def main():
    Start = 0
    End = 100
    NumSteps = 200
    delta_t = (End - Start)/NumSteps

    TimeCords = np.linspace(Start, End, NumSteps)

    initialSusceptible:float = .98
    initialInfected:float = .02


    beta = .3 * np.random.uniform(.5,2)
    nu = .3 * np.random.uniform(.5,2)
    omega = (2*np.pi / 25)
    def step(t, Susceptible, Infected):
        seasonalBeta = beta * (1 + np.cos(omega * t ))
        dS = (-seasonalBeta * Susceptible * Infected) * delta_t
        dI = (seasonalBeta * Susceptible * Infected - nu * Infected) * delta_t
        return dS, dI 


    SusceptibleArr = np.zeros_like(TimeCords)
    InfectedArr = np.zeros_like(TimeCords)
    SusceptibleArr[0] = initialSusceptible
    InfectedArr[0] = initialInfected

    for i in range(NumSteps-1):
        dS, dI = step(TimeCords[i], SusceptibleArr[i], InfectedArr[i])
        SusceptibleArr[i+1] = SusceptibleArr[i] + dS
        InfectedArr[i+1] = InfectedArr[i] + dI

    return TimeCords, SusceptibleArr, InfectedArr

def graph(TimeCords, Susceptible, Infected, filename="susceptible_vs_infected.png"):
    plt.figure(figsize=(8, 6))
    plt.scatter(Susceptible, Infected, c=TimeCords, cmap='viridis', s=40, edgecolors='k', zorder=3, label='Points')
    plt.plot(Susceptible, Infected, linestyle='--', color='gray', alpha=0.6, label='Trajectory')
    cbar = plt.colorbar()
    cbar.set_label('Time')
    plt.xlabel('Susceptible')
    plt.ylabel('Infected')
    plt.title('Susceptible vs. Infected')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    save_path = os.path.join(os.getcwd(), filename)
    plt.savefig(save_path, dpi=300)
    print(f"Plot saved to: {save_path}")
    #plt.show()


if __name__ == '__main__':
    time_cords, s_arr, i_arr = main()
    graph(time_cords, s_arr, i_arr)