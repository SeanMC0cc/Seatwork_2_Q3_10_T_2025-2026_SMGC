from pyscript import display, document

def check_intramurals(event):
    olr = document.querySelector("input[name='OLR']:checked")
    mc = document.querySelector("input[name='MC']:checked")
    grade = document.getElementById("Grade").value
    section = document.getElementById("Section").value

    output = document.getElementById("output")
    output.innerHTML = ""

    olr = olr.value if olr else ""
    mc = mc.value if mc else ""

    # Stackoverflow

    valid_sections = ["Topaz", "Emerald", "Ruby", "Sapphire"]

    eligible = (
        olr == "Yes"
        and mc == "Yes"
        and grade in ["7", "8", "9", "10"]
        and section in valid_sections
    )

    if eligible:
        teams = ["Green Hornets", "Red Bulldogs", "Yellow Tigers", "Blue Bears"]
        team = teams[valid_sections.index(section)]

        display(f'Congratulations! You are eligible to join the Intramurals. Assigned Team: {team}', target="output")

    else:
        if olr != "Yes":
            display(f'You are not eligible to join the Intramurals due to not registering online.', target="output")
        if mc != "Yes":
            display("Please secure a medical clearance.", target="output")
        if grade not in ["7", "8", "9", "10"]:
            display("You must be in grades 7–10 to join.", target="output")
        if section not in valid_sections:
            display("Please select a valid section.", target="output")
