def name_in_str(str, name):
    it = iter(str.lower())
    print(all(c in it for c in name.lower()))


name_in_str("Across the rivers", "chiis")
