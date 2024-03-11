from rankine import RankineCycle

def main():
    # Rankine cycle with saturated vapor entering turbine
    rankine_cycle_1 = RankineCycle(8000, 8)
    efficiency_1 = rankine_cycle_1.calculate_efficiency()

    # Rankine cycle with superheated steam entering turbine
    rankine_cycle_2 = RankineCycle(8000, 8, superheated=True)
    efficiency_2 = rankine_cycle_2.calculate_efficiency()

    # Output report
    print("Rankine Cycle 1 Efficiency:", efficiency_1)
    print("Rankine Cycle 2 Efficiency:", efficiency_2)

if __name__ == "__main__":
    main()
