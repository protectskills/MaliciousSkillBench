(function () {
  var links = window.MSB_PUBLIC_LINKS || {};
  var fallback = {
    PAPER_URL: "https://arxiv.org/abs/2608.19901",
    PAPER_PDF_URL: "https://arxiv.org/pdf/2608.19901",
    DATASET_URL: "https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench",
    GITHUB_URL: "https://github.com/protectskills/MaliciousSkillBench",
    DOCS_URL: "https://github.com/protectskills/MaliciousSkillBench/tree/main/benchmark"
  };

  document.querySelectorAll("a[data-msb-link]").forEach(function (node) {
    var key = node.getAttribute("data-msb-link");
    var url = (links[key] || fallback[key] || "").trim();
    if (url) {
      node.setAttribute("href", url);
    }
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
