// scholarships.js
document.addEventListener("DOMContentLoaded", function() {
    const scholarships = [
      {
        icon: "../static/Images/Questbridge_icon.png",
        title: "Questbridge National College Match",
        description:
          "The QuestBridge National College Match is a competitive scholarship program that helps high-achieving, low-income students gain admission to top U.S. colleges with full-ride scholarships, covering tuition, room, board, and other expenses.",
        link: "https://www.questbridge.org/apply-to-college/programs/national-college-match",
      },
      {
        icon: "../static/Images/Gates_icon.png",
        title: "The Gates Scholarship",
        description:
          "The Gates Scholarship supports high school seniors from minority backgrounds who demonstrate financial need. The scholarship covers the full cost of attendance, including tuition, fees, room, and board, with no cap on funding.",
        link: "https://www.thegatesscholarship.org",
      },
      {
        icon: "../static/Images/JKC_icon.png",
        title: "Jack Kent Cooke Undergraduate College Scholarship",
        description:
          "The Cooke College Scholarship Program is an undergraduate scholarship program available to high-achieving high school seniors with financial need who seek to attend and graduate from the nation's best four-year colleges and universities.",
        link: "https://www.jkcf.org/our-scholarships/college-scholarship-program/",
      },
      {
        icon: "../static/Images/Coke_icon.png",
        title: "Coca-Cola Scholars Foundation",
        description:
          "The Coca-Cola Scholars Program offers scholarships to high school seniors who demonstrate leadership, service, and academic excellence. Each year, 150 Coca-Cola Scholars are selected to receive up to $20,000 in college scholarships. The program is open to U.S. citizens or permanent residents attending high school in the United States.",
        link: "https://www.coca-colascholarsfoundation.org/",
      },
      {
        icon: "../static/Images/Jackie_icon.png",
        title: "Jackie Robinson Foundation Scholarship",
        description:
          "The Jackie Robinson Foundation offers the Jackie Robinson Scholarship to high school seniors who demonstrate academic excellence, leadership, and a commitment to community service. Open to minority students who are U.S. citizens, the scholarship awards up to $30,000 over four years to cover tuition and educational expenses.",
        link: "https://jackierobinson.org/scholarship/",
      },
    ];

    const scholarshipList = document.getElementById("scholarship-list");

    scholarships.forEach((scholarship) => {
      const scholarshipDiv = document.createElement("div");
      scholarshipDiv.classList.add("scholarship");

      // Create the icon container
      const iconContainer = document.createElement("div");
      iconContainer.classList.add("icon");

      const image = document.createElement("img");
      image.src = scholarship.icon;
      image.alt = `${scholarship.title} Logo`;

      iconContainer.appendChild(image);

      // Create the details container
      const detailsDiv = document.createElement("div");
      detailsDiv.classList.add("details");

      const title = document.createElement("h2");
      title.textContent = scholarship.title;

      const description = document.createElement("p");
      description.textContent = scholarship.description;

      const link = document.createElement("a");
      link.href = scholarship.link;
      link.textContent = "Learn More";

      detailsDiv.appendChild(title);
      detailsDiv.appendChild(description);
      detailsDiv.appendChild(link);

      // Append the icon and details to the scholarship div
      scholarshipDiv.appendChild(iconContainer);
      scholarshipDiv.appendChild(detailsDiv);

      // Add the scholarship div to the list
      scholarshipList.appendChild(scholarshipDiv);
    });
  });
