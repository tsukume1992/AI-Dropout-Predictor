# ==========================================================
# Student Module Version 4.1
# ==========================================================
import os
import uuid
from PIL import Image
from werkzeug.utils import secure_filename
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from app.services.student_service import (
    get_all_students,
    get_courses,
    get_sections,
    save_student,
    get_student_by_id,
    update_student,
    delete_student_record,
    student_number_exists,
    email_exists
)

student = Blueprint(
    "student",
    __name__,
    url_prefix="/students"
)

# ==========================================================
# File Upload Configuration
# ==========================================================

UPLOAD_FOLDER = os.path.join(
    "app",
    "static",
    "uploads",
    "students"
)

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg"
}

# ==========================================================
# Check Allowed File
# ==========================================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )

# ==========================================================
# Student List
# ==========================================================

@student.route("/")
def index():

    search = request.args.get("search", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = 10

    students, total = get_all_students(
        search,
        page,
        per_page
    )

    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "students/index.html",
        students=students,
        search=search,
        page=page,
        total_pages=total_pages
    )


# ==========================================================
# Add Student
# ==========================================================

@student.route("/add", methods=["GET", "POST"])
def add_student():

    courses = get_courses()
    sections = get_sections()

    if request.method == "POST":
        data = {
        "student_number": request.form.get("student_number", "").strip(),
        "first_name": request.form.get("first_name", "").strip(),
        "middle_name": request.form.get("middle_name", "").strip(),
        "last_name": request.form.get("last_name", "").strip(),
        "sex": request.form.get("sex", "").strip(),
        "birthdate": request.form.get("birthdate"),
        "email": request.form.get("email", "").strip(),
        "contact_number": request.form.get("contact_number", "").strip(),
        "address": request.form.get("address", "").strip(),
        "course_id": request.form.get("course_id"),
        "section_id": request.form.get("section_id"),
        "year_level": request.form.get("year_level"),
        "status": request.form.get("status"),

        # Default photo
        "photo": "default.png"
    }


        # ==========================================
        # Required Field Validation
        # ==========================================

        required_fields = [
            "student_number",
            "first_name",
            "last_name",
            "course_id",
            "section_id",
            "year_level",
            "status"
        ]

        for field in required_fields:

            if not data[field]:

                flash(
                    "Please complete all required fields.",
                    "danger"
                )

                return render_template(
                    "students/add.html",
                    courses=courses,
                    sections=sections,
                    student=data
                )

        # ==========================================
        # Duplicate Student Number
        # ==========================================

        if student_number_exists(data["student_number"]):

            flash(
                "Student Number already exists.",
                "danger"
            )

            return render_template(
                "students/add.html",
                courses=courses,
                sections=sections,
                student=data
            )

        # ==========================================
        # Duplicate Email
        # ==========================================

        if data["email"] and email_exists(data["email"]):

            flash(
                "Email address already exists.",
                "danger"
            )

            return render_template(
                "students/add.html",
                courses=courses,
                sections=sections,
                student=data
            )

        # ==========================================
        # Upload Student Photo
        # ==========================================

        photo = request.files.get("photo")

        if photo and photo.filename != "":

            if not allowed_file(photo.filename):

                flash(
                    "Only JPG, JPEG and PNG images are allowed.",
                    "danger"
                )

                return render_template(
                    "students/add.html",
                    courses=courses,
                    sections=sections,
                    student=data
                )

            extension = photo.filename.rsplit(".", 1)[1].lower()

            filename = (
                str(uuid.uuid4())
                + "."
                + extension
            )

            filepath = os.path.join(
                UPLOAD_FOLDER,
                filename
            )

            image = Image.open(photo)

            image = image.convert("RGB")

            image.thumbnail(
                (300, 300)
            )

            image.save(filepath)

            data["photo"] = filename

    # ==========================================
    # Save Student
    # ==========================================

    save_student(data)

    flash(
        "Student added successfully!",
        "success"
    )

    return redirect(
        url_for("student.index")
    )

    # GET Request
    return render_template(
        "students/add.html",
        courses=courses,
        sections=sections
    )

# ==========================================================
# View Student
# ==========================================================

@student.route("/view/<int:student_id>")
def view_student(student_id):

    student_data = get_student_by_id(student_id)

    if not student_data:

        flash(
            "Student not found.",
            "warning"
        )

        return redirect(
            url_for("student.index")
        )

    return render_template(
        "students/view.html",
        student=student_data
    )

# ==========================================================
# Edit Student
# ==========================================================

@student.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    student_data = get_student_by_id(student_id)

    if not student_data:

        flash(
            "Student not found.",
            "warning"
        )

        return redirect(
            url_for("student.index")
        )

    courses = get_courses()
    sections = get_sections()

    if request.method == "POST":
        data = {

        "student_number": request.form.get("student_number", "").strip(),
        "first_name": request.form.get("first_name", "").strip(),
        "middle_name": request.form.get("middle_name", "").strip(),
        "last_name": request.form.get("last_name", "").strip(),
        "sex": request.form.get("sex", "").strip(),
        "birthdate": request.form.get("birthdate"),
        "email": request.form.get("email", "").strip(),
        "contact_number": request.form.get("contact_number", "").strip(),
        "address": request.form.get("address", "").strip(),
        "course_id": request.form.get("course_id"),
        "section_id": request.form.get("section_id"),
        "year_level": request.form.get("year_level"),
        "status": request.form.get("status"),

        # Default photo
        "photo": "default.png"
    }
        # ==========================================
        # Required Field Validation
        # ==========================================

        required_fields = [
            "student_number",
            "first_name",
            "last_name",
            "course_id",
            "section_id",
            "year_level",
            "status"
        ]

        for field in required_fields:

            if not data[field]:

                flash(
                    "Please complete all required fields.",
                    "danger"
                )

                return render_template(
                    "students/edit.html",
                    student=data,
                    courses=courses,
                    sections=sections
                )

        # ==========================================
        # Duplicate Student Number
        # ==========================================

        if student_number_exists(
            data["student_number"],
            student_id
        ):

            flash(
                "Student Number already exists.",
                "danger"
            )

            return render_template(
                "students/edit.html",
                student=data,
                courses=courses,
                sections=sections
            )

        # ==========================================
        # Duplicate Email
        # ==========================================

        if data["email"] and email_exists(
            data["email"],
            student_id
        ):

            flash(
                "Email address already exists.",
                "danger"
            )

            return render_template(
                "students/edit.html",
                student=data,
                courses=courses,
                sections=sections
            )

        # ==========================================
        # Update Student
        # ==========================================

        update_student(
            student_id,
            data
        )

        flash(
            "Student updated successfully!",
            "success"
        )

        return redirect(
            url_for("student.index")
        )

    return render_template(
        "students/edit.html",
        student=student_data,
        courses=courses,
        sections=sections
    )

# ==========================================================
# Delete Student
# ==========================================================

@student.route("/delete/<int:student_id>")
def delete_student(student_id):

    try:

        delete_student_record(student_id)

        flash(
            "Student deleted successfully!",
            "success"
        )

    except Exception as e:

        flash(
            f"Unable to delete student. {str(e)}",
            "danger"
        )

    return redirect(
        url_for("student.index")
    )