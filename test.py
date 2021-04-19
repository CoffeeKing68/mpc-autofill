from autofill import AutoFiller

if __name__ == "__main__":
    # filename = "decklists/1_G Tron_tokens_(3).xml"
    # filename = "decklists/total_test.xml"
    filename = "decklists/___all.xml"

    autofiller = AutoFiller(filename)
    autofiller.autofill()