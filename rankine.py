from rankine import rankine

def main():
    # First scenario: Saturated vapor entering turbine
    print("Scenario 1:")
    cycle1 = rankine(p_high=8000, p_low=8, name="Saturated Vapor Entering Turbine")
    eff1 = cycle1.calc_efficiency()
    cycle1.print_summary()
    print(f"Efficiency: {eff1}%\n")

    # Second scenario: Superheated steam entering turbine
    print("Scenario 2:")
    cycle2 = rankine(p_high=8000, p_low=8, t_high=1.7 * cycle1.state1.T, name="Superheated Steam Entering Turbine")
    eff2 = cycle2.calc_efficiency()
    cycle2.print_summary()
    print(f"Efficiency: {eff2}%\n")

if __name__ == "__main__":
    main()
