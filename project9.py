
print("================================")
print("     STUDENT SUBJECT RECORD CLEANER")
print("================================")

subjects = []

number = int(input("How many subject records? "))

for i in range(number):
    subject = input("Enter subject name: ")

    subject = subject.strip().title()

    if subject != "":
        subjects.append(subject)

print("\n========== ORIGINAL RECORDS ==========")

print(subjects)

cleaned = list(set(subjects))
cleaned.sort()

print("\n========== CLEANED RECORDS ==========")

for subject in cleaned:
    print("-", subject)

print("\n========== RECORD ANALYSIS ==========")

print("Original records:", len(subjects))
print("Cleaned records:", len(cleaned))
print("Duplicate records removed:", len(subjects) - len(cleaned))

search = input("\nEnter a subject to search: ")
search = search.strip().title()

if search in cleaned:
    print(search, "was found in the records.")

else:
    print(search, "was not found.")

print("\nSubject record cleaning completed!")
