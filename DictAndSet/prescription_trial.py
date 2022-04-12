from prescription_data import *

trial_patiens = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patiens:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin.")
        print(f"Please remove {patient} from the trial.")
    print(patient, prescription)
