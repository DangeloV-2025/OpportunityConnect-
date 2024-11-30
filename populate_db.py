from app import app
from models import db, Scholarship

# Run within the app context
with app.app_context():
    scholarships = [
        Scholarship(
            name='Cameron Impact Scholarship',
            amount='Up to $50,000',
            deadline='2024-09-15',
            description='Awarded to high school seniors demonstrating academic excellence and community service.',
            apply_link='https://www.bryancameroneducationfoundation.org/cameron-impact-scholarship'
        ),
        Scholarship(
            name='The Gates Scholarship',
            amount='Full Tuition',
            deadline='2024-09-18',
            description='For minority high school seniors with financial need, showcasing leadership and academic success.',
            apply_link='https://www.thegatesscholarship.org/scholarship'
        ),
        Scholarship(
            name='QuestBridge National College Match',
            amount='Full Tuition',
            deadline='2024-09-27',
            description='Connects high-achieving, low-income students with full scholarships to top colleges.',
            apply_link='https://www.questbridge.org/high-school-students/national-college-match'
            ),
        Scholarship(
            name='Horatio Alger Scholarship Award',
            amount='Varies',
            deadline='2024-10-25',
            description='Assists high school seniors who have faced and overcome great obstacles.',
            apply_link='https://scholars.horatioalger.org/scholarships/'
            ),
        Scholarship(
            name='Coca-Cola Scholars Program',
            amount='$20,000',
            deadline='2024-10-31',
            description='Recognizes high school seniors for their capacity to lead and serve.',
            apply_link='https://www.coca-colascholarsfoundation.org/apply/'
        ),
        Scholarship(
            name='Elks National Foundation Most Valuable Student Competition',
            amount='Up to $50,000',
            deadline='2024-11-15',
            description='Awards scholarships to high school seniors based on academics and leadership.',
            apply_link='https://www.elks.org/scholars/scholarships/mvs.cfm'
        ),
        Scholarship(
            name='Jack Kent Cooke Foundation College Scholarship Program',
            amount='Up to $40,000 per year',
            deadline='2024-11-20',
            description='For high-achieving high school seniors with financial need.',
            apply_link='https://www.jkcf.org/our-scholarships/college-scholarship-program/'
        ),
        Scholarship(
            name='Dell Scholars Program',
            amount='$20,000',
            deadline='2024-12-01',
            description='Targets low-income, highly motivated students.',
            apply_link='https://www.dellscholars.org/scholarship/'
        ),
        Scholarship(
            name='Burger King Scholars Program',
            amount='Up to $50,000',
            deadline='2024-12-15',
            description='For high school seniors with a strong academic record and community involvement.',
            apply_link='https://bk-scholars.com/'
        ),
        Scholarship(
            name='AXA Achievement Scholarship',
            amount='Up to $25,000',
            deadline='2024-12-15',
            description='Provides scholarships to high school seniors who demonstrate ambition and self-drive.',
            apply_link='https://us.axa.com/axa-foundation/AXA-achievement-scholarship.html'
        )

    ]

    # Add to the session
    db.session.bulk_save_objects(scholarships)
    # Commit changes
    db.session.commit()

    print("Scholarships added to the database!")
