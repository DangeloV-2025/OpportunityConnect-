from app import app
from models import db, FlyIn

# Run within the app context
def populate_flyins():
    flyins = [
    FlyIn(
        name="Bates College Prologue to Bates",
        deadline="Oct (Exact dates vary)",
        description="An all-expenses-paid fly-in program for underrepresented students, providing an opportunity to explore campus life and meet faculty and students.",
        apply_link="https://www.bates.edu/admission-aid/visit/prologue-to-bates/"
    ),
    FlyIn(
        name="Brandeis University SEED",
        deadline="Late Oct",
        description="A program for rising seniors from diverse backgrounds to explore Brandeis and meet faculty, staff, and current students.",
        apply_link="https://www.brandeis.edu/admission/undergraduate/visit/seed.html"
    ),
    FlyIn(
        name="Bryn Mawr College Lantern Scholars Program",
        deadline="Late Sept to Early Oct",
        description="A fly-in program for students from historically underrepresented backgrounds, covering all expenses, including travel and accommodations.",
        apply_link="https://www.brynmawr.edu/admissions/visit/lantern-scholars"
    ),
    FlyIn(
        name="Bucknell University Journey to Bucknell",
        deadline="Fall (specific dates to be announced)",
        description="An introduction to Bucknell University for high-achieving, underrepresented students, offering small group activities and interactions with faculty.",
        apply_link="https://www.bucknell.edu/admission-aid/visit/journey-bucknell"
    ),
    FlyIn(
        name="Carleton College Taste of Carleton (TOC)",
        deadline="Late Jul to Early Aug",
        description="An all-expenses-paid fly-in program for high school seniors from underrepresented backgrounds to explore Carleton College.",
        apply_link="https://www.carleton.edu/admission/visit/taste/"
    ),
    FlyIn(
        name="Case Western Reserve University Diversity Overnight",
        deadline="Oct 13-14, Nov 10-11",
        description="A program for students from diverse backgrounds to stay overnight, attend classes, and meet current students and faculty.",
        apply_link="https://case.edu/admission/undergraduate/diversity-overnight"
    ),
    FlyIn(
        name="Colorado College Experiencing Colorado College (ECC)",
        deadline="Oct 12-14",
        description="An immersive program for prospective students from diverse backgrounds to explore Colorado College and meet current students.",
        apply_link="https://www.coloradocollege.edu/admission-aid/visit/experiencing-colorado-college/"
    ),
    FlyIn(
        name="Dartmouth College Indigenous Fly-In Program (IFI)",
        deadline="Oct 13-16",
        description="A program for Indigenous high school students to experience Dartmouth College and explore college opportunities.",
        apply_link="https://admissions.dartmouth.edu/visit/indigenous-fly-program"
    ),
    FlyIn(
        name="Davidson College Access Davidson",
        deadline="Sept 15-17",
        description="An event designed for underrepresented students to explore Davidson College, with travel and accommodation provided.",
        apply_link="https://www.davidson.edu/admission-aid/visit/access-davidson"
    ),
    FlyIn(
        name="Hamilton College Home at Hamilton",
        deadline="Oct 6-7",
        description="A fly-in for prospective students to experience Hamilton College, meet faculty, and interact with current students.",
        apply_link="https://www.hamilton.edu/admission/visit/home-at-hamilton"
    ),
    FlyIn(
        name="Haverford College Have-A-Look (HAL)",
        deadline="Oct 27-29",
        description="A program that gives students from diverse backgrounds an opportunity to visit Haverford College and engage with the community.",
        apply_link="https://www.haverford.edu/admission-aid/visit/have-a-look"
    ),
    FlyIn(
        name="Massachusetts Institute of Technology Weekend Immersion in Science & Engineering (WISE)",
        deadline="Oct 6-8",
        description="A program for women and non-binary students interested in science and engineering, covering travel and accommodation costs.",
        apply_link="https://wise.mit.edu"
    ),
    FlyIn(
        name="Middlebury College Discover Middlebury",
        deadline="Oct 20-22",
        description="An immersive program for underrepresented students to explore Middlebury College and its academic offerings.",
        apply_link="https://www.middlebury.edu/admission/visit/discover-middlebury"
    ),
    FlyIn(
        name="Oberlin College Multicultural Visit Program (MVP)",
        deadline="Oct 10-12, Nov 7-9",
        description="A program to help underrepresented students experience Oberlin College and meet other prospective students and faculty.",
        apply_link="https://www.oberlin.edu/admissions/multicultural-visit-program"
    ),
    FlyIn(
        name="Pomona College Perspectives on Pomona (POP)",
        deadline="Oct 6-8",
        description="A fly-in program for high school seniors to experience Pomona College and learn about its culture and community.",
        apply_link="https://www.pomona.edu/admission/visit/perspectives-pomona"
    ),
    FlyIn(
        name="Swarthmore College Discover Swarthmore",
        deadline="Sept 26-28, Oct 24-26",
        description="A chance for prospective students to explore Swarthmore College through student-led tours and panel discussions.",
        apply_link="https://www.swarthmore.edu/admission-aid/visit/discover-swarthmore"
    ),
    FlyIn(
        name="Tufts University Voices of Tufts Diversity Experience",
        deadline="Oct 6-7",
        description="A fly-in for students from diverse backgrounds to explore Tufts University and its community.",
        apply_link="https://admissions.tufts.edu/visit/voices-of-tufts"
    ),
    FlyIn(
        name="Washington and Lee University Diversity and Inclusion Visit Experience (DIVE)",
        deadline="Sept 22-24, Sept 29-Oct 1",
        description="A program designed to give underrepresented students an in-depth look at Washington and Lee University.",
        apply_link="https://www.wlu.edu/admission/diversity-and-inclusion-visit-experience"
    ),
    FlyIn(
        name="Wesleyan University WesExplore",
        deadline="Oct 13-14, Nov 10-11",
        description="A program for prospective students to explore Wesleyan University and its academic offerings.",
        apply_link="https://www.wesleyan.edu/admission/visit/wesexplore"
    ),
    FlyIn(
        name="Williams College Windows on Williams (WOW)",
        deadline="Oct 6-8",
        description="A program that allows prospective students to explore Williams College, its culture, and its community.",
        apply_link="https://www.williams.edu/admission-aid/visit/windows-on-williams"
    ),
    FlyIn(
        name="Yale University Yale in MOHtion",
        deadline="Oct 4-6",
        description="A fly-in program for students to explore Yale University’s resources and opportunities.",
        apply_link="https://admissions.yale.edu/yale-motion"
    )
    ]


    # Add to the session
    db.session.bulk_save_objects(flyins)
    # Commit changes
    db.session.commit()

    print("FlyIns added to the database!")
