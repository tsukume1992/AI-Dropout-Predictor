from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for,
    flash
)

from werkzeug.security import check_password_hash

from app.services.dashboard_service import get_dashboard_counts
from app.services.auth_service import (
    get_user_by_username,
    update_last_login
)
from app.services.audit_service import log_action


# ==========================================================
# Authentication Blueprint
# ==========================================================

auth = Blueprint(
    "auth",
    __name__
)


# ==========================================================
# Login
# ==========================================================

@auth.route("/", methods=["GET", "POST"])
def login():

    # If already logged in, go directly to dashboard
    if session.get("user_id"):
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = get_user_by_username(username)

        # --------------------------------------------------
        # Validate Credentials
        # --------------------------------------------------

        if user and check_password_hash(
            user["password_hash"],
            password
        ):

            # Clear previous session
            session.clear()

            # Create new session
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]
            session["role_id"] = user["role_id"]

            # Keep session active
            session.permanent = True

            # Update last login
            update_last_login(user["user_id"])

            # Audit Log
            try:

                log_action(
                    user["user_id"],
                    "User Logged In"
                )

            except Exception as error:

                print("Audit Error:", error)

            # Success Message
            flash(
                f"Welcome back, {user['username']}!",
                "success"
            )

            return redirect(
                url_for("auth.dashboard")
            )

        # --------------------------------------------------
        # Invalid Credentials
        # --------------------------------------------------

        flash(
            "Invalid username or password.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


# ==========================================================
# Dashboard
# ==========================================================

@auth.route("/dashboard")
def dashboard():

    if not session.get("user_id"):

        flash(
            "Your session has expired. Please log in again.",
            "warning"
        )

        return redirect(
            url_for("auth.login")
        )

    counts = get_dashboard_counts()

    return render_template(
        "dashboard/index.html",
        counts=counts
    )


# ==========================================================
# Logout
# ==========================================================

@auth.route("/logout")
def logout():

    if session.get("user_id"):

        try:

            log_action(
                session["user_id"],
                "User Logged Out"
            )

        except Exception as error:

            print("Audit Error:", error)

    # Destroy Session
    session.clear()

    # Logout Message
    flash(
        "You have been logged out successfully.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )