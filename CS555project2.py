supported_tags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR",
                  "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

with open('CS555project2.ged') as file:
    for line in file:
        line = line.strip()
        print("-->", line)
        parts = line.split(" ")
        level = parts[0]
        tag = parts[1] if len(parts) > 1 else ""
        valid = "Y" if tag in supported_tags else "N"
        arguments = " ".join(parts[2:]) if len(parts) > 2 else ""
        if arguments in supported_tags:
            print("<--", level, "|", arguments, "|", "Y", "|", tag, sep="")
        else:
            print("<--", level, "|", tag, "|", valid, "|", arguments, sep="")