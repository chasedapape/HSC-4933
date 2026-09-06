heart_rate_samples = {
    "J. Alvarez": [72, 75, 78],
    "M. Chen": [80, 82],
    "R. Okafor": [65, 68, 70, 66],
    "S. Patel": [90, 95, 92, 88, 91],
    "T. Nguyen": [77, 79],
    "L. Kowalski": [68, 70, 69],
    "D. Osei": [98, 101, 95, 99],
    "A. Whitfield": [74, 76, 75, 73],
}

patient_numbers = {i + 1: name for i, name in enumerate(heart_rate_samples)}
 
 
def avg(*args):
    return sum(args) / len(args)
 
 
def get_all_stats(*args):
    return {"avg": avg(*args), "min": min(args), "max": max(args), "latest": args[-1]}
 
 
def get_specific_stat(stat_name, *args):
    return get_all_stats(*args).get(stat_name)
 
 
def prompt_for_patient():
    for num, name in patient_numbers.items():
        print(f"  {num}. {name}")
    choice = int(input("Enter patient number: "))
    return patient_numbers[choice]
 
 
def main():
    while True:
        choice = input("\n1) All stats  2) Specific stat  3) All patients  4) Quit\nChoice: ")
 
        if choice == "1":
            name = prompt_for_patient()
            print(f"\n{name}: {get_all_stats(*heart_rate_samples[name])}")
 
        elif choice == "2":
            name = prompt_for_patient()
            stat = input("Which stat? (avg, min, max, latest): ").strip().lower()
            result = get_specific_stat(stat, *heart_rate_samples[name])
            print(f"\n{stat} for {name}: {result}" if result is not None else "Invalid stat name.")
 
        elif choice == "3":
            for name in heart_rate_samples:
                print(f"{name}: {get_all_stats(*heart_rate_samples[name])}")
 
        elif choice == "4":
            break
 
        else:
            print("Invalid choice.")
 
 
if __name__ == "__main__":
    main()
