import sys

file_path = sys.argv[1]

script_to_append = """
<script id="pub-headers-after-body" type="application/javascript">
document.addEventListener("DOMContentLoaded", () => {
  const refs =
    document.querySelector("#refs .csl-bib-body") ||
    document.getElementById("refs");

  if (!refs) return;

  const entries = Array.from(refs.querySelectorAll(".csl-entry"));
  let lastSection = null;

  entries.forEach((entry) => {
    const text = entry.textContent;
    let section;

    if (/\\(in press\\)/i.test(text)) {
      section = "In press / recent";
    } else if (/\\(preprint\\)/i.test(text)) {
      section = "Preprint";
    } else {
      const match = text.match(/\\((\\d{4})\\)/);
      section = match ? match[1] : "Other";
    }

    if (section !== lastSection) {
      const header = document.createElement("div");
      header.className = "pub-section";
      header.innerHTML = `<b>${section}</b>`;
      refs.insertBefore(header, entry);
      lastSection = section;
    }
  });
});
</script>
"""

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

if "</body>" in html:
    html = html.replace("</body>", script_to_append + "\n</body>")
else:
    html += script_to_append

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Script appended to the end of {file_path}")
