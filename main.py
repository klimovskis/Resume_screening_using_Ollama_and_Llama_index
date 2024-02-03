from llama_index.llms import Ollama
from resume_screener_pack import base

llm = Ollama(model="llama2")


resume_screener = base.ResumeScreenerPack(
    job_description="Senior Python Developer",
    criteria=[
        "Need to have 5 years of Python",
        "Should have worked with Flask and Django"
    ],
    llm = llm
)

response = resume_screener.run(resume_path="/Users/nikita/Desktop/sterfy_local/Anastasija Arfanova-CV.pdf")

for cd in response.criteria_decisions:
    print("### CRITERIA DECISION")
    print(cd.reasoning)
    print(cd.decision)
print("#### OVERALL REASONING ##### ")
print(str(response.overall_reasoning))
print(str(response.overall_decision))