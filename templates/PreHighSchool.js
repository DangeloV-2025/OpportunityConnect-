document.addEventListener("DOMContentLoaded", function() {
  const programs = [
      {
          icon: "../static/Images/JKC_icon.png",
          title: "Jack Kent Cooke Young Scholars Program",
          description:
              "The Cooke Young Scholars Program is a selective five-year, pre-college scholarship for exceptionally promising 7th grade students with financial need. It provides comprehensive academic and college advising, as well as financial support for school, Cooke-sponsored summer programs, internships, and other learning enrichment opportunities.",
          link: "https://www.jkcf.org/our-scholarships/young-scholars-program/",
      },
      {
          icon: "../static/Images/ABC_icon.png",
          title: "A Better Chance",
          description:
              "A Better Chance places high-performing students of color in our nation’s best independent and public schools and supports them on their educational and leadership journeys.",
          link: "https://abetterchance.org/program/how-our-program-works/",
      },
  ];

  const programList = document.getElementById("scholarship-list");

  programs.forEach((program) => {
      const programDiv = document.createElement("div");
      programDiv.classList.add("scholarship");

      // Create the icon container
      const iconContainer = document.createElement("div");
      iconContainer.classList.add("icon");

      const image = document.createElement("img");
      image.src = program.icon;
      image.alt = `${program.title} Logo`;

      iconContainer.appendChild(image);

      // Create the details container
      const detailsDiv = document.createElement("div");
      detailsDiv.classList.add("details");

      const title = document.createElement("h2");
      title.textContent = program.title;

      const description = document.createElement("p");
      description.textContent = program.description;

      const link = document.createElement("a");
      link.href = program.link;
      link.textContent = "Learn More";

      detailsDiv.appendChild(title);
      detailsDiv.appendChild(description);
      detailsDiv.appendChild(link);

      // Append the icon and details to the program div
      programDiv.appendChild(iconContainer);
      programDiv.appendChild(detailsDiv);

      // Add the program div to the list
      programList.appendChild(programDiv);
  });
});
