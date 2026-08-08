from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Resume
from .parser import extract_resume_text
from .analyzer import analyze_resume


def home(request):
    return render(request, "home.html")


#@login_required
def upload_resume(request):

    if request.method == "POST":

        resume_file = request.FILES.get("resume")

        if not resume_file:
            return render(
                request,
                "upload.html",
                {"error": "Please select a resume."}
            )

        allowed_extensions = [".pdf", ".docx"]

        file_name = resume_file.name.lower()

        if not any(file_name.endswith(ext) for ext in allowed_extensions):
            return render(
                request,
                "upload.html",
                {"error": "Only PDF and DOCX files are supported."}
            )

        resume = Resume.objects.create(
           # user=request.user,
            user=None,
            file=resume_file
        )

        text = extract_resume_text(resume.file.path)

        result = analyze_resume(text)

        resume.extracted_text = text
        resume.ats_score = result["ats_score"]
        resume.grammar_score = result["grammar_score"]
        resume.keyword_score = result["keyword_score"]
        resume.overall_score = result["overall_score"]
        resume.suggestions = "\n".join(result["suggestions"])

        resume.save()

        return redirect("result", resume_id=resume.id)

    return render(request, "upload.html")


#@login_required
def result(request, resume_id):

    resume = Resume.objects.get(
        id=resume_id,
        #user=request.user
    )

    skills = []

    if resume.extracted_text:
        analysis = analyze_resume(resume.extracted_text)
        skills = analysis["skills"]

    return render(
        request,
        "result.html",
        {
            "resume": resume,
            "skills": skills,
        }
    )


#@login_required
def dashboard(request):

    resumes = Resume.objects.filter(
        user=None
    ).order_by("-uploaded_at")

    return render(
        request,
        "dashboard.html",
        {
            "resumes": resumes
        }
    )

# Create your views here.
