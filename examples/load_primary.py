from datasets import load_dataset

ds = load_dataset(
    "ProtectSkills/MaliciousSkillBench",
    "primary",
    split="train",
)

def get_public_text(row):
    return row["skill_text"] or row["public_skill_text"]


print(len(ds))
print(get_public_text(ds[0]) is not None)
