"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150


# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary by its key
schools.pop("Duke")

# Test for the existence of a key (is the key in the dictionary)
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}.")

if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' in schools.")

# Update/reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict(); shorthand

# Alternatively, initialize key-value pairs
schools = {"UNC": 19_400, "Duke": 6_717, "NCSU": 26_150}

schools = {
    "UNC": 19_400,
    "Duke": 6_717,
    "NCSU": 26_150,
}

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
