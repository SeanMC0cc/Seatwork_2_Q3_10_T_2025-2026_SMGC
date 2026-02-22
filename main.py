from pyscript import display, document

def intramsteam(e):  
    document.getElementById('registrationoutput').innerHTML = '' # resets value

    # raw variables, to be used in the if statements

    eligibility = 0
    getgradelevel = document.querySelector('#gradeselect').value
    gradelevel = getgradelevel
    getsection = document.querySelector('#sectionselect').value
    section = getsection
    assignedteam = '#'

    # collects the given team via section

    if section == 'Emerald':
        assignedteam = 'Yellow Tigers'

    elif section == 'Ruby':
        assignedteam = 'Green Hornets'
    
    elif section == 'Sapphire':
        assignedteam = 'Blue Bears'

    elif section == 'Topaz':
        assignedteam = 'Red Bulldogs'

    # checked area for eligibility, represented by an integer (0 is uneligible, 1 is uneligible with no medical clearance, 2 is uneligible with no registration, 3 is eligible)
    
    if document.getElementById('registrationcheck').checked:
        eligibility = eligibility + 1
    if document.getElementById('medicalcheck').checked:
        eligibility = eligibility + 2

    if eligibility == 3:
        display(f"You are eligible for the intramurals!", target="registrationoutput")
        display(f"Your class, {gradelevel}-{section}, is a part of {assignedteam}!", target="registrationoutput")

    elif eligibility == 1: 
         display(f"You are not eligible for the intramurals. If you wish to play, please secure medical clearance.", target="registrationoutput")

    elif eligibility == 2: 
         display(f"You are not eligible for the intramurals. To register, go to our OBMC Portal.", target="registrationoutput")

    else: 
         display(f"You are not eligible for the intramurals.", target="registrationoutput")

def account_verify(e):
    document.getElementById('accountoutput').innerHTML = '' # resets value
    
    username = document.getElementById('nameinput').value

    password = document.getElementById('passwordinput').value

    # one nested if statement

    if len(password) >= 10 and len(username) >= 7: # primary check, if the username's length is 7 or more and if the password's length is 10 or more
        if not password.isalpha(): # secondary check for the password, checks if it contains solely letters
            if password.isdigit(): # final check for the password, checks if it contains solely numbers
                display(f"Your username is eligible. Your password must contain both letters and numbers. Please add letters.", target="accountoutput")
    
            else: # if the second and third check are false, sign in
                display(f"You are signed up, {username}! Welcome!", target="accountoutput")

        elif password.isalpha():
            display(f"Your username is eligible. Your password must contain both letters and numbers. Please add numbers.", target="accountoutput")

    elif not len(password) >= 10 and len(username) >= 7:
            display(f"Your username is eligible. Your password must be 10 characters or more.", target="accountoutput")
    
    elif not len(password) >= 10 and not len(username) >= 7:
            display(f"Your username must be 7 characters or more. Your password must be 10 characters or more.", target="accountoutput")
    
    elif len(password) >= 10 and not len(username) >= 7:
            display(f"Your username must be 7 characters or more.", target="accountoutput")


def show_players(event):
    document.getElementById("listoutput").innerHTML = ""

    getsectionB = document.querySelector('#sectionselect2').value
    sectionB = getsectionB
    players = []

    if sectionB == 'Emerald':
        players = [
            "Abayon",
            "Antes",
            "Apostol",
            "Banaag",
            "Barrientos",
            "Casal",
            "Coeli",
            "David",
            "De Mata",
            "Dela Cruz",
            "Dela Cruz",
            "Dellejero",
            "Fukuda",
            "Gozum",
            "Ibay",
            "Lim",
            "Lozano",
            "Mamauag",
            "Navarro",
            "Ramos",
            "Sidhu",
            "Tiu",
            "Villamayor",
            "Zaragoza"
        ]
        

    elif sectionB == 'Ruby':
        players = [
            "Agena",
            "Ala",
            "Baring",
            "Baylon",
            "Brodhagen",
            "Cabatingan",
            "Canete",
            "Dimaculangan",
            "Evangelista",
            "Galang",
            "Garabiles",
            "Gonzales",
            "Jamet",
            "Ledesma",
            "Nacino",
            "Nardo",
            "Olmedo",
            "Oliveros",
            "Ong",
            "Rebadulla",
            "Reyes",
            "Sangreo",
            "Villegas",
            "Villafuerte",
            "Yao"
        ]
         
    
    
    elif sectionB == 'Sapphire':
        players = [
            "Aseo",
            "Batac",
            "Calanglang",
            "De Guzman",
            "Dee",
            "Dolor",
            "Galvez",
            "Garces",
            "Grospe",
            "Hizon",
            "Intalan",
            "Ko",
            "Lagman",
            "Law",
            "Macabago",
            "Martinez",
            "Medina",
            "Mendoza",
            "Mergal",
            "Ngo",
            "Padojinog",
            "Rivera",
            "Shrestha",
            "Uy",
            "Yao"
        ]
          

    elif sectionB == 'Topaz':
        players = [
             "Abdullah", 
             "Abeleda", 
             "Arce", 
             "Arias", 
             "Bonzon", 
             "Cajucom", 
             "Catimbang", 
             "Choi", 
             "Cotioco", 
             "Daradal", 
             "Enriquez", 
             "Escobar", 
             "Espina", 
             "Gano", 
             "Garcia", 
             "Kaur", 
             "Ong", 
             "Rufo", 
             "Sanchez", 
             "Santos", 
             "Tan", 
             "Vilale", 
             "Yao", 
             "Zosa",
        ]

    for player in players:
        display(f"- {player}", target="listoutput")

    




