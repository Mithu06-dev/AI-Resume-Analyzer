import re


COMMON_SKILLS = [
    "python",
    "java",
    "javascript",
    "html",
    "css",
    "react",
    "django",
    "node.js",
    "sql",
    "mysql",
    "mongodb",
    "git",
    "github",
    "aws",
    "docker",
    "machine learning",
    "data science",
    "artificial intelligence",
]


def analyze_resume(text):

    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    score = 40

    if len(text) > 1000:
        score += 15

    if "education" in text_lower:
        score += 10

    if "experience" in text_lower:
        score += 10

    if "skills" in text_lower:
        score += 10

    if "projects" in text_lower:
        score += 10

    if "contact" in text_lower:
        score += 5

    score = min(score, 100)

    suggestions = []

    if "summary" not in text_lower and "objective" not in text_lower:
        suggestions.append(
            "Add a professional summary or career objective."
        )

    if "projects" not in text_lower:
        suggestions.append(
            "Add a Projects section with measurable achievements."
        )

    if "experience" not in text_lower:
        suggestions.append(
            "Add internship, work experience, or relevant practical experience."
        )

    if len(found_skills) < 5:
        suggestions.append(
            "Add more relevant technical skills based on the target job."
        )

    if len(text) < 1000:
        suggestions.append(
            "Your resume contains limited content. Add relevant projects, "
            "skills, certifications, or achievements."
        )

    return {
        "ats_score": score,
        "grammar_score": 75,
        "keyword_score": min(len(found_skills) * 10, 100),
        "overall_score": score,
        "skills": found_skills,
        "suggestions": suggestions,
    }