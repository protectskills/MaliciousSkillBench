(function () {
  var links = window.MSB_PUBLIC_LINKS || {};
  var fallback = {
    PAPER_URL: "#paper",
    DATASET_URL: "https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench",
    GITHUB_URL: "https://github.com/protectskills/MaliciousSkillBench",
    DOCS_URL: "https://github.com/protectskills/MaliciousSkillBench/tree/main/benchmark"
  };

  document.querySelectorAll("[data-msb-link]").forEach(function (node) {
    var key = node.getAttribute("data-msb-link");
    var url = (links[key] || "").trim();
    if (url) {
      node.setAttribute("href", url);
      node.classList.remove("is-placeholder");
      node.removeAttribute("aria-disabled");
      node.removeAttribute("title");
      return;
    }
    if (fallback[key]) {
      node.setAttribute("href", fallback[key]);
    } else {
      node.setAttribute("href", "#");
      node.setAttribute("aria-disabled", "true");
    }
    node.classList.add("is-placeholder");
    node.setAttribute("title", "Publication URL pending");
  });

  var copyBtn = document.getElementById("copy-citation");
  var citation = document.getElementById("citation-block");
  if (copyBtn && citation && navigator.clipboard) {
    copyBtn.addEventListener("click", function () {
      navigator.clipboard.writeText(citation.textContent.trim()).then(function () {
        copyBtn.textContent = "Copied";
        window.setTimeout(function () { copyBtn.textContent = "Copy"; }, 1600);
      });
    });
  }
})();
