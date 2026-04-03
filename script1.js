// JOB DATA
const jobs = [
    { title: "Frontend Developer", location: "Hyderabad", type: "Full-Time" },
    { title: "Backend Developer", location: "Bangalore", type: "Full-Time" },
    { title: "UI/UX Designer", location: "Chennai", type: "Internship" },
    { title: "Data Analyst", location: "Hyderabad", type: "Internship" },
    { title: "Full Stack Developer", location: "Bangalore", type: "Full-Time" },
    { title: "Python Developer", location: "Bangalore", type: "Full-Time" },
    { title: "Data Scientist", location: "Pune", type: "Internship" },
    { title: "Java Developer", location: "Hyderabad", type: "Full-Time" },
    { title: "AI Developer", location: "Bangalore", type: "Internship" },
    { title: "ML Developer", location: "Hyderabad", type: "Internship" },
    { title: "Cyber security", location: "Pune", type: "Full-Time" },
    { title: ".Net Developer", location: "Bangalore", type: "Full-Time" },
    { title: "Networking", location: "Pune", type: "Internship" },
    { title: "UI Developer", location: "Bangalore", type: "Full-Time" },
    { title: "Software Developer", location: "Hyderabad", type: "Full-Time" }
];

// ELEMENTS
const jobList = document.getElementById("jobList");
const search = document.getElementById("search");
const locationFilter = document.getElementById("locationFilter");
const typeFilter = document.getElementById("typeFilter");

// DISPLAY JOBS
function displayJobs(filteredJobs) {
    jobList.innerHTML = "";

    filteredJobs.forEach(job => {
        const div = document.createElement("div");
        div.classList.add("job-card");

        div.innerHTML = `
            <h3>${job.title}</h3>
            <p><strong>Location:</strong> ${job.location}</p>
            <p><strong>Type:</strong> ${job.type}</p>
        `;

        jobList.appendChild(div);
    });

    updateDashboard(filteredJobs);
}

// FILTER FUNCTION
function filterJobs() {
    let filtered = jobs.filter(job => {
        return (
            job.title.toLowerCase().includes(search.value.toLowerCase()) &&
            (locationFilter.value === "" || job.location === locationFilter.value) &&
            (typeFilter.value === "" || job.type === typeFilter.value)
        );
    });

    displayJobs(filtered);
}

// DASHBOARD
function updateDashboard(list) {
    document.getElementById("totalJobs").innerText = list.length;

    let fullTime = list.filter(j => j.type === "Full-Time").length;
    let intern = list.filter(j => j.type === "Internship").length;

    document.getElementById("fullTimeCount").innerText = fullTime;
    document.getElementById("internCount").innerText = intern;
}

// EVENT LISTENERS
search.addEventListener("input", filterJobs);
locationFilter.addEventListener("change", filterJobs);
typeFilter.addEventListener("change", filterJobs);

// INITIAL LOAD
displayJobs(jobs);
