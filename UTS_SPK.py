import pandas as pd

# Data nasabah
nasabah_data = {
    "A": {
        "ADB": 20000,
        "Credit_History": 0.9,  # Nilai kredit baik
        "Savings_Amount": 5000,
        "Age": 35,
        "Monthly_Income": 5000
    },
    "B": {
        "ADB": 10000,
        "Credit_History": 0.7,  # Nilai kredit cukup baik
        "Savings_Amount": 10000,
        "Age": 40,
        "Monthly_Income": 6000
    },
    "C": {
        "ADB": 30000,
        "Credit_History": 0.3,  # Nilai kredit buruk
        "Savings_Amount": 3000,
        "Age": 28,
        "Monthly_Income": 4000
    }
}

# Bobot atribut
weights = {
    "ADB": 0.3,
    "Credit_History": 0.2,
    "Savings_Amount": 0.15,
    "Age": 0.2,
    "Monthly_Income": 0.15
}

# Normalisasi atribut
for attribute in nasabah_data["A"]:
    values = [nasabah_data[nasabah][attribute] for nasabah in nasabah_data]
    min_value = min(values)
    max_value = max(values)
    for nasabah in nasabah_data:
        nasabah_data[nasabah][attribute] = (nasabah_data[nasabah][attribute] - min_value) / (max_value - min_value)

# Perhitungan derajat keanggotaan terpilih
membership_degrees = {}
for nasabah in nasabah_data:
    degree = sum(nasabah_data[nasabah][attribute] * weights[attribute] for attribute in nasabah_data[nasabah])
    membership_degrees[nasabah] = degree

# Tentukan ambang batas (threshold)
threshold = 0.6  # Misalnya, ambang batas 0.6

# Menentukan nasabah prioritas atau bukan
prioritas_nasabah = {}
for nasabah, degree in membership_degrees.items():
    if degree > threshold:
        prioritas_nasabah[nasabah] = "Yes"
    else:
        prioritas_nasabah[nasabah] = "No"

# Membuat DataFrame pandas
result_df = pd.DataFrame({
    "Nama Nasabah": list(prioritas_nasabah.keys()),
    "Derajat Keanggotaan": list(membership_degrees.values()),
    "Prioritas": list(prioritas_nasabah.values())
})

# Cetak hasil dalam bentuk tabel
print(result_df)
