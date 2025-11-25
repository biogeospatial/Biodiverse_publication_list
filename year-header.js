document.addEventListener("DOMContentLoaded", function () {
  const refs = document.querySelectorAll(".references div, .references li");
  let seenYears = new Set();

  refs.forEach((ref) => {
    const match = ref.textContent.match(/\((\d{4}|in press)\)/i);
    const year = match ? match[1] : "Unknown";

    if (!seenYears.has(year)) {
      const header = document.createElement("h2");
      header.textContent =
        year.toLowerCase() === "in press" ? "In Press" : year;
      ref.parentNode.insertBefore(header, ref);
      seenYears.add(year);
    }
  });
});
